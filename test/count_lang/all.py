import random
import os
import lzma
import subprocess
from collections import Counter
import logzero
from logzero import logger
import multiprocessing
from multiprocessing import Pool

from store import get_langs
from common import read, read_frequency
from count_word import scan_lang


def scan(langs):
    with Pool(4) as p:
        res = p.imap_unordered(scan_lang, langs)
        for x in res:
            logger.info(f"{x}")
    # for la in langs:
        # la='yo'
        # cmd=f" python scan_xz.py --lang={la} "
        # print(cmd)
        # subprocess.call(cmd,shell=True)


def merge_global_word(langs):
    logzero.logfile(f"../lang/global/merge_global_word.log", 'w')
    counter = Counter()
    files = []
    for j, lang in enumerate(langs):
        dir = "../lang/"+lang
        p = f"{dir}/word_frequency.txt.xz"
        if not os.path.exists(p):
            continue
        i = 0
        for x in read_frequency(p):
            i += 1
            word, num = x
            if num == 1:
                continue
            counter[word] += num
        logger.info(f" {p} files:{i} counter:{len(counter)} ")
    logger.info(f"  files:{len(langs)} counter:{len(counter)} ")
    tgt = f"../lang/global/word_frequency-unordered.txt"
    with open(tgt, 'w') as f:
        for k, v in counter.items():
            l = f"{k}\t{v}"
            f.write(l+'\n')
    logger.info(f" word_counter:{len(counter)} --> {tgt}  ")

# merge word frequency>1
# sort -k 2nr -k 1 word_frequency-unordered.txt > word_frequency.txt


def count_global_word():
    logzero.logfile(f"../lang/global/count_global_word.log", 'w')
    p = f"../lang/global/word_frequency-unordered.txt"
    freq2word = {}
    for word, num in read_frequency(p):
        if num == 1:
            continue
        if num not in freq2word:
            freq2word[num] = []
        freq2word[num].append(word)

    top = list(freq2word)
    top.sort(reverse=True)
    logger.info(f" freq2word:{len(freq2word)}   ")

    tgt = f"../lang/global/word_frequency.txt"
    with open(tgt, "w") as f:
        for freq in top:
            words = freq2word[freq]
            words.sort(key=lambda x: (len(x), x))
            for k in words:
                f.write(f"{k}\t{freq}"+'\n')
            del freq2word[freq]
            logger.info(f" frequency:{freq} words:{len(words)} --> {tgt}  ")
    os.system(f" xz {tgt} ")
    logger.info(f"  count_word_global 完成 \n")


if __name__ == "__main__":
    langs = get_langs()
    # for lang in langs[len(langs)//2+10:]:
        # scan_lang(lang)
    random.shuffle(langs)
    scan(langs)


"""
scan split
count word
count char

count word lower

"""
