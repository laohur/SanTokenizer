# langer

language processor

## get unicode block of a character
```python
from langer import get_block

line = 'pays-grand-blanc-élevé » (白高大夏國)'
for x in line:
    is_chinese=is_hanzi(x)
    start,end,block_name=get_block(x)
    char_name=unicodedata.name(x)
```

##  convert varirants to base character
```python    
print(shave_marks(line))
# pays-grand-blanc-eleve » (白高大夏國)
```

##  token a sentence for all languages
```python
line = 'pays-grand-blanc-élevé » (白高大夏國)'    print(tokenize(line))
# ['pays', '-', 'grand', '-', 'blanc', '-', 'élevé', '»', '(', '白', '高', '大', '夏', '國', ')']
```


##  todo
* segment sentence
Some tool use ICU(https://unicode-org.github.io/icu/userguide/boundaryanalysis/break-rules.html) to segment sentence for multi-languages. But ICU is hard to install.

## License
[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)