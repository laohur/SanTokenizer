# -*- coding: utf-8 -*-


from timeit import repeat
import sys
from UnicodeTokenizer import UnicodeTokenizer


def demo(doc):
    head = [
        "chars num"
        "tokens num",
        "sentence",
        "tokens",
    ]
    result = [head]
    for line in doc:
        tokens = uToker.tokenize(line)
        row = [len(line),len(tokens), line.replace("\n", "Ø"), "▁".join(tokens).replace("\n", "Ø")]
        result.append(row)
    print(result)
    with open("result.tsv", "w") as f:
        for row in result:
            line = "\t".join(str(x) for x in row)
            f.write(line + "\n")


if __name__ == "__main__":
    uToker = UnicodeTokenizer()

    doc = [
        "                                                          ",
        "ننصحك أن تستخدم كلمة سر فريدة لا تستخدمها على أي موقع شبكي آخر.",
        "แก๊สมีสกุล หรือ แก๊สมีตระกูล (ในอดีตเรียกว่า แก๊สเฉื่อย หรือบางครั้งใช้ชื่อว่า aerogens) เป็นกลุ่มของธาตุทางเคมีที่มีสมบัติคล้ายกัน ภายใต้ภาวะมาตรฐานสำหรับอุณหภูมิและความดันธาตุเหล่านี้ต่างไม่มีกลิ่น ไม่มีสี เป็นแก๊สอะตอมเดี่ยวซึ่งไม่มีความว่องไวต่อปฏิกริยาเคมี แก๊สมีสกุลที่เกิดในธรรมชาติทั้งหกธาตุ ได้แก่ ฮีเลียม (He), นีออน (Ne), อาร์กอน (Ar), คริปทอน (Kr), ซีนอน (Xe) (ในภาพตามลำดับ) และเรดอน (Rn)  โอกาเนสซอน (Og) เป็นธาตุสังเคราะห์มีความเป็นกัมมันตรังสีสูงมาก แม้ว่า IUPAC จัดโอกาเนสซอนเป็นแก๊สมีสกุลหรือหมู่ที่ 18 มันอาจไม่เฉื่อยทางเคมีเหมือนธาตุอื่นในหมู่เดียวกัน และถูกทำนายว่าจะสลายและแผ่กัมมันตรังสีเนื่องจากปรากฏการณ์สัมพัทธ์ เนื่องจากครึ่งชีวิตที่สั้นเพียง 0.7 ไมโครวินาทีของไอโซโทปตัวเดียว ทำให้คุณสมบัติทางเคมีของโอกาเนสซอนยังไม่มีการศึกษามากนัก     首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终� no such name",
        "ᠠᠩᠬ᠎ᠠ ᠳᠤᠮᠳᠠᠳᠤ ᠶᠢᠨ ᠮᠣᠩᠭᠤᠯ ᠬᠡᠯᠡᠨ ᠤ ᠬᠢᠴᠢᠶᠡᠯ ᠤᠨ ᠪᠡᠯᠡᠳᠭᠡᠮᠵᠢ ᠮᠢᠨᠣ ᠳᠤᠰᠬᠠᠢ ᠰᠡᠳᠤᠪ ᠤᠨ ᠭᠤᠣᠯ ᠠᠭᠤᠯᠭ᠎ᠠ ᠨᠢ ᠠᠩᠬ᠎ᠠ ᠳᠤᠮᠳᠠᠳᠤ ᠶᠢᠨ ᠮᠣᠩᠭᠤᠯ ᠬᠡᠯᠡᠨ ᠤ ᠬᠢᠴᠢᠶᠡᠯ ᠳᠤ ᠳᠠᠭᠠᠯᠳᠤᠭᠤᠯᠤᠨ ᠵᠣᠬᠢᠶᠠᠭᠰᠠᠨ ᠺᠣᠣᠷᠰᠸᠠᠢᠷ ᠪᠣᠯᠤᠨ᠎ᠠ᠃ ᠲᠤᠰ ᠺᠣᠣᠷᠰᠸᠠᠢᠷ ᠲᠤ ᠪᠠᠨ ᠰᠤᠷᠤᠭᠴᠢ ᠶᠢᠨ ᠰᠤᠷᠬᠤ ᠤᠷᠮ᠎ᠠ ᠪᠠᠬ᠎ᠠ ᠶᠢ ᠳᠠᠳᠠᠬᠤ᠂ ᠬᠢᠴᠢᠶᠡᠯ ᠤᠨ ᠭᠤᠣᠯᠳᠠᠯᠭ᠎ᠠ ᠬᠦᠴᠢᠷᠳᠡᠯᠭᠡ ᠶᠢ ᠳᠠᠭᠤᠯᠵᠤ ᠬᠢᠴᠢᠶᠡᠯᠯᠡᠭᠡ ᠶᠢᠨ ᠶᠠᠪᠤᠴᠠ ᠪᠠᠨ ᠪᠦᠷᠢᠨᠵᠢᠬᠦᠯᠵᠤ᠂ ᠮᠡᠳᠡᠯᠭᠡ ᠶᠢᠨ ᠥᠷᠭᠡᠳᠭᠡᠯ ᠢᠶᠠᠷ ᠳᠠᠮᠵᠢᠨ ᠵᠢᠭᠠᠨ ᠰᠤᠷᠭᠠᠬᠤ ᠴᠢᠨᠠᠷ ᠴᠢᠨᠰᠠᠭ᠎ᠠ ᠪᠠᠨ ᠳᠡᠭᠡᠭᠰᠢᠯᠡᠭᠦᠯᠬᠦ ᠬᠡᠰᠡᠨ ᠵᠣᠷᠢᠯᠭ᠎ᠠ ᠲᠠᠢ᠃ ᠲᠤᠰ ᠬᠥᠮᠦᠨ ᠤ ᠬᠤᠪᠢ ᠶᠢᠨ ᠬᠡᠪ ᠴᠢᠨᠠᠷ᠂ ᠮᠡᠳᠡᠯᠭᠡ ᠴᠢᠳᠠᠪᠤᠷᠢ ᠶᠢᠨ ᠮᠡᠬᠦᠰ ᠠᠴᠠ ᠪᠣᠯᠵᠤ ᠪᠡᠯᠡᠳᠭᠡᠮᠵᠢ ᠶᠢᠨ ᠳᠤᠮᠳᠠ ᠠᠰᠠᠭᠤᠳᠠᠯ ᠣᠷᠤᠰᠢᠵᠤ ᠪᠠᠢᠭ᠎ᠠ ᠨᠢ ᠯᠠᠪᠳᠠᠢ᠃ ᠠᠩᠬᠠᠷᠤᠯ ᠶᠢᠨ ᠬᠠᠨᠳᠤᠭᠤᠯᠤᠭᠰᠠᠨ ᠲᠠ ᠪᠦᠬᠦᠨ ᠢᠯᠡᠭᠦᠬᠡᠨ ᠰᠠᠨᠠᠯ ᠵᠥᠪᠯᠡᠯᠭᠡ ᠥᠭᠬᠦ ᠶᠢ ᠬᠦᠰᠡᠵᠤ ᠪᠠᠢᠨ᠎ᠠ᠃    的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis",
        "四色定理是一个著名的数学定理：如果在平面上划出一些邻接的有限区域，那么可以用四种颜色来给这些区域染色，使得每两个邻接区域染的颜色都不一样。被称为邻接的两个区域是指它们有一段公共的边界，而不仅仅是一个公共的交点。四色问题最早是由英国数学家法兰西斯·古德里在1852年提出的。人们发现，要证明宽松一点的“五色定理”很容易，但四色问题却出人意料地异常困难。1976年，数学家凯尼斯·阿佩尔和沃夫冈·哈肯借助电子计算机首次得到一个完全的证明，四色问题也终于成为四色定理。这是首个主要借助计算机证明的定理。",
        """est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). """,
        "蜂蜜とはミツバチが花の蜜を採集し、巣の中で加工、貯蔵したものをいう。約8割の糖分と約2割の水分によって構成され、ビタミンとミネラル類などの栄養素をわずかに含む。味や色は蜜源植物によって様々である。  本来はミツバチの食料であるが、しばしば他の生物が採集して食料としている。人類も「蜂蜜の歴史は人類の歴史」ということわざがあるように、古来、食用、薬用など様々な用途に用いている。人類は初め、野生のミツバチの巣から蜂蜜を採集していたが、やがてミツバチを飼育して採集すること（養蜂）を身に付けた。人類による蜂蜜の生産量は、世界全体で年間約120万tと推定される。",
        "[2]: Different from the embedding model, reranker uses question and document as input and directly output similarity instead of embedding. To balance the accuracy and time cost, cross-encoder is widely used to re-rank top-k documents retrieved by other simple models. For example, use bge embedding model to retrieve top 100 relevant documents, and then use bge reranker to re-rank the top 100 documents to get the final top-3 results.    ",
        "오스트레일리아청개구리(Australian green tree frog)는 오스트레일리아와 뉴기니 원산의 청개구리과에 속한 청개구리의 일종이다. 미국과 뉴질랜드에도 외래종으로 흘러들어갔는데, 뉴질랜드에서는 멸종된 것으로 여겨진다. 학명 명명자 존 화이트의 이름을 따 화이트청개구리(White's tree frog), 특유의 생김새에서 유래한 시무룩청개구리(dumpy tree frog) 등의 별명이 있으며, 학명은 리토리아 카에룰레아(Litoria caerulea)이다. 형태학적으로 오스트레일리아청개구리속의 다른 청개구리, 특히 예쁜청개구리와 왕청개구리와 많이 닮았다. ",
        "Элой была придумана студией Guerrilla Games, которая хотела создать сильного и героического женского персонажа в рамках своей совершенно новой игры. Лицо героини было создано на основе внешности нидерландской актрисы Ханны Хукстры; роль персонажа при озвучивании на английском языке и в сценах захвата движения исполняет американская актриса Эшли Бёрч. ",
        "網上瘋傳一張照片，指在港鐵的機場快綫列車有床蝨蹤影。. 通訊事務管理局公布，香港寬頻 (01310.HK)於1至4月期間發生三宗涉及固定和流動電訊服務用戶的錯誤收帳事件。. 三宗事件共影響超過1萬名客戶",
        "하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]" "def normalize(text, maxlen=0, isolate_digits=False):     text = unicodedata.normalize('NFC', text)     if maxlen > 0:         if isolate_digits:             regex = '\d|[^\n\d]{,%d}\n{1,100}|[^\n\d]{1,%d}' % (maxlen, maxlen)         else:             regex = '.{,%d}\n{1,100}|.{1,%d}' % (maxlen, maxlen)     else:         if isolate_digits:             regex = '\d|[^\n\d]*\n+|[^\n\d]+'         else:             regex = '.*\n+|.+'     return [t.encode() for t in re.findall(regex, text)]",
        "ꃛꏢꄧꍏꇩꇭꍣꄈ꒜ꀉꒉꊰꏁꃢꌠꇩꏤꑭꊂꁧꎁ꒜ꈿꅉꇬꄉꅇꄜꌠ",
        'thead> <tbody> <tr> <td align="left"><a href="https://comparable.limsi.fr/bucc2018/bucc2018-task.html" rel="nofollow">BUCC</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/bucc-bitext-mining" rel="nofollow">mteb/bucc-bitext-mining</a></td> <td align="left">BUCC bitext mining dataset</td> <td align="left">BitextMining</td> <td align="left">s2s</td> <td align="right">4</td> <td align="right">0</td> <td align="right">0</td> <td align="right">641684</td> <td align="right">0</td> <td align="right">0</td> <td align="right">101.3</td> </tr> <tr> <td align="left"><a href="https://github.com/facebookresearch/LASER/tree/main/data/tatoeba/v1">Tatoeba</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/tatoeba-bitext-mining" rel="nofollow">mteb/tatoeba-bitext-mining</a></td> <td align="left">1,000 English-aligned sentence pairs for each language based on the Tatoeba corpus</td> <td align="left">BitextMining</td> <td align="left">s2s</td> <td align="right">112</td> <td align="right">0</td> <td align="right">0</td> <td align="right">2000</td> <td align="right">0</td> <td align="right">0</td> <td align="right">39.4</td> </tr> <tr> <td align="left"><a href="https://aclanthology.org/W19-6138/" rel="nofollow">Bornholm parallel</a></td> <td align="left"><a href="https://huggingface.co/datasets/strombergnlp/bornholmsk_parallel" rel="nofollow">strombergnlp/bornholmsk_parallel</a></td> <td align="left">Danish Bornholmsk Parallel Corpus.</td> <td align="left">BitextMining</td> <td align="left">s2s</td> <td align="right">2</td> <td align="right">100</td> <td align="right">100</td> <td align="right">100</td> <td align="right">64.6</td> <td align="right">86.2</td> <td align="right">89.7</td> </tr> <tr> <td align="left"><a href="https://arxiv.org/abs/2104.06893" rel="nofollow">AmazonCounterfactualClassification</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/amazon_counterfactual" rel="nofollow">mteb/amazon_counterfactual</a></td> <td align="left">A collection of Amazon customer reviews annotated for counterfactual detection pair classification.</td> <td align="left">Classification</td> <td align="left">s2s</td> <td align="right">4</td> <td align="right">4018</td> <td align="right">335</td> <td align="right">670</td> <td align="right">107.3</td> <td align="right">109.2</td> <td align="right">106.1</td> </tr> <tr> <td align="left"><a href="https://dl.acm.org/doi/10.1145/2507157.2507163" rel="nofollow">AmazonPolarityClassification</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/amazon_polarity" rel="nofollow">mteb/amazon_polarity</a></td> <td align="left">Amazon Polarity Classification Dataset.</td> <td align="left">Classification</td> <td align="left">s2s</td> <td align="right">1</td> <td align="right">3600000</td> <td align="right">0</td> <td align="right">400000</td> <td align="right">431.6</td> <td align="right">0</td> <td align="right">431.4</td> </tr> <tr> <td align="left"><a href="https://arxiv.org/abs/2010.02573" rel="nofollow">AmazonReviewsClassification</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/amazon_reviews_multi" rel="nofollow">mteb/amazon_reviews_multi</a></td> <td align="left">A collection of Amazon reviews specifically designed to aid research in multilingual text classification.</td> <td align="left">Classification</td> <td align="left">s2s</td> <td align="right">6</td> <td align="right">1200000</td> <td align="right">30000</td> <td align="right">30000</td> <td align="right">160.5</td> <td align="right">159.2</td> <td align="right">160.4</td> </tr> <tr> <td align="left"><a href="https://arxiv.org/abs/2003.04807" rel="nofollow">Banking77Classification</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/banking77" rel="nofollow">mteb/banking77</a></td> <td align="left">Dataset composed of online banking queries annotated with their corresponding intents.</td> <td align="left">Classification</td> <td align="left">s2s</td> <td align="right">1</td> <td align="right">10003</td> <td align="right">0</td> <td align="right">3080</td> <td align="right">59.5</td> <td align="right">0</td> <td align="right">54.2</td> </tr> <tr> <td align="left"><a href="https://www.aclweb.org/anthology/D18-1404" rel="nofollow">EmotionClassification</a></td> <td align="left"><a href="https://huggingface.co/datasets/mteb/emotion" rel="nofollow">mteb/emotion</a></td> <td align="left">Emotion is a dataset of English Twitter messages with six basic emotions: anger, fear, joy, love, sadness, and surprise. For more detailed information please refer to the paper.</td> <td align="left">Classification</td> <td align="left">s2s</td> <td align="right">1</td> <td align="right">16000</td> <td align="right">2000</td> <td align="right">2000</td> <td align="right">96.8</td> <td align="right">95.3</td> <td align="right">96.6</td> </tr> <tr>',
    ]
    demo(doc)


""" 

"""
