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


"""
http://yedict.com/zsts.htm
"""
ranges = [
    [0x2e80,0x2eff],
    [0x2e80,0x2eff],
    [0x2f00,0x2fdf],
    [0x2ff0,0x2fff],
    [0x3000,0x303f],
    [0x31c0,0x31ef],
    [0x31c0,0x31ef],
    [0x3200,0x32ff],
    [0x3300,0x33ff],
    [0x3400,0x4dbf],
    [0x3400,0x4dbf],
    [0x4e00,0x9fff],
    [0x4e00,0x9fff],
    [0xa490,0xa4cf],
    [0xf900,0xfaff],
    [0xf900,0xfaff],
    [0xfe30,0xfe4f],
    [0x16fe0,0x16fff],
    [0x1f200,0x1f2ff],
    [0x20000,0x2a6df],
    [0x20000,0x2a6df],
    [0x2a700,0x2b73f],
    [0x2a700,0x2b73f],
    [0x2b740,0x2b81f],
    [0x2b740,0x2b81f],
    [0x2b820,0x2ceaf],
    [0x2b820,0x2ceaf],
    [0x2ceb0,0x2ebef],
    [0x2ceb0,0x2ebef],
    [0x2f800,0x2fa1f],
    [0x2f800,0x2fa1f],
    [0x30000,0x3134f],
    [0x30000,0x3134f],
]
ranges.sort(key=lambda x:x[0])

def is_hanzi(c):
    """
    if character c is hanzi
    """
    point=ord(c)
    if ranges[0][0]<=point<=ranges[-1][1]:
        for a, b in ranges:
            if a <= point <= b:
                return True
    return False

def get_block_han():
    # import regex
    # def is_hanzi(char):
        # return bool(regex.match(r'\p{script=han}', char))
    block_han=[]

    for a,b,name in blocks:
        for x in ["cjk",  "ideograph", "stroke", "radical"]:
            if x in name.lower():
                # print(a,b,name)
                m=str(hex(a))
                n=str(hex(b))
                block_han.append([m,n])
                print('['+m+','+n+'],')

    # print(block_han)

    #     c=chr(a)
    #     if  regex.match(r'\p{script=han}',c):
    #         print(a,b,name,c)


# 去掉全部组合记号的函数
# https://zhuanlan.zhihu.com/p/86329130
def shave_marks(txt):
    # 把所有字符分解成基字符和组合记号
    norm_txt = unicodedata.normalize('NFD', txt)
    # unicodedata.combining('a')
    # 过滤掉所有组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    # 重组所有字符
    return unicodedata.normalize('NFKC', shaved)


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
        elif n-m+1 > 256 or is_hanzi(c) :
                c = ' '+c+' '
        elif name0 and name != name0:
            c = ' '+c
            # keep original

        l+=c
        cat0 = cat
        name0 = name

    tokens = [ x for x in l.split() if x]
    return tokens

def gen_bigrams():
    sets=[]
    for i in range(ord('0'),ord('9')+1):
        sets.append(chr(i))
    for i in range(ord('a'),ord('z')+1):
        sets.append(chr(i))
    words=set()
    for x in sets:
        words.add(x)
        for y in sets:
            words.add(x+y)
    return words

def trim(line):
    while line and  not '0'<=line[0]<='9' and not 'a'<=line[0]<='z':
        line=line[1:]
    while line and  not '0'<=line[-1]<='9' and not 'a'<=line[-1]<='z':
        line=line[:-1]
    return line

def trim_char_name(c):
    names=unicodedata.name(c).split(' ')
    a=names[0]
    b=names[-1]
    if '-' in a:
        a=a.split('-')[0]
    if '-' in b:
        b=b.split('-')[-1]
    a=trim(a.lower())  # cat
    b=trim(b.lower())  # index
    return a[:2],b[-2:]

def read_char_names():
    bigrams=gen_bigrams()
    cats=set()
    ids=set()
    for l in open("NamesList.txt"):
        l=l.rstrip()
        if not l or l[0] in ['\t','@',' ',';'] or '\t' not in l :
            continue
        names=l.split('\t')[-1].split(' ')
        a=names[0].lower()
        b=names[-1].lower()
        if '-' in a:
            a=a.split('-')[0]
        if '-' in b:
            b=b.split('-')[-1]
        a=trim(a)
        b=trim(b)

        cats.add(a[:2])
        ids.add(b[-2:])

    print(len(cats),' '.join(cats))
    print(len(ids),' '.join(ids))

if __name__=="__main__":

    get_block_han()

    a='\u2167'
    b=tokenize(a)
    
    print(b)
    print( unicodedata.combining('a'))
    for x in a:
        print(trim_char_name(a))