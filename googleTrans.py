import sys
import re

import googletrans
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

translator = googletrans.Translator()
form_class = uic.loadUiType("ui/trans.ui")[0]
# 디자인한 외부 ui 파일 불러와서 저장

class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__() # 부모 클래스 생성자 호출
        self.setupUi(self) # 불러온 ui 파일을 연결

        self.setWindowTitle("Four Languages Translator")
        self.setWindowIcon(QIcon("image/icon.png"))
        self.statusBar().showMessage("Translator version 1.0")

        self.trabtn.clicked.connect(self.trans_action)  # signal
        self.rebtn.clicked.connect(self.init_action)
        self.rvbtn.clicked.connect(self.init2_action)

# 정규 표현식을 이용하면, 한글을 안들어가게 할 수 있음
# 입력된 텍스트를 가지고 와서 버튼을 클릭하면 출력이 되도록 하는 것 
    def trans_action(self): # 번역 실행함수
        engText = self.engtext.text() # 여기에 입력된 영어텍스트 가져오기
        # 넣는 것 text, 빼는 건 subtext
        # if engText == "":
        #     print("공백테스트") # pass로는 해결이 안됨
        if engText == "": # 공백 문제 될 때
            QMessageBox.warning(self, "Warning", "Please enter text to translate.")
        elif not self.is_english_text(engText):
            QMessageBox.warning(self, "Warning", "Please enter only English text.")
        else:
            trans = googletrans.Translator()
            trans_de = trans.translate(engText, dest="de")
            trans_ja = trans.translate(engText, dest="ja")
            trans_ko = trans.translate(engText, dest="ko")

            self.detext.append(trans_de.text)
            self.jatext.append(trans_ja.text)
            self.kotext.append(trans_ko.text)

    def init_action(self):
        self.engtext.clear()  # 영어 입력 필드 초기화

    def init2_action(self):
        self.engtext.clear()  # 영어 입력 필드 초기화
        self.detext.clear()  # 독일어 번역 텍스트 출력 필드 초기화
        self.jatext.clear()  # 일본어 번역 텍스트 출력 필드 초기화
        self.kotext.clear()  # 한국어 번역 텍스트 출력 필드 초기화

    def is_english_text(self, text):
        pattern = r'^[a-zA-Z\s,.!?]*$'  # 영어, 공백, 특정 특수 문자만 허용
        return re.match(pattern, text) is not None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())