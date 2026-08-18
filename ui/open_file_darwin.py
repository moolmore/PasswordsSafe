# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_fileWnXTdB.ui'
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
        Form.resize(504, 340)
        Form.setMinimumSize(QSize(504, 340))
        Form.setMaximumSize(QSize(504, 340))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.PathInput = QLineEdit(Form)
        self.PathInput.setObjectName(u"PathInput")
        self.PathInput.setGeometry(QRect(79, 66, 304, 29))
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(18)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.PathInput.setFont(font1)
        self.PathInput.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"color: rgb(195, 195, 195);")
        self.PathInput.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-1, 132, 507, 33))
        self.label_2.setMinimumSize(QSize(177, 0))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(26)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(227, 227, 227);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.KeyInput = QLineEdit(Form)
        self.KeyInput.setObjectName(u"KeyInput")
        self.KeyInput.setGeometry(QRect(210, 180, 77, 23))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(18)
        self.KeyInput.setFont(font3)
        self.KeyInput.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.KeyInput.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"color: rgb(195, 195, 195);")
        self.KeyInput.setFrame(True)
        self.KeyInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.KeyInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ApplyButton = QPushButton(Form)
        self.ApplyButton.setObjectName(u"ApplyButton")
        self.ApplyButton.setGeometry(QRect(207, 286, 91, 35))
        font4 = QFont()
        font4.setFamilies([u"Google Sans"])
        font4.setPointSize(14)
        font4.setWeight(QFont.DemiBold)
        self.ApplyButton.setFont(font4)
        self.ApplyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ApplyButton.setStyleSheet(u"QPushButton {\n"
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
        self.ErrorsLable = QLabel(Form)
        self.ErrorsLable.setObjectName(u"ErrorsLable")
        self.ErrorsLable.setEnabled(True)
        self.ErrorsLable.setGeometry(QRect(0, 254, 504, 33))
        font5 = QFont()
        font5.setFamilies([u"Google Sans"])
        font5.setPointSize(12)
        font5.setWeight(QFont.Medium)
        self.ErrorsLable.setFont(font5)
        self.ErrorsLable.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ErrorsLable.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(227, 227, 227);")
        self.ErrorsLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 21, 506, 32))
        font6 = QFont()
        font6.setFamilies([u"Google Sans"])
        font6.setPointSize(26)
        font6.setBold(False)
        font6.setItalic(False)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: rgb(227, 227, 227);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ErrorsIcon = QLabel(Form)
        self.ErrorsIcon.setObjectName(u"ErrorsIcon")
        self.ErrorsIcon.setGeometry(QRect(0, 235, 504, 20))
        font7 = QFont()
        font7.setFamilies([u"Inter 24pt"])
        self.ErrorsIcon.setFont(font7)
        self.ErrorsIcon.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/newPrefix/error_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);")
        self.ErrorsIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.QuickDirButton = QPushButton(Form)
        self.QuickDirButton.setObjectName(u"QuickDirButton")
        self.QuickDirButton.setGeometry(QRect(388, 68, 38, 24))
        self.QuickDirButton.setStyleSheet(u"\n"
"QPushButton {\n"
"image: url(:/newPrefix/menu_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.ErrorsBack = QLabel(Form)
        self.ErrorsBack.setObjectName(u"ErrorsBack")
        self.ErrorsBack.setGeometry(QRect(102, 200, 300, 300))
        self.ErrorsBack.setStyleSheet(u"image: url(:/newPrefix/Rectangle 75red.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(73, 66, 356, 28))
        self.label_3.setStyleSheet(u"border-radius: 7px;\n"
"color: rgba(157, 221, 176, 219);\n"
"background-color: rgb(46, 46, 46);\n"
"border: 1px solid rgb(78, 78, 78);\n"
"\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(207, 178, 84, 28))
        self.label_4.setStyleSheet(u"border-radius: 7px;\n"
"color: rgba(157, 221, 176, 219);\n"
"background-color: rgb(46, 46, 46);\n"
"border: 1px solid rgb(78, 78, 78);\n"
"\n"
"")
        self.ErrorsBack.raise_()
        self.label_2.raise_()
        self.ApplyButton.raise_()
        self.ErrorsLable.raise_()
        self.label.raise_()
        self.ErrorsIcon.raise_()
        self.label_3.raise_()
        self.PathInput.raise_()
        self.QuickDirButton.raise_()
        self.label_4.raise_()
        self.KeyInput.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Open passwords file", None))
        self.PathInput.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Decryption key</p></body></html>", None))
        self.KeyInput.setText("")
        self.ApplyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.ErrorsLable.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Error</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ErrorsLable.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Error display</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Passwords file [.json]</p></body></html>", None))
        self.ErrorsIcon.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.QuickDirButton.setText("")
        self.ErrorsBack.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

