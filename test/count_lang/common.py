import os
import gzip
import bz2
import lzma
from collections import Counter
import unicodedata

from logzero import logger


def read(path):
    if path.endswith('.xz'):
        with lzma.open(path, mode="rt") as reader:
            for l in reader:
                yield l
    elif path.endswith('.bz2'):
        with bz2.BZ2File(path, mode="rb") as reader:
            for l in reader:
                yield l.decode()
    elif path.endswith('.gz'):
        with gzip.open('big_file.txt.gz', 'rb') as reader:
            for l in reader:
                yield l.decode()
    else:
        with open(path) as reader:
            for l in reader:
                yield l
    # return reader


def read1(path):
    if path.endswith('.xz'):
        cmd = f"xzcat "+path
    elif path.endswith('.bz2'):
        cmd = "bzip2 -d -c "+path
    elif path.endswith('.gz'):
        cmd = "zcat "+path
    else:
        cmd = "cat "+path
    # return cmd
    with os.popen(cmd) as p:
        for l in p:
            yield l


def mopen(path):
    if path.endswith('xz'):
        return lzma.open(path, mode="rt")
    else:
        return open(path)


def read_frequency(p):
    for l in read(p):
        w = l.split()
        if len(w) != 2:
            continue
        word = w[0]
        num = int(w[1])
        if num == 1:
            continue
        yield word, num


def load_frequency(p):
    # counter=Counter()
    for i, l in enumerate(read1(p)):
        w = l.strip().split()
        if len(w) != 2:
            continue
        word, num = w
        num = int(num)
        if num == 1:
            continue
        # counter[word]+=num
        yield (word, num)
    # logger.info(f"  {p}  lines:{i} counter:{len(counter)} ")

    # return counter


if __name__ == "__main__":
    # load_frequency(f"../lang/ab/word_frequency.txt.xz")
    names = set()
    tails = set()
    for i in range(0x110000):
        c = chr(i)
        try:
            name = unicodedata.name(c)
        except:
            name = unicodedata.category(c)
        # r = name.split()[-1].split('-')[-1].lower()
        tail = name.split()[-1].lower()
        r = name[:2].lower()
        names.add(r)
    print(tails)
    print(len(tails))

    print(names)
    print(len(names))
