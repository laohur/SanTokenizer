import glob
from collections import Counter
import os
import unicodedata
from timeit import repeat
from langer import BasicTokenizer

if __name__ == "__main__":

    line = '[ัีิ์ื็ํึ]Ⅷpays-grand-blanc-élevé » (白高大夏國)'
    tokenizer=BasicTokenizer()
    print(tokenizer.tokenize(line))

    # ['[', ']', 'viiipays', '-', 'grand', '-', 'blanc', '-', 'eleve', '»', '(', '白', '高', '大', '夏', '國', ')']

    def test():
        doc0 = """
                首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
                的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
                하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من 
               est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
            """

        for i, line in enumerate(doc0.split('\n')):
            line=line.strip()
            print(tokenizer.tokenize(line))
            tokenizer.tokenize(line)
    test()

    import timeit
    # print(timeit.timeit("unicodedata.category('c')",setup="import unicodedata",number=1000000))  # 0.11s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0]",setup="import unicodedata",number=1000000)) # 0.46s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0].strip()",setup="import unicodedata",number=1000000)) # 0.47s
    # print(timeit.timeit("test()",setup="from __main__ import test",number=10000)) # 7.60s
    