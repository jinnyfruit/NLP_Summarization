from typing import List
from konlpy.tag import Okt
from typing import List
from lexrankr import LexRank
import json

#한국어 추출요약 
class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.pos(text, norm=True, stem=True, join=True)
        return tokens

#JSON 읽어오기
file = open('get.json')
test = json.load(file)
print(test.get("eng_to_kor"))

# 1. init using Okt tokenizer 
mytokenizer: OktTokenizer = OktTokenizer()
lexrank: LexRank = LexRank(mytokenizer)
text = test.get("eng_to_kor")

# 2. summarize (like, pre-computation)
lexrank.summarize(text)

# 3. probe (like, query-time)
summaries: List[str] = lexrank.probe()
for summary in summaries:
    print(summary)