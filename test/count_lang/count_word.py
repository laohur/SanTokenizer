import math
import shutil
from store import get_langs, lang_files
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
            if n_line == 1 and max([ord(x) for x in l]) < 128:  # bad msg
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

    words = list(counter.items())
    del counter
    words.sort(key=lambda x: (-x[1], len(x[0]), x[0]))
    with open(tgt, "w") as f:
        for k, v in words:
            f.write(f"{k}\t{v}"+'\n')
    logger.info(f" word_counter:{len(words)} --> {tgt}  ")
    return lang+f' {len(words)}'


def load_frequency(p, max_len=20):
    doc = open(p).read().splitlines()
    for i in range(len(doc)):
        k, v = doc[i].split('\t')[:2]
        doc[i] = (k, int(v))
    logger.info(f" {p} load {len(doc)} words")
    return doc


def coung_global():
    counter = Counter()
    langs = get_langs()

    # freq_path=f"C:/data/languages/*/word_frequency.tsv"
    freq_paths = [
        f"C:/data/languages/{lang}/word_frequency.tsv" for lang in langs]
    # pipe='cat '+' '.join(freq_paths)
    for src in freq_paths:
        if not os.path.exists(src):
            continue
        for l in open(src):
            l = l.strip()
            w = l.split('\t')
            k, v = w
            v = int(v)
            if v <= 1 or len(k) >= 20:
                k = ' '
            counter[k] += math.sqrt(v)
        logger.info(f"src：{src} counter:{len(counter)}")
    words = [(k, int(v)) for k, v in counter.items()]
    del counter
    words.sort(key=lambda x: (-x[1], len(x[0]), x[0]))
    total = 0
    tgt = f"C:/data/languages/global/word_frequency.tsv"
    with open(tgt, "w") as f:
        for k, v in words:
            f.write(f"{k}\t{v}"+'\n')
            total += 1
    logger.info(f" word_counter:{total} --> {tgt}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', default="global",  type=str)
    args = parser.parse_args()
    print(args)

    coung_global()
    # langs = get_langs()
    # for lang in langs:
    #     scan_lang(lang)
