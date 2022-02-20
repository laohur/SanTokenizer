import glob
from collections import Counter
import os
import unicodedata
from timeit import repeat
from langer import is_hanzi, split_chars, split_category, strip_accents, split_lanugage, split_punctuation, Langer
from tokenization import BasicTokenizer


if __name__ == "__main__":
    line = ''
    for i in range(128):
        try:
            c = chr(i)
            line += c
        except:
            pass
    line = '〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)'
    # s=line
    s = split_chars(line)
    s = split_category(line)
    s = strip_accents(line)
    s = split_lanugage(line)
    s = split_punctuation(line)

    print(s)
    for x in line:
        try:
            c = unicodedata.category(x)
            n = unicodedata.name(x)
            print(x, c, n, is_hanzi(x))
        except:
            print(x, c, 'err')
            pass
    # ['[', ']', 'viiipays', '-', 'grand', '-', 'blanc', '-', 'eleve', '»', '(', '白', '高', '大', '夏', '國', ')']
    # a=tokenizer=Langer()
    a = tokenizer = Langer(do_lower_case=False)
    # b=tokenizer=BasicTokenizer()
    b = tokenizer = BasicTokenizer(do_lower_case=False)

    def test():
        doc0 = """ 
                Ⅷ首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
                的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
                하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
               est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
            """

        for i, line in enumerate(doc0.split('\n')):
            line = line.strip()
            # print(tokenizer.tokenize(line))
            tokens = a.tokenize(line)
            print(' '.join(tokens))
            print(len(tokens))

            tokens = b.tokenize(line)
            print(' '.join(tokens))
            print(len(tokens))
            # a.tokenize(line)
    test()
    s = 'วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้'
    tokens = a.tokenize(s)
    print(' '.join(tokens))
    print(len(tokens))
    s = 'ສົມເດັດພະເຈົ້າຢູ່ຫົວບໍຣົມໂກດຊົງທຳນຸບຳລຸງບ້ານເມືອງແລະພະສາດສະໜາຈົນກ່າວໄດ້ວ່າກຸງສີອະຍຸທະຢາໃນສະໄໝພະອົງນັ້ນເປັນຍຸກທີ່ບ້ານເມືອງດີ ມີຂຸນນາງຄົນສຳຄັນທີ່ເຕີບໂຕໃນເວລາຕໍ່ມາ ໃນລາຊະການຂອງພະອົງຫຼາຍຄົນ ເຊັ່ນ ສົມເດັດພະເຈົ້າກຸງທົນບຸລີ, ພະບາດສົມເດັດພະພຸດທະຍອດຟ້າຈຸລາໂລກມະຫາລາດ ເປັນຕົ້ນ ໃນທາງດ້ານວັນນະຄະດີກໍມີກະວີຄົນສຳຄັນ ເຊັ່ນ ເຈົ້າຟ້າທຳມາທິເບດໄຊຍະເຊດສຸລິຍະວົງ ກົມມະຂຸນເສນາພິທັກ ຫຼືເຈົ້າຟ້າກຸ້ງ ເຊິ່ງເປັນພະໂອລົດ ເປັນຕົ້ນ'
    tokens = a.tokenize(s)
    print(' '.join(tokens))
    print(len(tokens))
    # import timeit
    # print(timeit.timeit("unicodedata.category('c')",setup="import unicodedata",number=1000000))  # 0.08s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0]",setup="import unicodedata",number=1000000)) # 0.32s
    # print(timeit.timeit("unicodedata.name('c').split(' ')[0].strip()",setup="import unicodedata",number=1000000)) # 0.36s
    # print(timeit.timeit("test()",setup="from __main__ import test",number=10000)) # 11.02s

""" tokenize result (both basic)
Langer
BERT 

0
Ⅷ 首 先 8 . 88 设 置 st 。 art _ new _ word = True 和 output = [ açaí ] ， output 就 是 最 终    no such name "
36
Ⅷ 首 先 8 . 88 设 置 st 。 art _ new _ word = True 和 output = [ açaí ] ， output 就 是 最 终 no such name "
33
的 输 出 คุ ณจะจั ดพิ ธี แต่ งงานเมื่ อไรคะ 탑 승 수 속 해 야 pneumonoultramicroscopicsilico volcanoconiosis "
19
的 输 出 คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis "
6
하 는 데 카 운 터 가 어 디 에 있 어 요 ꆃ ꎭ ꆈ ꌠ ꊨ ꏦ ꏲ ꅉ ꆅ ꉚ ꅉ ꋍ ꂷ ꂶ ꌠ لأحياء تمارين تتطلب من [ MASK ] [ PAD ] [ CLS ] [ SEP ]
44
하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [ CLS ] [ SEP ]
15
est 𗴂 𗹭 𘜶 𗴲 𗂧 , ou " phiow - bjij - lhjij - lhjij " , ce que l ' on peut traduire par « pays - grand - blanc - élevé » ( 白 高 大 夏 國 ) .
43
est 𗴂𗹭𘜶𗴲𗂧 , ou " phiow - bjij - lhjij - lhjij " , ce que l ' on peut traduire par « pays - grand - blanc - élevé » ( 白 高 大 夏 國 ) .
39

0

0
วรรณพงษ์ เป็ นนั กศึ กษาชั้ นปี ที่ หนึ่ ง เรี ยนสาขาวิ ทยาการคอมพิ วเตอร์ และสารสนเทศคณะวิ ทยาศาสตร์ ประยุ กต์ และวิ ศวกรรมศาสตร์ อยู่ ที่ มหาวิ ทยาลั ยขอนแก่ นวิ ทยาเขตหนองคายยื มคื น
ทรั พยากรห้ องสมุ ดเอกสารสั มมนาคอมพิ วเตอร์ ปั ญญาประดิ ษฐ์ กั บการพั ฒนาเกมแมวกิ นปลาหิ วววไหมหลั กสู ตรใหม่ สดสดทนได้
44
ສົ ມເດັ ດພະເຈົ້ າຢູ່ ຫົ ວບໍ ຣົ ມໂກດຊົ ງທຳນຸ ບຳລຸ ງບ້ ານເມື ອງແລະພະສາດສະໜາຈົ ນກ່ າວໄດ້ ວ່ າກຸ ງສີ ອະຍຸ ທະຢາໃນສະໄໝພະອົ ງນັ້ ນເປັ ນຍຸ ກທີ່ ບ້ ານເມື ອງດີ ມີ ຂຸ ນນາງຄົ ນສຳຄັ ນທີ່ ເຕີ ບໂຕໃນເວ
ລາຕໍ່ ມາ ໃນລາຊະການຂອງພະອົ ງຫຼ າຍຄົ ນ ເຊັ່ ນ ສົ ມເດັ ດພະເຈົ້ າກຸ ງທົ ນບຸ ລີ , ພະບາດສົ ມເດັ ດພະພຸ ດທະຍອດຟ້ າຈຸ ລາໂລກມະຫາລາດ ເປັ ນຕົ້ ນ ໃນທາງດ້ ານວັ ນນະຄະດີ ກໍ ມີ ກະວີ ຄົ ນສຳຄັ ນ ເຊັ່ ນ ເຈ
ົ າຟ້ າທຳມາທິ ເບດໄຊຍະເຊດສຸ ລິ ຍະວົ ງ ກົ ມມະຂຸ ນເສນາພິ ທັ ກ ຫຼື ເຈົ້ າຟ້ າກຸ້ ງ ເຊິ່ ງເປັ ນພະໂອລົ ດ ເປັ ນຕົ້ ນ
93
"""
