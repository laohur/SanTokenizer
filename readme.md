# UnicodeTokenizer

tokenize for all Unicode text

## 切词规格 Tokenize Rules
* 空白切分 split on blank： '\n', ' ', '\t'
* 保留关键词 keep never_splits
* 字符分割 chars split： 以字的符号类别和语言分割 split line by category and languae of characters
    - 类别CZ替换为空格:  category C/Z  -> ' '
    - 类别为PS或大字符集，单字分割：category P/S or big alphabet  -> ' ' + x + ' '
    - 类别为LN且不同语言，新分割: Letter or Number of different languages ->  ' '+ x
    - 类别为M，替换为空格： category M -> ' '
* 若小写，则NFD规范化，再字符分割  nomalize NFD if lower， character split again： if lower: nomalize, then chars split 
    - 类别为M，略过 ingore if category M ： category M -> ''
* 截断 max_len


## use
```python
from UnicodeTokenizer import BasicTokenizer
tokenizer=BasicTokenizer()

doc0 = """ 
        首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
        的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
        하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
        est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
    """
tokenizer.tokenize(doc0)
```

## result 
UnicodeTokenizer
BertTokenizer

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

## reference
* Unicode Blocks  https://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt
* unicodedata.category https://www.unicode.org/reports/tr44/  #Table 12. General_Category Values
* 汉字区间 http://yedict.com/zsts.htm


## General_Category Values
| Abbr |          Long         |                     Description                    |
|:----:|:---------------------:|:--------------------------------------------------:|
| Lu   | Uppercase_Letter      | an uppercase letter                                |
| Ll   | Lowercase_Letter      | a lowercase letter                                 |
| Lt   | Titlecase_Letter      | a digraphic character, with first part uppercase   |
| LC   | Cased_Letter          | Lu \| Ll \| Lt                                     |
| Lm   | Modifier_Letter       | a modifier letter                                  |
| Lo   | Other_Letter          | other letters, including syllables and ideographs  |
| L    | Letter                | Lu \| Ll \| Lt \| Lm \| Lo                         |
| Mn   | Nonspacing_Mark       | a nonspacing combining mark (zero advance width)   |
| Mc   | Spacing_Mark          | a spacing combining mark (positive advance width)  |
| Me   | Enclosing_Mark        | an enclosing combining mark                        |
| M    | Mark                  | Mn \| Mc \| Me                                     |
| Nd   | Decimal_Number        | a decimal digit                                    |
| Nl   | Letter_Number         | a letterlike numeric character                     |
| No   | Other_Number          | a numeric character of other type                  |
| N    | Number                | Nd \| Nl \| No                                     |
| Pc   | Connector_Punctuation | a connecting punctuation mark, like a tie          |
| Pd   | Dash_Punctuation      | a dash or hyphen punctuation mark                  |
| Ps   | Open_Punctuation      | an opening punctuation mark (of a pair)            |
| Pe   | Close_Punctuation     | a closing punctuation mark (of a pair)             |
| Pi   | Initial_Punctuation   | an initial quotation mark                          |
| Pf   | Final_Punctuation     | a final quotation mark                             |
| Po   | Other_Punctuation     | a punctuation mark of other type                   |
| P    | Punctuation           | Pc \| Pd \| Ps \| Pe \| Pi \| Pf \| Po             |
| Sm   | Math_Symbol           | a symbol of mathematical use                       |
| Sc   | Currency_Symbol       | a currency sign                                    |
| Sk   | Modifier_Symbol       | a non-letterlike modifier symbol                   |
| So   | Other_Symbol          | a symbol of other type                             |
| S    | Symbol                | Sm \| Sc \| Sk \| So                               |
| Zs   | Space_Separator       | a space character (of various non-zero widths)     |
| Zl   | Line_Separator        | U+2028 LINE SEPARATOR only                         |
| Zp   | Paragraph_Separator   | U+2029 PARAGRAPH SEPARATOR only                    |
| Z    | Separator             | Zs \| Zl \| Zp                                     |
| Cc   | Control               | a C0 or C1 control code                            |
| Cf   | Format                | a format control character                         |
| Cs   | Surrogate             | a surrogate code point                             |
| Co   | Private_Use           | a private-use character                            |
| Cn   | Unassigned            | a reserved unassigned code point or a noncharacter |
| C    | Other                 | Cc \| Cf \| Cs \| Co \| Cn                         |


## License
[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)
