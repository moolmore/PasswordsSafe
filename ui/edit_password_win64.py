# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WIP_password_editAdpWWY.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(536, 181)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 36, 16))
        self.newNameEdit = QLineEdit(Form)
        self.newNameEdit.setObjectName(u"newNameEdit")
        self.newNameEdit.setGeometry(QRect(10, 40, 113, 22))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 20, 52, 16))
        self.newNicknameEdit = QLineEdit(Form)
        self.newNicknameEdit.setObjectName(u"newNicknameEdit")
        self.newNicknameEdit.setGeometry(QRect(140, 40, 113, 22))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 20, 29, 16))
        self.newMailEdit = QLineEdit(Form)
        self.newMailEdit.setObjectName(u"newMailEdit")
        self.newMailEdit.setGeometry(QRect(270, 40, 113, 22))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 20, 50, 16))
        self.newPassEdit = QLineEdit(Form)
        self.newPassEdit.setObjectName(u"newPassEdit")
        self.newPassEdit.setGeometry(QRect(410, 40, 113, 22))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 70, 54, 16))
        self.newDescEdit = QLineEdit(Form)
        self.newDescEdit.setObjectName(u"newDescEdit")
        self.newDescEdit.setGeometry(QRect(180, 90, 201, 22))
        self.applyButton = QPushButton(Form)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(230, 130, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Editing a password", None))
        self.label.setText(QCoreApplication.translate("Form", u"service", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"nickname", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"email", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"password", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"decription", None))
        self.applyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
    # retranslateUi

