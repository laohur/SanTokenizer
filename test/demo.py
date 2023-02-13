# -*- coding: utf-8 -*-


from timeit import repeat
from UnicodeTokenizer  import UnicodeTokenizer
from BertTokenization import BasicTokenizer as BertBasicTokenizer


def demo(doc):
    head = ["sentence", "UnicodeTokenizer",
            "Unicode Tokens Length", "BertBasicTokenizer", "Bert Tokens length"]
    result = [head]
    for line in doc[1:]:
        tokens1 = UnicodeTokenizer.tokenize(line)
        tokens2 = BertTokenizer.tokenize(line)
        row = [line, ' '.join(tokens1), len(tokens1),
               ' '.join(tokens2), len(tokens2)]
        result.append(row)
    # result='\n'.join(result)
    print(result)
    with open("data/result.tsv", "w") as f:
        for row in result:
            line = '\t'.join(str(x) for x in row)
            f.write(line+'\n')


if __name__ == "__main__":

    UnicodeTokenizer = UnicodeTokenizer(never_split=["[UNK]", "[SEP]", "[PAD]", "[CLS]", "[MASK]"])
    BertTokenizer = BertBasicTokenizer()

    doc = ["'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x0000𧭏２０１９\U0010ffff",
           "Ⅷ首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name",
           "的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis",
           "하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]",
           '''est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國).''',
           'วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้',
           'ສົມເດັດພະເຈົ້າຢູ່ຫົວບໍຣົມໂກດຊົງທຳນຸບຳລຸງບ້ານເມືອງແລະພະສາດສະໜາຈົນກ່າວໄດ້ວ່າກຸງສີອະຍຸທະຢາໃນສະໄໝພະອົງນັ້ນເປັນຍຸກທີ່ບ້ານເມືອງດີ ມີຂຸນນາງຄົນສຳຄັນທີ່ເຕີບໂຕໃນເວລາຕໍ່ມາ ໃນລາຊະການຂອງພະອົງຫຼາຍຄົນ ເຊັ່ນ ສົມເດັດພະເຈົ້າກຸງທົນບຸລີ, ພະບາດສົມເດັດພະພຸດທະຍອດຟ້າຈຸລາໂລກມະຫາລາດ ເປັນຕົ້ນ ໃນທາງດ້ານວັນນະຄະດີກໍມີກະວີຄົນສຳຄັນ ເຊັ່ນ ເຈົ້າຟ້າທຳມາທິເບດໄຊຍະເຊດສຸລິຍະວົງ ກົມມະຂຸນເສນາພິທັກ ຫຼືເຈົ້າຟ້າກຸ້ງ ເຊິ່ງເປັນພະໂອລົດ ເປັນຕົ້ນ'
           ]
    demo(doc)


""" 

"""
