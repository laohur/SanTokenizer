import glob
from collections import Counter
import os

from logzero import logger


def get_langs():
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z')+1))
    langs = [x+y for x in alphabet for y in alphabet]
    return langs


def lang_files(lang):
    # C:/data/wiki-20220606-cirrussearch-content-txt-bz2/aawiki-20220606-cirrussearch-content.txt.bz2
    files = glob.glob(
        f"C:/data/wiki-20220606-cirrussearch-content-txt-bz2/{lang}*-20220606-cirrussearch-content.txt.bz2")

    return list(files)


if __name__ == "__main__":
    counter = Counter()
    langs = get_langs()
    for i, x in enumerate(langs):
        counter[x] = i
    doc = list(counter.items())
    doc.sort(key=lambda x:(-x[1],x[0]))        
    print(doc)