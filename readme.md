# UnicodeTokenizer

tokenize for all Unicode text

## 切词规格
\n空格\t先切
在never_split中不切

若小写：NFD规范化，忽略Mn，Punctuation切割

净化
独字左右间隔
类目不同间隔

语言不同切割

长度切割

组词规则：
忽略Mn
同为L，或者N，且同类语言，才组词

## tokenize



This specification defines default mechanisms; more sophisticated implementations can and should tailor them for particular locales or environments. For example, reliable detection of word boundaries in languages such as Thai, Lao, Chinese, or Japanese requires the use of dictionary lookup, analogous to English hyphenation. An implementation therefore may need to provide means to override or subclass the default mechanisms described in this annex. Note that tailoring can either add boundary positions or remove boundary positions, compared to the defaults specified here. 
(https://unicode.org/reports/tr29/#Sentence_Boundaries)

### use
```python
from ZiTokenizer import BasicTokenizer
tokenizer=BasicTokenizer()

doc0 = """ 
        首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
        的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
        하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
        est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
    """
tokenizer.tokenize(doc0)
```

### result 
ZiTokenizer
BERT 

```
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
```

## License
[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)
