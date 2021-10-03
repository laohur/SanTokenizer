import bisect
import unicodedata

# https://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt
blocks = []
for line in open("Blocks.txt"):
    line = line.strip()
    if not line or line[0] == '#':
        continue
    w = line.split('; ')
    name = w[1].strip()
    a, b = w[0].split('..')
    m = int(a, 16)
    n = int(b, 16)
    blocks.append([m, n, name])
    # r=n-m+1
    # if r>256:
    #     print(r,name)

# print(blocks)
starts = [x[0] for x in blocks]

def get_block(c):
    point=ord(c)    
    idx = bisect.bisect_right(starts, point)-1
    if 0 <= idx <= len(blocks) and blocks[idx][0] <= point <= blocks[idx][1]:
        return blocks[idx]
    else:
        return -1, -1, ''

# 去掉全部组合记号的函数
# https://zhuanlan.zhihu.com/p/86329130
def shave_marks(txt):
    # 把所有字符分解成基字符和组合记号
    norm_txt = unicodedata.normalize('NFD', txt)
    unicodedata.combining('a')
    # 过滤掉所有组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    # 重组所有字符
    return unicodedata.normalize('NFC', shaved)


"""
http://yedict.com/zsts.htm
"""
ranges = [
    [0x4E00, 0x9FA5],
    [0x9FA6, 0x9FFC],
    [0x3400, 0x4DB5],
    [0x4DB6, 0x4DBF],
    [0x20000, 0x2A6D6],
    [0x2A6D7, 0x2A6DD],
    [0x2A700, 0x2B734],
    [0x2B740, 0x2B81D],
    [0x2B820, 0x2CEA1],
    [0x2CEB0, 0x2EBE0],
    [0x30000, 0x3134A],
    [0x2F00, 0x2FD5],
    [0x2E80, 0x2EF3],
    [0xF900, 0xFAD9],
    [0x2F800, 0x2FA1D],
    [0x31C0, 0x31E3],
    [0x2FF0, 0x2FFB],
    [0x3105, 0x312F],
    [0x31A0, 0x31BA],
]


def is_hanzi(c):
    """
    if character c is hanzi
    """
    point=ord(c)
    for a, b in ranges:
        if a <= point <= b:
            return True
    return False

#  require regex
# def is_hanzi(char):
#     return bool(regex.match(r'\p{script=han}', char))


def tokenize(line,normalize=True):
    # token sentence to tokens
    if not isinstance(line,str):
        return None
    if not line:
        return []
    if normalize:
        line=shave_marks(line)
    l = ''
    cat0 = ''
    name0 = ''
    for c in line:
        if not c:
            continue
        cat = unicodedata.category(c)[0]
        # https://zhuanlan.zhihu.com/p/93029007 https://www.zmonster.me/2018/10/20/nlp-road-3-unicode.html
        m, n, name = get_block(c)
        try:
            name = unicodedata.name(c).split(' ')[0]
        except Exception as e :
            # print( str(hex(ord(c)))+' '+c+' '+str(e))
            pass
        c = c.strip()
        if not c:
            c = ' '
        elif cat == 'C':
            c = ' '
        elif cat in 'MPSZ' :
            c = ' '+c+' '
        elif cat0 and  cat != cat0:
            c = ' '+c
        elif n-m+1 > 256 or name[:3]=='CJK' :
                c = ' '+c+' '
        elif name[:3]=='CJK':
            c = ' '+c+' '
        elif name0 and name != name0:
            c = ' '+c
            # keep original

        l+=c
        cat0 = cat
        name0 = name

    tokens = [ x for x in l.split() if x]
    return tokens

