# Form implementation generated from reading ui file 'MainActivity.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# python -m PyQt6.uic.pyuic -o output.py -x MainActivity.ui
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 730)
        Dialog.setMinimumSize(1280,730)
        Dialog.setMaximumSize(1280,730)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 730))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 730))
        self.label.setStyleSheet("border-image: url(Gui/images/background.png)\n")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ImageViewer = QtWidgets.QScrollArea(parent=self.widget)
        self.ImageViewer.setGeometry(QtCore.QRect(0, 220, 390, 219))
        self.ImageViewer.setWidgetResizable(True)
        self.ImageViewer.setObjectName("ImageViewer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 388, 217))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 20, 104, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.ImageViewer.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(1200, 0, 80, 730))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Notice = QtWidgets.QScrollArea(parent=self.widget)
        self.Notice.setGeometry(QtCore.QRect(400, 170, 451, 271))
        self.Notice.setWidgetResizable(True)
        self.Notice.setObjectName("Notice")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 449, 269))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_2)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 104, 71))
        self.textEdit.setObjectName("textEdit")
        self.Notice.setWidget(self.scrollAreaWidgetContents_2)
        self.Schedule_LIst = QtWidgets.QScrollArea(parent=self.widget)
        self.Schedule_LIst.setGeometry(QtCore.QRect(400, 440, 451, 271))
        self.Schedule_LIst.setWidgetResizable(True)
        self.Schedule_LIst.setObjectName("Schedule_LIst")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 449, 269))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 20, 104, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.Schedule_LIst.setWidget(self.scrollAreaWidgetContents_3)
        self.icon_home = QtWidgets.QScrollArea(parent=self.widget)
        self.icon_home.setGeometry(QtCore.QRect(1220, 60, 40, 40))
        self.icon_home.setWidgetResizable(True)
        self.icon_home.setObjectName("icon_home")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 38, 38))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.pushButton_home = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_4)
        self.pushButton_home.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.pushButton_home.setObjectName("pushButton_home")
        self.icon_home.setWidget(self.scrollAreaWidgetContents_4)
        self.icon_calender_schedule = QtWidgets.QScrollArea(parent=self.widget)
        self.icon_calender_schedule.setGeometry(QtCore.QRect(1220, 160, 40, 40))
        self.icon_calender_schedule.setWidgetResizable(True)
        self.icon_calender_schedule.setObjectName("icon_calender_schedule")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 38, 38))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.icon_calender_schedule.setWidget(self.scrollAreaWidgetContents_5)
        self.icon_apguide = QtWidgets.QScrollArea(parent=self.widget)
        self.icon_apguide.setGeometry(QtCore.QRect(1220, 260, 40, 40))
        self.icon_apguide.setWidgetResizable(True)
        self.icon_apguide.setObjectName("icon_apguide")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 38, 38))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.pushButton_AP = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_6)
        self.pushButton_AP.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.pushButton_AP.setObjectName("pushButton_CalGrowth")
        self.icon_apguide.setWidget(self.scrollAreaWidgetContents_6)
        self.icon_calculater = QtWidgets.QScrollArea(parent=self.widget)
        self.icon_calculater.setGeometry(QtCore.QRect(1220, 360, 40, 40))
        self.icon_calculater.setWidgetResizable(True)
        self.icon_calculater.setObjectName("icon_calculater")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 38, 38))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.icon_calculater.setWidget(self.scrollAreaWidgetContents_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Blue Scheduler")
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">이미지뷰</p></body></html>"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">주요소식</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">공지사항</p></body></html>"))
        self.pushButton_home.setText(_translate("Dialog", "PushButton"))
        self.pushButton_AP.setText(_translate("Dialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
