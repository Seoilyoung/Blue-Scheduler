# Main 코드
# gui코드가 와야 하나?

# 기능
# - AP 존버 가이드
# 	탬플릿 만들고 함수 쓰면 될듯. 서버 연동도 필요없음. 이미지로 저장, 공유 깔끔하게 되면 좋을듯. 
# - 일정(이벤트, 총력전 등)
# 	이건 수동으로 해야 하는거 아닌가? 달력형식, 목록형식으로 구현.
# - 트위터 / 넥슨 홈페이지 새 글 갱신
# 	크롤링
# - 재화 계산(총 재화, 2~3달 내 재화 등 구분 프리셋)
# 	스프레드시트 이미 구현한 것 이용
# - 인게임 연동도 가능한가?(AP, 카페, 숙제, 순위 확인)
# 	api 알아내려면 클뜯을 하면 나오나?
# - 원스 출석 알리미 / 알림이 아니라 출석을 해주거나 출석을 안했을 때 푸시알림
#   이것도 12시에 알리미는 프로그램 알림 기능을 사용하면 가능하겠지만 출석을 하지 않았을 때를 파악하려면 어떻게 해야 하나?
# - 총력전 / 이벤트 조력자 매크로
# 	다른 방식으로 이미 구현한 것 이용
# - GUI
#   깔끔하게 원신 구동기 화면
#   종류가 많음. 메모리 먹는거 확인하면서 선택.
# - 트위치 스트리머 확인
#   특정 스트리머 방송 켰는지 확인

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from Gui_Main.MainActivity import Ui_MainWindow
from Gui_CalGrowth.CalGrowthActivity import Ui_CalGrowthWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def CalGrowth(self):
        print("여기")
        self.hide()
        self.calgrowth = CalGrowthWindow()
        self.calgrowth.app.exec()
        self.show()

class CalGrowthWindow(QMainWindow, Ui_CalGrowthWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(CalGrowthWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

            
    def btn_home(self):
        self.hide()
        self.home = MainWindow()
        self.home.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())