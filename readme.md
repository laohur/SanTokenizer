# langer

language processor
tokenizer better than BERT

## tokenize

### use
```python
from langer import Langer
tokenizer=Langer()

doc0 = """ 
        首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
        的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
        하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
        est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
    """
```

### result 
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

##  todo
* segment sentence
Some tool use ICU(https://unicode-org.github.io/icu/userguide/boundaryanalysis/break-rules.html) to segment sentence for multi-languages. But ICU is hard to install.

## License
[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)