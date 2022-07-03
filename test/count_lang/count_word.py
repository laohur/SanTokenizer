import lzma
import shutil
from store import lang_files
from multiprocessing import Pool
import glob
from collections import Counter
import os
import time

from logzero import logger

from UnicodeTokenizer.UnicodeTokenizer import UnicodeTokenizer

from common import read

tokenizer = UnicodeTokenizer(max_len=20)


def token(line):
    return tokenizer.tokenize(line)


def count_files(files):
    counter = Counter()
    logger.info(f" reading:{files} ")
    for i, src in enumerate(files):
        logger.info(
            f" lang:{files[i]} file:{i}/{len(files)} counter:{len(counter)} ")
        n_line = 0
        reader = read(src)
        # with os.popen(cmd) as p:
        # for l in os.popen(p):
        for l in reader:
            n_line += 1
            if not l:
                continue
            if n_line==1 and max([ord(x) for x in l])<128:  # bad msg
                continue
            tokens = token(l)
            for x in tokens:
                if not x:
                    continue
                counter[x] += 1
    logger.info(
        f" n_line:{n_line} counter:{len(counter)} ")
    return counter


def scan_lang(lang):
    files = lang_files(lang)
    logger.info(f"{lang} found {len(files)} files")

    dir = f"C:/data/languages/{lang}"
    if len(files) == 0:
        logger.warning(f"{lang} no files")
        if os.path.exists(dir):
            shutil.rmtree(dir)
            logger.warning(f"{dir} removed")
        return lang+" none"

    os.makedirs(dir, exist_ok=True)
    tgt = f"{dir}/word_frequency.tsv"
    if os.path.exists(tgt):
        # os.remove(tgt)
        logger.warning(f"{tgt} 存在")
        return 
    counter = count_files(files)
    if not counter:
        logger.warning(f" word_counter:{len(counter)} --> None  ")
        if os.path.exists(dir):
            shutil.rmtree(dir)
            logger.warning(f"{dir} removed")
        return lang+" 0"


    words = [(k,v) for k,v in counter.items()]
    del counter
    words.sort(key=lambda x: (-x[1], len(x[0]), x[0]))
    with open(tgt, "w") as f:
        for k,v in words:
            f.write(f"{k}\t{v}"+'\n')
    logger.info(f" word_counter:{len(words)} --> {tgt}  ")
    return lang+f' {len(words)}'


def load(p):
    counter = Counter()
    t = 0
    for l in open(p):
        t += 1
        l = l.strip()
        w = l.split('\t')
        k = w[0]
        v = int(w[1])
        counter[k] += v
    logger.info(f" {p} --> total:{t} word_counter:{len(counter)} ")
    return counter


def merge_lang(lang):
    dir = lang
    tgt = f"{dir}/word_frequency.tsv"
    counter = load(tgt)
    words = list(counter)
    words.sort(key=lambda x: (-counter[x], len(x), x))
    with open(tgt, "w") as f:
        for k in words:
            v = counter[k]
            f.write(f"{k}\t{v}"+'\n')
    logger.info(f" word_counter:{len(counter)} --> {tgt}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', default="global",  type=str)
    # parser.add_argument('--lang', default="yo",  type=str)
    args = parser.parse_args()
    print(args)
    # lang = args.lang
    lang = "aa"

    scan_lang(lang)
    # merge_lang(lang)

    # langs=['ar','en','fr','ja','ru','zh','th','sw','ur']
    # for lang in langs:
    # count_lang(lang)
    # lang_sentence(lang)
    # from store import get_langs
    # import os
    # # import subprocess
    # langs = get_langs()
    # for lang in langs:
    #     # if lang =='zh':
    #     # continue
    #     scan_lang(lang)
