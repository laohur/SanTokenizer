import glob
from collections import Counter
import os
import unicodedata
from timeit import repeat
from langer import is_hanzi,split_chars,split_category,strip_accents,split_lanugage,split_punctuation,Langer
from tokenization import BasicTokenizer



if __name__ == "__main__":
    line=''
    for i in range(128):
        try:
            c=chr(i)
            line+=c
        except:
            pass
    line = '㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)'
    # s=line
    s=split_chars(line)
    s=split_category(line)
    s=strip_accents(line)
    s=split_lanugage(line)
    s=split_punctuation(line)

    print(s)
    for x in line :
        try:
            c=unicodedata.category(x)
            n=unicodedata.name(x)
            print(x,c,n,is_hanzi(x))
        except:
            print(x,c,'err')
            pass
    # ['[', ']', 'viiipays', '-', 'grand', '-', 'blanc', '-', 'eleve', '»', '(', '白', '高', '大', '夏', '國', ')']
    # a=tokenizer=Langer()
    a=tokenizer=Langer(do_lower_case=False)
    # b=tokenizer=BasicTokenizer()
    b=tokenizer=BasicTokenizer(do_lower_case=False)
    def test():
        doc0 = """ 
                Ⅷ首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
                的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
                하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
               est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
            """

        for i, line in enumerate(doc0.split('\n')):
            line=line.strip()
            # print(tokenizer.tokenize(line))
            print(a.tokenize(line))
            print(b.tokenize(line))
            # a.tokenize(line)
    test()
    s = 'วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้'
    print(a.tokenize(s))
    # import timeit
    # print(timeit.timeit("unicodedata.category('c')",setup="import unicodedata",number=1000000))  # 0.08s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0]",setup="import unicodedata",number=1000000)) # 0.32s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0].strip()",setup="import unicodedata",number=1000000)) # 0.36s
    # print(timeit.timeit("test()",setup="from __main__ import test",number=10000)) # 11.02s
    
""" tokenize result (both basic)
Langer
BERT 

[]
[]
['首', '先', '8', '.', '88', '设', '置', 'st', '。', 'art', '_', 'new', '_', 'word', '=', 'true', '和', 'output', '=', '[', 'acai', ']', '，', 'output', '就', '是', '最', '终', 'no', 'such', 'name', '"']
['首', '先', '8', '.', '88', '设', '置', 'st', '。', 'art', '_', 'new', '_', 'word', '=', 'true', '和', 'output', '=', '[', 'acai', ']', '，', 'output', '就', '是', '最', '终', 'no', 'such', 'name', '"']
['的', '输', '出', 'ค', 'ณจะจ', 'ดพ', 'ธ', 'แต', 'งงานเม', 'อไรคะ', '탑', '승', '수', '속', '해', '야', 'pneumonoultramicroscopicsilicovolcanoconiosis', '"']
['的', '输', '出', 'คณจะจดพธแตงงานเมอไรคะ탑승', '수속해야pneumonoultramicroscopicsilicovolcanoconiosis', '"']
['하', '는', '데', '카', '운', '터', '가', '어', '디', '에', '있', '어', '요', 'ꆃ', 'ꎭ', 'ꆈ', 'ꌠ', 'ꊨ', 'ꏦ', 'ꏲ', 'ꅉ', 'ꆅ', 'ꉚ', 'ꅉ', 'ꋍ', 'ꂷ', 'ꂶ', 'ꌠ
', 'لاحياء', 'تمارين', 'تتطلب', 'من', '[MASK]', '[PAD]', '[', 'cls', ']', '[', 'sep', ']']
['하는데', '카운터가', '어디에', '있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلاحياء', 'تمارين', 'تتطلب', 'من', '[MASK]', '[PAD]', '[', 'cls', ']', '[', 'sep', ']']
['est', ',', 'ou', '"', 'phiow', '-', 'bjij', '-', 'lhjij', '-', 'lhjij', '"', ',', 'ce', 'que', 'l', "'", 'on', 'peut', 'traduire', 'par', '«', 'pays', '-', 'grand', '-', 'blanc', '-', 'eleve', '»', '(', '白', '高', '大', '夏', '國', ')', '.']
['est', '𗴂𗹭𘜶𗴲𗂧', ',', 'ou', '"', 'phiow', '-', 'bjij', '-', 'lhjij', '-', 'lhjij', '"', ',', 'ce', 'que', 'l', "'", 'on', 'peut', 'traduire', 'par', '«', 'pays', '-', 'grand', '-', 'blanc', '-', 'eleve', '»', '(', '白', '高', '大', '夏', '國', ')', '.']
[]
[]
"""
