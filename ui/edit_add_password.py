# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_password_v2rTHOiJ.ui'
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
        Form.resize(340, 528)
        Form.setMinimumSize(QSize(340, 528))
        Form.setMaximumSize(QSize(340, 528))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.newNameEdit = QLineEdit(Form)
        self.newNameEdit.setObjectName(u"newNameEdit")
        self.newNameEdit.setGeometry(QRect(51, 50, 238, 34))
        font = QFont()
        font.setFamilies([u"Google Sans"])
        font.setPointSize(11)
        font.setBold(True)
        self.newNameEdit.setFont(font)
        self.newNameEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(88, 88, 88, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"color: rgba(157, 221, 176, 219);\n"
"border-radius: 8px;")
        self.newNameEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newNameEdit.setDragEnabled(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(51, 18, 238, 31))
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(14)
        font1.setWeight(QFont.Medium)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(138, 138, 138);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newNicknameEdit = QLineEdit(Form)
        self.newNicknameEdit.setObjectName(u"newNicknameEdit")
        self.newNicknameEdit.setGeometry(QRect(51, 131, 238, 34))
        self.newNicknameEdit.setFont(font)
        self.newNicknameEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(88, 88, 88, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"color: rgba(157, 221, 176, 219);\n"
"border-radius: 8px;")
        self.newNicknameEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newNicknameEdit.setDragEnabled(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(51, 100, 238, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(138, 138, 138);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newMailEdit = QLineEdit(Form)
        self.newMailEdit.setObjectName(u"newMailEdit")
        self.newMailEdit.setGeometry(QRect(51, 212, 238, 34))
        self.newMailEdit.setFont(font)
        self.newMailEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(88, 88, 88, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"color: rgba(157, 221, 176, 219);\n"
"border-radius: 8px;")
        self.newMailEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newMailEdit.setDragEnabled(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(51, 180, 238, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(138, 138, 138);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newPassEdit = QLineEdit(Form)
        self.newPassEdit.setObjectName(u"newPassEdit")
        self.newPassEdit.setGeometry(QRect(51, 293, 238, 34))
        self.newPassEdit.setFont(font)
        self.newPassEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(88, 88, 88, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"color: rgba(157, 221, 176, 219);\n"
"border-radius: 8px;")
        self.newPassEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newPassEdit.setDragEnabled(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(51, 260, 238, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(138, 138, 138);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newDescEdit = QLineEdit(Form)
        self.newDescEdit.setObjectName(u"newDescEdit")
        self.newDescEdit.setGeometry(QRect(51, 374, 238, 34))
        self.newDescEdit.setFont(font)
        self.newDescEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(88, 88, 88, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"color: rgba(157, 221, 176, 219);\n"
"border-radius: 8px;")
        self.newDescEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newDescEdit.setDragEnabled(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(51, 340, 238, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(138, 138, 138);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ApplyButton = QPushButton(Form)
        self.ApplyButton.setObjectName(u"ApplyButton")
        self.ApplyButton.setGeometry(QRect(60, 470, 100, 35))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.ApplyButton.setFont(font2)
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
        self.ErrorsLable.setGeometry(QRect(0, 430, 340, 33))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(11)
        font3.setWeight(QFont.Medium)
        self.ErrorsLable.setFont(font3)
        self.ErrorsLable.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ErrorsLable.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(227, 227, 227);")
        self.ErrorsLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CancelButton = QPushButton(Form)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(180, 470, 100, 35))
        self.CancelButton.setFont(font2)
        self.CancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CancelButton.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"WINDOW NAME HAS NOT EDITED", None))
        self.newNameEdit.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Service name", None))
        self.newNicknameEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Username", None))
        self.newMailEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.newPassEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.newDescEdit.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Misc", None))
        self.ApplyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.ErrorsLable.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Error</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ErrorsLable.setText(QCoreApplication.translate("Form", u"TEXT LABLE NOT EDITED", None))
        self.CancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

