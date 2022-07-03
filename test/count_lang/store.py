import glob
from collections import Counter
import os

from logzero import logger



def get_langs():
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z')+1))
    langs = [ x+y for x in alphabet for y in alphabet ]
    return langs


def lang_files(lang):
    # C:/data/wiki-20220606-cirrussearch-content-txt-bz2/aawiki-20220606-cirrussearch-content.txt.bz2
    files = glob.glob(
        f"C:/data/wiki-20220606-cirrussearch-content-txt-bz2/{lang}*-20220606-cirrussearch-content.txt.bz2")

    return list(files)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', default="global",  type=str)
    args = parser.parse_args()
    print(args)
    lang = args.lang

    langs = get_langs()
    d = lang_files('zh')
    print(d)
    # langs=['ar','en','fr','ja','ru','zh','th','sw','ur']
    a = ord('a')
    z = ord('z')+1
    langs = [chr(x)+chr(y) for x in range(a, z) for y in range(a, z)]
    for lang in langs:
        print(lang, lang_files(lang))
