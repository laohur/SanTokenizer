
from logzero import logger
from collections import Counter
import os,glob
import math
from UnicodeTokenizer.UnicodeTokenizer import UnicodeTokenizer

tokenizer=UnicodeTokenizer()

def tokenize(x):
    return tokenizer.tokenize(x)

def read(p):
    counter=Counter()
    for l in open(p):
        l = l.strip()
        if not l:
            continue
        w = l.split('\t')
        if len(w) == 2:
            c = w[0]
            f = int(w[1])
            counter[c]+=f
    doc = [ (k,v) for k,v in counter.items() ]
    doc.sort(key=lambda x:x[1],reverse=True)
    logger.info(f" {p} load {len(doc)} words")  
    return doc

def describe(doc):
    total = sum(b for a, b in doc)
    word_len = sum(len(a)*b for a, b in doc)/total
    cover = [ b/total for a, b in doc]

    stone=0
    cover_stone=0
    for i in range(1,len(cover)):
        cover[i]+=cover[i-1]
        if not stone and math.log1p(i)*cover[i] > 10:
            stone = i
            cover_stone = cover[i]

    import  bisect
    pos1=[ bisect.bisect_right(cover,i/10) for i in range(10) ]
    pos2=[ bisect.bisect_right(cover,0.9+i/100) for i in range(10) ]
    pos3=[ bisect.bisect_right(cover,0.99+i/1000) for i in range(10) ]
    pos4=[ bisect.bisect_right(cover,0.999+i/10000) for i in range(10) ]

    return pos1, pos2, pos3, pos4, word_len, stone, cover_stone, cover

def gen_hot(lang):
    import logzero
    from logzero import logger
    dir=lang
    os.makedirs(dir,exist_ok=True)
    logzero.logfile(f"{dir}/bomb.log",mode="w")
    p=f"{dir}/word_frequency.txt"

    frequency = read(p)
    pos1, pos2, pos3, pos4, word_len, stone, cover_stone, cover = describe(frequency)
    logger.info(f"lang:{lang} word_len:{word_len:.4f} stone:{stone} cover_stone:{cover_stone:.4f} pos1:{pos1} ")
    logger.info(f"lang:{lang} 0.9+pos2:{pos2} ")
    logger.info(f"lang:{lang} 0.99+pos3:{pos3} ")
    logger.info(f"lang:{lang} 0.999+pos4:{pos4} ")

    pos=pos1[4]
    words= [ x[0] for x in frequency[:pos+1]   ]
    tgt=f"{dir}/cover5.txt"
    with open(tgt,'w') as f:
        for w in words:
            f.write(f"{w}\n")
    logger.info(f"  {lang} bomb  {len(words)} words --> {tgt} ")
    return words

def read_hot(lang):
    import logzero
    dir=lang
    os.makedirs(dir,exist_ok=True)
    t=f"{dir}/cover5.txt"
    hot=set()
    for l in open(t):
        l=l.strip()
        if l:
            hot.add(l)

    logger.info(f"{lang}:{len(hot)} ")
    return hot

def color(tokens,hot):
    return [ 1 if x in hot else 0 for x in tokens  ]

def count_line(colored,flag):
    if not colored:
        return []
    last=colored[0]
    lens=[]
    leng=0
    if last==flag:
        leng+=1
    for i in range(1,len(colored)):
        if colored[i]!=flag:
            lens.append(leng)
            leng=0
        else:
            leng+=1        
    lens.append(leng)
    return lens


def scan(l,hot,show=False):
    tokens=tokenize(l.strip().lower())
    colored=color(tokens,hot)
    if show:
        masked=' '.join(  x if not colored[i] else '〇'  for i,x in enumerate(tokens)   )
        logger.info(l)
        logger.info(masked)
    red=count_line(colored,1)
    black=count_line(colored,0)
    return red,black

import lzma
def count_file(path,hot,max_lines=0,red_counter=Counter(), black_counter=Counter()):
    t=0
    # for l in open(p):
    with lzma.open(path,mode="rt") as f:
        for l in f:
    # for l in  lzma.open(path,mode="rt"):
            red,black=scan(l.strip().lower(),hot)
            for x in red:
                if x:
                    red_counter[x]+=1
            for x in black:
                if x:
                    black_counter[x]+=1      
            t+=1
            if max_lines and t>=max_lines:
                break          
    return red_counter,black_counter

def avg_len(counter):
	total=0
	freq=0
	for k,v in counter.items():
		total+=k*v
		freq+=v
	avg=total/freq
	total-=counter[1]
	freq-=counter[1]
	avg_gt1=total/freq
	return avg,avg_gt1

zh='''
虽然科弗声称一开始对由其他作者执笔银河系漫游指南这个念头感到有点生气，但最后他认为这本书对他是＂一个绝佳的机会＂。
他因此可以＂和他自童年起就开始喜欢的小说人物一起创作，并且可以在继承道格拉斯·亚当斯原意的同时加入一些自己的声音＂。
亚当斯的遗孀，简·贝尔森，称她＂想不出一个比科弗更好的人选来为亚瑟，柴法德和马文注入新的活力＂并全力支持这本书。
在2009年3月9日，企鹅出版集团在伦敦举行了一个招待会。
会中公布了本书的封面，并宣布了一些相关的市场活动，如BBC广播剧的CD，以及Pan Books出版社对本系列前五部书的重新发行。
作为宣传活动的一部分，有一个网站被用来搜集访问者的留言，并称将在本书的发行当天把这些信息发送到太空深处。
Warerstones的科幻小说采购者Michael Rowley描述科弗和银河系漫游指南系列是一个＂绝佳的搭配＂。
不过该系列的一些书迷也表达了遗憾。
'''

en="""
‘The press is a mighty engine, sir,’ said Pott.
Mr. Pickwick yielded his fullest assent to the proposition.
‘But I trust, sir,’ said Pott, ‘that I have never abused the enormous power I wield. I trust, sir, that I have never pointed the noble instrument which is placed in my hands, against the sacred bosom of private life, or the tender breast of individual reputation; I trust, sir, that I have devoted my energies to—to endeavours—humble they may be, humble I know they are—to instil those principles of—which—are—’
Here the editor of the Eatanswill Gazette, appearing to ramble, Mr. Pickwick came to his relief, and said—
‘Certainly.’
‘And what, Sir,’ said Pott—‘what, Sir, let me ask you as an impartial man, is the state of the public mind in London, with reference to my contest with the Independent?’
‘Greatly excited, no doubt,’ interposed Mr. Perker, with a look of slyness which was very likely accidental.
‘The contest,’ said Pott, ‘shall be prolonged so long as I have health and strength, and that portion of talent with which I am gifted. From that contest, Sir, although it may unsettle men’s minds and excite their feelings, and render them incapable for the discharge of the everyday duties of ordinary life; from that contest, sir, I will never shrink, till I have set my heel upon the Eatanswill Independent. I wish the people of London, and the people of this country to know, sir, that they may rely upon me—that I will not desert them, that I am resolved to stand by them, Sir, to the last.’ ‘Your conduct is most noble, Sir,’ said Mr. Pickwick; and he grasped the hand of the magnanimous Pott. ‘You are, sir, I perceive, a man of sense and talent,’ said Mr. Pott, almost breathless with the vehemence of his patriotic declaration. ‘I am most happy, sir, to make the acquaintance of such a man.’
‘And I,’ said Mr. Pickwick, ‘feel deeply honoured by this expression of your opinion. Allow me, sir, to introduce you to my fellow–travellers, the other corresponding members of the club I am proud to have founded.’
‘I shall be delighted,’ said Mr. Pott.
Mr. Pickwick withdrew, and returning with his friends, presented them in due form to the editor of the Eatanswill Gazette.
‘Now, my dear Pott,’ said little Mr. Perker, ‘the question is, what are we to do with our friends here?’
‘We can stop in this house, I suppose,’ said Mr. Pickwick.
‘Not a spare bed in the house, my dear sir—not a single bed.’
"""

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', default="global",  type=str)
    args = parser.parse_args()
    print(args)
    lang = args.lang

    # gen_hot(lang)


    def test_lines(lang,doc):
        # gen_hot(lang)
        hot=read_hot(lang)
        t=0
        for l in doc.split('\n'):
            scan(l,hot,True)
            t+=1
            if t>=10:
                break
    test_lines('zh',zh)
    test_lines('en',en)


    # langs=['ar','en','fr','ja','ru','zh','th','sw','ur']
    # for lang in langs:
    #     print(f"===={lang}====")
    # #     hot=gen_hot(lang)
    #     hot=read_hot(lang)
    #     files=list(glob.glob(rf"C:/data/pretrain/wikicources/{lang}wikisource/*.xz",recursive=True))
    #     p=files[0]
    #     red_counter,black_counter=count_file(p,hot,1000)
    #     logger.info(f"red_counter {red_counter} avg_len  {avg_len(red_counter)} ")
    #     logger.info(f"black_counter {black_counter}  avg_len  {avg_len(black_counter)}  ")



"""
# raw
[I 211009 02:19:01 bomb:68] lang:ar half:751 p9:40007 p99:714826 p999:1962855 p9999:2130065 word_len:4.236165175764779 stone:53803 cover:0.9180126189242591
[I 211009 02:19:11 bomb:68] lang:en half:108 p9:10575 p99:367459 p999:3245140 p9999:5691158 word_len:4.253547322669194 stone:35775 cover:0.9537435931791999
[I 211009 02:19:16 bomb:68] lang:fr half:41 p9:11192 p99:306594 p999:1947355 p9999:2807840 word_len:4.081349236114406 stone:36409 cover:0.9521477619579167
[I 211009 02:19:42 bomb:68] lang:ja half:171 p9:3421 p99:7852097 p999:14036377 p9999:14654805 word_len:1.6614731129175149 stone:39329 cover:0.9452038036012321
[I 211009 02:19:50 bomb:68] lang:ru half:451 p9:61152 p99:1205109 p999:4118460 p9999:4705050 word_len:4.9485649140564965 stone:64467 cover:0.9030241748832335
[I 211009 02:19:51 bomb:68] lang:zh half:198 p9:1573 p99:7880 p999:226459 p9999:592069 word_len:1.0816164798574512 stone:22994 cover:0.9957195051817077
[I 211009 02:20:00 bomb:68] lang:th half:2336 p9:2958805 p99:4291330 p999:4424583 p9999:4437908 word_len:10.917366221990601 stone:670136 cover:0.7454211630361384
[I 211009 02:20:03 bomb:68] lang:sw half:170 p9:7486 p99:259658 p999:1329823 p9999:1630349 word_len:4.724880221961319 stone:34072 cover:0.958200318497699
[I 211009 02:20:07 bomb:68] lang:ur half:150 p9:5146 p99:99635 p999:1566328 p9999:2330357 word_len:3.411066796072937 stone:28181 cover:0.9759522442113341

# my
[I 211010 05:22:52 bomb:69] lang:ar half:706 p9:38119 p99:650907 p999:1852246 p9999:2023255 word_len:4.142004525468866 stone:52728 cover:0.9197183120013657
[I 211010 05:23:02 bomb:69] lang:en half:108 p9:10315 p99:341265 p999:2987433 p9999:5335091 word_len:4.239601011125864 stone:35431 cover:0.954622001643837
[I 211010 05:23:07 bomb:69] lang:fr half:41 p9:11068 p99:293902 p999:1828549 p9999:2689936 word_len:4.076873346546693 stone:36213 cover:0.9526349893112815
[I 211010 05:23:14 bomb:69] lang:ja half:156 p9:2440 p99:200757 p999:2625331 p9999:3316444 word_len:1.4865901441603508 stone:29095 cover:0.972921537203228
[I 211010 05:23:22 bomb:69] lang:ru half:451 p9:60605 p99:1177863 p999:4048019 p9999:4636176 word_len:4.934486282983768 stone:64224 cover:0.9033318919668537
[I 211010 05:23:23 bomb:69] lang:zh half:202 p9:1586 p99:7480 p999:170874 p9999:512269 word_len:1.0803129430284255 stone:22867 cover:0.9962649070208504
[I 211010 05:23:28 bomb:69] lang:th half:330 p9:130196 p99:2264962 p999:2682775 p9999:2724556 word_len:3.4818284021110517 stone:83377 cover:0.882524744966917
[I 211010 05:23:31 bomb:69] lang:sw half:172 p9:7456 p99:252554 p999:1291299 p9999:1591675 word_len:4.725873310539403 stone:33977 cover:0.9584565894721703
[I 211010 05:23:36 bomb:69] lang:ur half:153 p9:5085 p99:80016 p999:1163355 p9999:1935075 word_len:3.3723635543215558 stone:27756 cover:0.977399109737237

# bert
[I 211009 01:58:39 bomb:65] lang:ar half:751 p9:40007 p99:714826 p999:1962855 p9999:2130065 word_len:4.236165175764779 stone:53803 cover:0.9180126189242591
[I 211009 01:58:50 bomb:65] lang:en half:108 p9:10575 p99:367459 p999:3245140 p9999:5691158 word_len:4.253547322669194 stone:35775 cover:0.9537435931791999
[I 211009 01:58:54 bomb:65] lang:fr half:41 p9:11192 p99:306594 p999:1947355 p9999:2807840 word_len:4.081349236114406 stone:36409 cover:0.9521477619579167
[I 211009 01:59:20 bomb:65] lang:ja half:171 p9:3421 p99:7852097 p999:14036377 p9999:14654805 word_len:1.6614731129175149 stone:39329 cover:0.9452038036012321
[I 211009 01:59:29 bomb:65] lang:ru half:451 p9:61152 p99:1205109 p999:4118460 p9999:4705050 word_len:4.9485649140564965 stone:64467 cover:0.9030241748832335
[I 211009 01:59:30 bomb:65] lang:zh half:198 p9:1573 p99:7880 p999:226459 p9999:592069 word_len:1.0816164798574512 stone:22994 cover:0.9957195051817077
[I 211009 01:59:39 bomb:65] lang:th half:2336 p9:2958805 p99:4291330 p999:4424583 p9999:4437908 word_len:10.917366221990601 stone:670136 cover:0.7454211630361384
[I 211009 01:59:42 bomb:65] lang:sw half:170 p9:7486 p99:259658 p999:1329823 p9999:1630349 word_len:4.724880221961319 stone:34072 cover:0.958200318497699
[I 211009 01:59:46 bomb:65] lang:ur half:150 p9:5146 p99:99635 p999:1566328 p9999:2330357 word_len:3.411066796072937 stone:28181 cover:0.9759522442113341

[I 211010 05:58:44 bomb:184] ====ar====
[I 211010 05:58:50 bomb:71] lang:ar word_len:4.1420 stone:52728 cover_stone:0.9197 pos1:[1, 2, 11, 62, 244, 706, 1776, 4307, 11166, 38119] 
[I 211010 05:58:50 bomb:72] lang:ar 0.9+pos2:[38119, 44654, 52995, 63957, 78941, 100613, 134254, 192406, 311470, 650907]
[I 211010 05:58:50 bomb:73] lang:ar 0.99+pos3:[650907, 714244, 789443, 884448, 979453, 1092205, 1282215, 1472225, 1662236, 1852246]
[I 211010 05:58:50 bomb:184] ====en====
[I 211010 05:59:06 bomb:71] lang:en word_len:4.2396 stone:35431 cover_stone:0.9546 pos1:[1, 1, 4, 10, 26, 108, 374, 1061, 2918, 10315] 
[I 211010 05:59:06 bomb:72] lang:en 0.9+pos2:[10315, 12239, 14772, 18238, 23167, 30591, 42884, 66409, 123706, 341265]
[I 211010 05:59:06 bomb:73] lang:en 0.99+pos3:[341265, 392886, 457454, 539784, 647515, 793364, 1000557, 1317100, 1866366, 2987433]
[I 211010 05:59:06 bomb:184] ====fr====
[I 211010 05:59:14 bomb:71] lang:fr word_len:4.0769 stone:36213 cover_stone:0.9526 pos1:[1, 2, 5, 10, 19, 41, 184, 781, 2706, 11068] 
[I 211010 05:59:14 bomb:72] lang:fr 0.9+pos2:[11068, 13250, 16111, 19962, 25352, 33417, 46407, 69948, 122539, 293902]
[I 211010 05:59:14 bomb:73] lang:fr 0.99+pos3:[293902, 331257, 376948, 433924, 506621, 602801, 736933, 934922, 1245090, 1828549]
[I 211010 05:59:14 bomb:184] ====ja====
[I 211010 05:59:24 bomb:71] lang:ja word_len:1.4866 stone:29095 cover_stone:0.9729 pos1:[1, 2, 9, 30, 78, 156, 287, 511, 947, 2440] 
[I 211010 05:59:24 bomb:72] lang:ja 0.9+pos2:[2440, 2864, 3461, 4355, 5790, 8289, 13062, 23615, 53399, 200757]
[I 211010 05:59:24 bomb:73] lang:ja 0.99+pos3:[200757, 242162, 297088, 371785, 477247, 631628, 862102, 1226570, 1857427, 2625331]
[I 211010 05:59:24 bomb:184] ====ru====
[I 211010 05:59:38 bomb:71] lang:ru word_len:4.9345 stone:64224 cover_stone:0.9033 pos1:[1, 1, 5, 16, 92, 451, 1549, 4763, 14986, 60605] 
[I 211010 05:59:38 bomb:72] lang:ru 0.9+pos2:[60605, 72436, 87853, 108577, 137432, 179655, 245554, 358378, 582440, 1177863]
[I 211010 05:59:38 bomb:73] lang:ru 0.99+pos3:[1177863, 1292957, 1428388, 1591765, 1798301, 2046738, 2373492, 2741005, 3394512, 4048019]
[I 211010 05:59:38 bomb:184] ====zh====
[I 211010 05:59:40 bomb:71] lang:zh word_len:1.0803 stone:22867 cover_stone:0.9963 pos1:[1, 4, 21, 61, 118, 202, 330, 534, 874, 1586] 
[I 211010 05:59:40 bomb:72] lang:zh 0.9+pos2:[1586, 1710, 1852, 2020, 2227, 2490, 2839, 3349, 4312, 7480]
[I 211010 05:59:40 bomb:73] lang:zh 0.99+pos3:[7480, 8236, 9178, 10428, 12214, 15066, 20561, 32763, 63889, 170874]
[I 211010 05:59:40 bomb:184] ====th====
[I 211010 05:59:50 bomb:71] lang:th word_len:3.4818 stone:83377 cover_stone:0.8825 pos1:[1, 7, 18, 42, 118, 330, 929, 3202, 15318, 130196] 
[I 211010 05:59:50 bomb:72] lang:th 0.9+pos2:[130196, 171534, 230306, 314542, 441269, 629824, 872251, 1336488, 1800725, 2264962]
[I 211010 05:59:50 bomb:73] lang:th 0.99+pos3:[2264962, 2311385, 2357809, 2404233, 2450656, 2497080, 2543504, 2589927, 2636351, 2682775]
[I 211010 05:59:50 bomb:184] ====sw====
[I 211010 05:59:54 bomb:71] lang:sw word_len:4.7259 stone:33977 cover_stone:0.9585 pos1:[1, 2, 4, 16, 64, 172, 382, 820, 1968, 7456] 
[I 211010 05:59:54 bomb:72] lang:sw 0.9+pos2:[7456, 9012, 11117, 14088, 18411, 25062, 36116, 56571, 102566, 252554]
[I 211010 05:59:54 bomb:73] lang:sw 0.99+pos3:[252554, 284996, 324413, 373182, 434473, 513174, 617816, 766706, 957548, 1291299]
[I 211010 05:59:54 bomb:184] ====ur====
[I 211010 06:00:00 bomb:71] lang:ur word_len:3.3724 stone:27756 cover_stone:0.9774 pos1:[1, 3, 8, 20, 56, 153, 374, 839, 1887, 5085] 
[I 211010 06:00:00 bomb:72] lang:ur 0.9+pos2:[5085, 5796, 6679, 7802, 9292, 11372, 14543, 20024, 32133, 80016]
[I 211010 06:00:00 bomb:73] lang:ur 0.99+pos3:[80016, 92951, 110197, 133956, 168062, 218982, 299110, 434424, 675682, 1163355]

====ar====
[I 211106 16:49:38 bomb:86] ar:246 
[I 211106 16:49:41 bomb:198] red_counter Counter({1: 12620, 2: 1592, 3: 501, 4: 219, 5: 38, 7: 3, 6: 2, 9: 1}) avg_len  (1.2296340811965811, 2.4596774193548385) 
[I 211106 16:49:41 bomb:199] black_counter Counter({1: 5828, 2: 4096, 3: 2157, 4: 1164, 5: 685, 6: 394, 7: 255, 8: 140, 9: 120, 10: 47, 11: 42, 12: 24, 13: 20, 14: 13, 16: 11, 15: 8, 17: 6, 18: 3, 21: 3, 20: 2, 19: 2})  avg_len  (2.4750998668442077, 3.4103568320278503)
====en====
[I 211106 16:49:41 bomb:86] en:27
[I 211106 16:49:43 bomb:198] red_counter Counter({1: 25727, 2: 6611, 3: 1443, 4: 428, 5: 86, 6: 7, 7: 6, 9: 1, 8: 1}) avg_len  (1.3267560477994753, 2.306186648025166) 
[I 211106 16:49:43 bomb:199] black_counter Counter({1: 15290, 2: 9002, 3: 4471, 4: 2413, 5: 1387, 6: 728, 7: 426, 8: 242, 9: 167, 10: 74, 11: 59, 12: 32, 13: 26, 14: 20, 16: 13, 15: 10, 17: 7, 21: 4, 18: 3, 20: 2, 19: 2})  avg_len  (2.2446622840188493, 3.241670159262364)
====fr====
[I 211106 16:49:43 bomb:86] fr:20
[I 211106 16:49:44 bomb:198] red_counter Counter({1: 33808, 2: 8739, 3: 1874, 4: 492, 5: 93, 6: 9, 7: 6, 9: 1, 8: 1}) avg_len  (1.3205250649667948, 2.286758805171645) 
[I 211106 16:49:44 bomb:199] black_counter Counter({1: 20738, 2: 11617, 3: 5679, 4: 2972, 5: 1711, 6: 907, 7: 513, 8: 296, 9: 194, 10: 94, 11: 69, 12: 41, 13: 29, 14: 21, 16: 14, 15: 11, 17: 7, 21: 4, 18: 3, 20: 2, 19: 2})  avg_len  (2.185580090820052, 3.2021417348879515)
====ja====
[I 211106 16:49:44 bomb:86] ja:79
[I 211106 16:49:45 bomb:198] red_counter Counter({1: 38002, 2: 9620, 3: 2089, 4: 544, 5: 123, 6: 12, 7: 7, 9: 2, 8: 1}) avg_len  (1.3183928571428571, 2.2943216647846425) 
[I 211106 16:49:45 bomb:199] black_counter Counter({1: 23143, 2: 12764, 3: 6307, 4: 3712, 5: 1931, 6: 1105, 7: 560, 8: 352, 9: 220, 10: 129, 11: 80, 12: 51, 13: 37, 16: 28, 14: 27, 15: 22, 18: 12, 19: 12, 23: 10, 21: 9, 17: 8, 20: 8, 25: 7, 24: 5, 45: 5, 27: 5, 30: 4, 28: 4, 22: 4, 29: 4, 26: 4, 36: 4, 53: 3, 48: 3, 31: 3, 50: 2, 57: 2, 60: 2, 44: 2, 43: 2, 41: 2, 80: 2, 55: 1, 85: 1, 34: 1, 37: 1, 38: 1, 121: 1, 35: 1, 82: 1, 49: 1, 72: 1, 52: 1, 33: 1, 69: 1, 40: 1})  avg_len  (2.2980833827306855, 3.3918156333054212)
====ru====
[I 211106 16:49:45 bomb:86] ru:109 
[I 211106 16:49:45 bomb:198] red_counter Counter({1: 43171, 2: 10601, 3: 2424, 4: 640, 5: 152, 6: 30, 7: 25, 9: 4, 8: 4, 13: 2}) avg_len  (1.321823567559988, 2.3226480334245787) 
[I 211106 16:49:45 bomb:199] black_counter Counter({1: 25921, 2: 14413, 3: 7204, 4: 4205, 5: 2185, 6: 1271, 7: 625, 8: 375, 9: 235, 10: 133, 11: 88, 12: 54, 13: 37, 16: 28, 14: 27, 15: 22, 18: 12, 19: 12, 23: 10, 21: 9, 17: 8, 20: 8, 25: 7, 24: 5, 45: 5, 27: 5, 30: 4, 28: 4, 22: 4, 29: 4, 26: 4, 36: 4, 53: 3, 48: 3, 31: 3, 50: 2, 57: 2, 60: 2, 44: 2, 43: 2, 41: 2, 80: 2, 55: 1, 85: 1, 34: 1, 37: 1, 38: 1, 121: 1, 35: 1, 82: 1, 49: 1, 72: 1, 52: 1, 33: 1, 69: 1, 40: 1})  avg_len  (2.2864741507943473, 3.3606494008504058)
====zh====
[I 211106 16:49:45 bomb:86] zh:119
[I 211106 16:49:47 bomb:198] red_counter Counter({1: 54586, 2: 15326, 3: 4185, 4: 1427, 5: 408, 6: 132, 7: 61, 8: 14, 9: 10, 10: 4, 13: 2, 12: 1}) avg_len  (1.4055360050422816, 2.431803430690774)
[I 211106 16:49:47 bomb:199] black_counter Counter({1: 34065, 2: 19611, 3: 9732, 4: 5849, 5: 2795, 6: 1628, 7: 823, 8: 451, 9: 274, 10: 155, 11: 101, 12: 62, 13: 43, 14: 28, 16: 28, 15: 22, 18: 14, 19: 12, 23: 10, 21: 9, 17: 8, 20: 8, 25: 7, 24: 5, 45: 5, 27: 5, 30: 4, 28: 4, 22: 4, 29: 4, 26: 4, 36: 4, 53: 3, 48: 3, 31: 3, 50: 2, 57: 2, 60: 2, 44: 2, 43: 2, 41: 2, 
80: 2, 55: 1, 85: 1, 34: 1, 37: 1, 38: 1, 121: 1, 35: 1, 82: 1, 49: 1, 72: 1, 52: 1, 33: 1, 69: 1, 40: 1})  avg_len  (2.2565722652385536, 3.281943180184928)
====th====
[I 211106 16:49:47 bomb:86] th:119 
[I 211106 16:49:48 bomb:198] red_counter Counter({1: 57836, 2: 16600, 3: 4613, 4: 1626, 5: 454, 6: 156, 7: 63, 8: 16, 9: 10, 10: 4, 13: 2, 12: 1}) avg_len  (1.4170629508116146, 2.4415374814185604)
[I 211106 16:49:48 bomb:199] black_counter Counter({1: 36161, 2: 20829, 3: 10594, 4: 6295, 5: 3041, 6: 1771, 7: 906, 8: 513, 9: 308, 10: 181, 11: 115, 12: 70, 13: 48, 14: 31, 16: 30, 15: 24, 19: 15, 18: 14, 17: 10, 23: 10, 21: 9, 20: 8, 25: 7, 24: 5, 45: 5, 27: 5, 30: 4, 28: 4, 22: 4, 29: 4, 26: 4, 36: 4, 53: 3, 48: 3, 31: 3, 50: 2, 57: 2, 60: 2, 44: 2, 43: 2, 41: 2, 80: 2, 55: 1, 85: 1, 34: 1, 37: 1, 38: 1, 121: 1, 35: 1, 82: 1, 49: 1, 72: 1, 52: 1, 33: 1, 69: 1, 40: 1})  avg_len  (2.2724200034539757, 3.2970715955906913)
====sw====

无论黑红，先轰炸自身，其次0.5轰炸临近，左侧或者右侧

"""