# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_passwordiHfblx.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from .assets import images

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(407, 182)
        Form.setMinimumSize(QSize(407, 182))
        Form.setMaximumSize(QSize(407, 182))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(52, 52, 52);")
        self.newNameEdit = QLineEdit(Form)
        self.newNameEdit.setObjectName(u"newNameEdit")
        self.newNameEdit.setGeometry(QRect(27, 66, 143, 31))
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(15)
        self.newNameEdit.setFont(font1)
        self.newNameEdit.setStyleSheet(u"border-radius: 10px;\n"
"color: rgba(157, 221, 176, 219);\n"
"background-color: rgba(45, 45, 45, 128);\n"
"border: 1px solid rgb(162, 162, 162);\n"
"")
        self.newNameEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(291, 28, 32, 31))
        self.label_11.setStyleSheet(u"image: url(:/newPrefix/password_2_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 11, 408, 21))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(222, 222, 222);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newPassEdit = QLineEdit(Form)
        self.newPassEdit.setObjectName(u"newPassEdit")
        self.newPassEdit.setGeometry(QRect(235, 66, 143, 31))
        self.newPassEdit.setFont(font1)
        self.newPassEdit.setStyleSheet(u"border-radius: 10px;\n"
"color: rgba(157, 221, 176, 219);\n"
"background-color: rgba(45, 45, 45, 128);\n"
"border: 1px solid rgb(162, 162, 162);\n"
"")
        self.newPassEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.applyButton = QPushButton(Form)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(154, 130, 99, 37))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(12)
        font3.setWeight(QFont.Medium)
        self.applyButton.setFont(font3)
        self.applyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.applyButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"	color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(78, 109, 88);\n"
"}")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(83, 28, 32, 31))
        self.label_10.setStyleSheet(u"image: url(:/newPrefix/label_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-65, -10, 515, 515))
        self.label_3.setStyleSheet(u"image: url(:/newPrefix/Rectangle 75.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ErrorsLable_2 = QLabel(Form)
        self.ErrorsLable_2.setObjectName(u"ErrorsLable_2")
        self.ErrorsLable_2.setEnabled(True)
        self.ErrorsLable_2.setGeometry(QRect(0, 93, 408, 41))
        font4 = QFont()
        font4.setFamilies([u"Google Sans"])
        font4.setPointSize(11)
        font4.setWeight(QFont.Medium)
        self.ErrorsLable_2.setFont(font4)
        self.ErrorsLable_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ErrorsLable_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(227, 227, 227);")
        self.ErrorsLable_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_10.raise_()
        self.newPassEdit.raise_()
        self.newNameEdit.raise_()
        self.applyButton.raise_()
        self.label_11.raise_()
        self.ErrorsLable_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Add password", None))
        self.newNameEdit.setText("")
        self.label_11.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"New password", None))
        self.newPassEdit.setText("")
        self.applyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_10.setText("")
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.ErrorsLable_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Error</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ErrorsLable_2.setText(QCoreApplication.translate("Form", u"Error display", None))
    # retranslateUi

