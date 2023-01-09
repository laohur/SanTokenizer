# UnicodeTokenizer

UnicodeTokenizer: tokenize all Unicode text, tokenize blank char as a token as default

## 切词规则 Tokenize Rules
* 空白切分 split on blank： '\n', ' ', '\t'
* 保留关键词 keep never_splits
* 若小写，则规范化：全角转半角，则NFD规范化，再字符分割  nomalize if lower：full2half，nomalize NFD, then chars split 
    - 类别为M，略过 ingore if category M ： category M -> ''
* 字符分割 chars split： 以字的符号类别和语言分割 split line by category and languae of characters
    - 只有临近数字成词 only numers joind
    - 只有临近字母成词 only letters joind 
    - 高码点独字  split high UnicodePoint characters

* 截断 max_len


## use
> pip install UnicodeTokenizer

```python
from UnicodeTokenizer import UnicodeTokenizer
tokenizer=UnicodeTokenizer()

doc0 = """ 
        首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
        的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
        하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
        est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
    """
print(tokenizer.tokenize(doc0))
```

## result 
| sentence                                                                                                                                                                                                                                                                                                          | UnicodeTokenizer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Unicode Tokens Length | BertBasicTokenizer                                                                                                                                                                                                                                                                                                 | Bert Tokens length |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Ⅷ首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name                                                                                                                                                                                                                              | ⅷ 首 先 8 . 88 设 置 st 。 art _ new _ word = true 和 output = [ ac ̧ ai ́ ] ， output 就 是 最 终    no such name                                                                                                                                                                                                                                                                                                                                                                               | 38                    | ⅷ 首 先 8 . 88 设 置 st 。 art _ new _ word = true 和 output = [ acai ] ， output 就 是 最 终 no such name                                                                                                                                                                                                         | 32                 |
| 的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis                                                                                                                                                                                                                             | 的 输 出 ค ุ ณจะจ ั ดพ ิ ธ ี แต ่ งงานเม ื ่ อไรคะ 탑승 수속해야 pneumonoultramicroscopicsilicovolcanoconiosis                                                                                                                                                                                                                                                                                                                                                                                          | 20                    | 的 输 出 คณจะจดพธแตงงานเมอไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis                                                                                                                                                                                                                           | 5                  |
| 하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]                                                                                                                                                                                                         | 하는데 카운터가 어디에 있어요 ꆃ ꎭ ꆈ ꌠ ꊨ ꏦ ꏲ ꅉ ꆅ ꉚ ꅉ ꋍ ꂷ ꂶ ꌠ لا ٔ حياء تمارين تتطلب من [MASK] [PAD] [ cls ] [ sep ]                                                                                                                                                                                                                                                                                                                                                                 | 33                    | 하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلاحياء تمارين تتطلب من [MASK] [PAD] [ cls ] [ sep ]                                                                                                                                                                                                     | 15                 |
| est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國).                                                                                                                                                                                                    | est 𗴂 𗹭 𘜶 𗴲 𗂧 , ou " phiow - bjij - lhjij - lhjij " , ce que l ' on peut traduire par « pays - grand - blanc - e ́ leve ́ » ( 白 高 大 夏 國 ) .                                                                                                                                                                                                                                                                                                                                                   | 46                    | est 𗴂𗹭𘜶𗴲𗂧 , ou " phiow - bjij - lhjij - lhjij " , ce que l ' on peut traduire par « pays - grand - blanc - eleve » ( 白 高 大 夏 國 ) .                                                                                                                                                                            | 39                 |
| วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้                                                                                           | วรรณพงษ ์ เป ็ นน ั กศ ึ กษาช ั ้ นป ี ท ี ่ หน ึ ่ ง เร ี ยนสาขาว ิ ทยาการคอมพ ิ วเตอร ์ และสารสนเทศคณะว ิ ทยาศาสตร ์ ประย ุ กต ์ และว ิ ศวกรรมศาสตร ์ อย ู ่ ท ี ่ มหาว ิ ทยาล ั ยขอนแก ่ นว ิ ทยาเขตหนองคายย ื มค ื นทร ั พยากรห ้ องสม ุ ดเอกสารส ั มมนาคอมพ ิ วเตอร ์ ป ั ญญาประด ิ ษฐ ์ ก ั บการพ ั ฒนาเกมแมวก ิ นปลาห ิ วววไหมหล ั กส ู ตรใหม ่ สดสดทนได ้                                                                                                                                                                                | 92                    | วรรณพงษเปนนกศกษาชนปทหนง เรยนสาขาวทยาการคอมพวเตอรและสารสนเทศคณะวทยาศาสตรประยกตและวศวกรรมศาสตรอยทมหาวทยาลยขอนแกนวทยาเขตหนองคายยมคนทรพยากรหองสมดเอกสารสมมนาคอมพวเตอรปญญาประดษฐกบการพฒนาเกมแมวกนปลาหวววไหมหลกสตรใหมสดสดทนได                                                                                            | 2                  |
| ສົມເດັດພະເຈົ້າຢູ່ຫົວບໍຣົມໂກດຊົງທຳນຸບຳລຸງບ້ານເມືອງແລະພະສາດສະໜາຈົນກ່າວໄດ້ວ່າກຸງສີອະຍຸທະຢາໃນສະໄໝພະອົງນັ້ນເປັນຍຸກທີ່ບ້ານເມືອງດີ ມີຂຸນນາງຄົນສຳຄັນທີ່ເຕີບໂຕໃນເວລາຕໍ່ມາ ໃນລາຊະການຂອງພະອົງຫຼາຍຄົນ ເຊັ່ນ ສົມເດັດພະເຈົ້າກຸງທົນບຸລີ, ພະບາດສົມເດັດພະພຸດທະຍອດຟ້າຈຸລາໂລກມະຫາລາດ ເປັນຕົ້ນ ໃນທາງດ້ານວັນນະຄະດີກໍມີກະວີຄົນສຳຄັນ ເຊັ່ນ ເຈົ້າຟ້າທຳມາທິເບດໄຊຍະເຊດສຸລິຍະວົງ ກົມມະຂຸນເສນາພິທັກ ຫຼືເຈົ້າຟ້າກຸ້ງ ເຊິ່ງເປັນພະໂອລົດ ເປັນຕົ້ນ | ສ ົ ມເດ ັ ດພະເຈ ົ ້ າຢ ູ ່ ຫ ົ ວບ ໍ ຣ ົ ມໂກດຊ ົ ງທຳນ ຸ ບຳລ ຸ ງບ ້ ານເມ ື ອງແລະພະສາດສະໜາຈ ົ ນກ ່ າວໄດ ້ ວ ່ າກ ຸ ງສ ີ ອະຍ ຸ ທະຢາໃນສະໄໝພະອ ົ ງນ ັ ້ ນເປ ັ ນຍ ຸ ກທ ີ ່ ບ ້ ານເມ ື ອງດ ີ ມ ີ ຂ ຸ ນນາງຄ ົ ນສຳຄ ັ ນທ ີ ່ ເຕ ີ ບໂຕໃນເວລາຕ ໍ ່ ມາ ໃນລາຊະການຂອງພະອ ົ ງຫ ຼ າຍຄ ົ ນ ເຊ ັ ່ ນ ສ ົ ມເດ ັ ດພະເຈ ົ ້ າກ ຸ ງທ ົ ນບ ຸ ລ ີ , ພະບາດສ ົ ມເດ ັ ດພະພ ຸ ດທະຍອດຟ ້ າຈ ຸ ລາໂລກມະຫາລາດ ເປ ັ ນຕ ົ ້ ນ ໃນທາງດ ້ ານວ ັ ນນະຄະດ ີ ກ ໍ ມ ີ ກະວ ີ ຄ ົ ນສຳຄ ັ ນ ເຊ ັ ່ ນ ເຈ ົ ້ າຟ ້ າທຳມາທ ິ ເບດໄຊຍະເຊດສ ຸ ລ ິ ຍະວ ົ ງ ກ ົ ມມະຂ ຸ ນເສນາພ ິ ທ ັ ກ ຫ ຼ ື ເຈ ົ ້ າຟ ້ າກ ຸ ້ ງ ເຊ ິ ່ ງເປ ັ ນພະໂອລ ົ ດ ເປ ັ ນຕ ົ ້ ນ | 189                   | ສມເດດພະເຈາຢຫວບຣມໂກດຊງທຳນບຳລງບານເມອງແລະພະສາດສະໜາຈນກາວໄດວາກງສອະຍທະຢາໃນສະໄໝພະອງນນເປນຍກທບານເມອງດ ມຂນນາງຄນສຳຄນທເຕບໂຕໃນເວລາຕມາ ໃນລາຊະການຂອງພະອງຫາຍຄນ ເຊນ ສມເດດພະເຈາກງທນບລ , ພະບາດສມເດດພະພດທະຍອດຟາຈລາໂລກມະຫາລາດ ເປນຕນ ໃນທາງດານວນນະຄະດກມກະວຄນສຳຄນ ເຊນ ເຈາຟາທຳມາທເບດໄຊຍະເຊດສລຍະວງ ກມມະຂນເສນາພທກ ຫເຈາຟາກງ ເຊງເປນພະໂອລດ ເປນຕນ | 15                 |

## reference
* Unicode Blocks  https://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt
* unicodedata.category https://www.unicode.org/reports/tr44/  #Table 12. General_Category Values
* 汉字区间 http://yedict.com/zsts.htm


## License
[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)
