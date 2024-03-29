import sys

import googletrans

trans = googletrans.Translator() # 구글 번역 객체 생성
trans2 = trans.translate("It's about time to go home. We have to go now.", dest="de")
trans3 = trans.translate("It's about time to go home. We have to go now.", dest="ja")
trans4 = trans.translate("It's about time to go home. We have to go now.", dest="ko")

print("-----------------------------------------------")
print(trans2.text)
print(trans3.text)
print(trans4.text)



# print(googletrans.LANGUAGES) - > destination에 삽입할 내용