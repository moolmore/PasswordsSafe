# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menusUGBEc.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QWidget)
from .assets import images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(381, 574)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(381, 574))
        MainWindow.setMaximumSize(QSize(381, 574))
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"border: none;")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(381, 574))
        self.centralwidget.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.CreateFile = QPushButton(self.centralwidget)
        self.CreateFile.setObjectName(u"CreateFile")
        self.CreateFile.setGeometry(QRect(80, 20, 32, 32))
        self.CreateFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CreateFile.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/note_add_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.OpenFile = QPushButton(self.centralwidget)
        self.OpenFile.setObjectName(u"OpenFile")
        self.OpenFile.setGeometry(QRect(40, 20, 32, 32))
        self.OpenFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.OpenFile.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/file_open_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.OpenFile.setAutoRepeat(False)
        self.AddPassButton = QPushButton(self.centralwidget)
        self.AddPassButton.setObjectName(u"AddPassButton")
        self.AddPassButton.setEnabled(False)
        self.AddPassButton.setGeometry(QRect(190, 20, 32, 32))
        self.AddPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AddPassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.DeletePassButton = QPushButton(self.centralwidget)
        self.DeletePassButton.setObjectName(u"DeletePassButton")
        self.DeletePassButton.setEnabled(False)
        self.DeletePassButton.setGeometry(QRect(230, 20, 32, 32))
        self.DeletePassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DeletePassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/delete_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.EditPassButton = QPushButton(self.centralwidget)
        self.EditPassButton.setObjectName(u"EditPassButton")
        self.EditPassButton.setEnabled(False)
        self.EditPassButton.setGeometry(QRect(270, 20, 32, 32))
        self.EditPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.EditPassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/edit_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.CopyPassButton = QPushButton(self.centralwidget)
        self.CopyPassButton.setObjectName(u"CopyPassButton")
        self.CopyPassButton.setEnabled(False)
        self.CopyPassButton.setGeometry(QRect(310, 20, 32, 32))
        self.CopyPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CopyPassButton.setStyleSheet(u"QPushButton {\n"
"image: url(:/newPrefix/content_copy_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.VisibilityPassButton = QPushButton(self.centralwidget)
        self.VisibilityPassButton.setObjectName(u"VisibilityPassButton")
        self.VisibilityPassButton.setEnabled(False)
        self.VisibilityPassButton.setGeometry(QRect(150, 20, 32, 32))
        self.VisibilityPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.VisibilityPassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/visibility_off_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.VisibilityPassButton.setIconSize(QSize(16, 16))
        self.label_4 = QPushButton(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 10, 91, 51))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        self.SearchButton = QPushButton(self.centralwidget)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(True)
        self.SearchButton.setGeometry(QRect(301, 70, 51, 32))
        self.SearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SearchButton.setStyleSheet(u"QPushButton {\n"
"image: url(:/newPrefix/search_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border: 1px solid rgb(110, 110, 110);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(78, 109, 88);\n"
"}")
        self.SearchButton.setIconSize(QSize(16, 16))
        self.SearchButton.setCheckable(False)
        self.SearchButton.setAutoRepeat(False)
        self.Search_Input = QLineEdit(self.centralwidget)
        self.Search_Input.setObjectName(u"Search_Input")
        self.Search_Input.setEnabled(False)
        self.Search_Input.setGeometry(QRect(30, 70, 261, 32))
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Search_Input.setFont(font1)
        self.Search_Input.setStyleSheet(u"QLineEdit {\n"
"border-radius: 16px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"color: rgba(157, 221, 176, 219);\n"
"border: 1px solid rgb(110, 110, 110);\n"
"}\n"
"\n"
"")
        self.Search_Input.setFrame(True)
        self.Search_Input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.Search_Input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Search_Input.setDragEnabled(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 102, 261, 21))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lableListBackground = QLabel(self.centralwidget)
        self.lableListBackground.setObjectName(u"lableListBackground")
        self.lableListBackground.setGeometry(QRect(25, 127, 329, 418))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(17)
        font3.setWeight(QFont.Medium)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        font3.setHintingPreference(QFont.PreferNoHinting)
        self.lableListBackground.setFont(font3)
        self.lableListBackground.setAutoFillBackground(False)
        self.lableListBackground.setStyleSheet(u"border-radius: 15px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.56, y2:1, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(125, 177, 136, 255));\n"
"letter-spacing: 1px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 85, 194), stop:0.137931 rgba(69, 69, 69, 197));\n"
"selection-background-color: rgba(119, 165, 133, 184);\n"
"")
        self.lableListBackground.setScaledContents(False)
        self.lableListBackground.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lableListBackground.setWordWrap(True)
        self.PasswordList = QListWidget(self.centralwidget)
        self.PasswordList.setObjectName(u"PasswordList")
        self.PasswordList.setGeometry(QRect(25, 127, 329, 418))
        font4 = QFont()
        font4.setFamilies([u"Google Sans"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.PasswordList.setFont(font4)
        self.PasswordList.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.PasswordList.setStyleSheet(u"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0441\u0430\u043c\u043e\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 (\u0444\u043e\u043d\u0430) */\n"
"QListWidget {\n"
"     /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    padding: 5px;              /* \u041e\u0442\u0441\u0442\u0443\u043f \u043e\u0442 \u043a\u0440\u0430\u0435\u0432 \u0434\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"    color: #ffffff;            /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e */\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0432\u0441\u0435\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043f\u0438\u0441\u043a\u0430 \u0432 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0438 */\n"
"QListWidget::item {\n"
"   "
                        " \n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.002, y1:0, x2:0, y2:1, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(85, 85, 85, 255));\n"
"                /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"	color: rgb(225, 225, 225);\n"
"    padding: 8px 12px;         /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b (\u0432\u044b\u0441\u043e\u0442\u0430 \u0438 \u0448\u0438\u0440\u0438\u043d\u0430) */\n"
"    margin-bottom: 4px;        /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c\u0438 */\n"
"    border-radius: 15px;        /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u044d\u043b\u0435\u043c"
                        "\u0435\u043d\u0442\u043e\u0432 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 (\u0445\u043e\u0432\u0435\u0440) */\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(98, 98, 98);\n"
"	border: 1px solid rgb(110, 110, 110);\n"
"\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"QListWidget::item:selected {\n"
"    /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 93, 93, 255), stop:1 rgba(106, 137, 115, 255));\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.PasswordList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PasswordList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.lableVersion = QLabel(self.centralwidget)
        self.lableVersion.setObjectName(u"lableVersion")
        self.lableVersion.setGeometry(QRect(2, 547, 377, 22))
        self.lableVersion.setFont(font2)
        self.lableVersion.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.lableVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(373, 408, 454, 454))
        self.label_6.setStyleSheet(u"image: url(:/newPrefix/Rectangle 75.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 211, 51))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label_4.raise_()
        self.lableListBackground.raise_()
        self.CreateFile.raise_()
        self.OpenFile.raise_()
        self.AddPassButton.raise_()
        self.DeletePassButton.raise_()
        self.EditPassButton.raise_()
        self.CopyPassButton.raise_()
        self.VisibilityPassButton.raise_()
        self.Search_Input.raise_()
        self.label.raise_()
        self.PasswordList.raise_()
        self.lableVersion.raise_()
        self.label_6.raise_()
        self.SearchButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Passwords Safe", None))
        self.CreateFile.setText("")
        self.OpenFile.setText("")
#if QT_CONFIG(tooltip)
        self.AddPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>add</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.AddPassButton.setText("")
#if QT_CONFIG(tooltip)
        self.DeletePassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>remove password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DeletePassButton.setText("")
#if QT_CONFIG(tooltip)
        self.EditPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>edit password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.EditPassButton.setText("")
#if QT_CONFIG(tooltip)
        self.CopyPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>copy password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CopyPassButton.setText("")
#if QT_CONFIG(tooltip)
        self.VisibilityPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>change password visible</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.VisibilityPassButton.setText("")
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.SearchButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>change password visible</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SearchButton.setText("")
        self.Search_Input.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search password name", None))
        self.lableListBackground.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#a1c292;\">Welcome to Passwords safe</span></p><p align=\"center\"><span style=\" color:#b5b5b5;\">This is a cryptographic manager of passwords<br/><br/></span><span style=\" text-decoration: underline; color:#b5b5b5;\">Open</span><span style=\" color:#b5b5b5;\"> a file or </span><span style=\" text-decoration: underline; color:#b5b5b5;\">create new</span><span style=\" color:#b5b5b5;\"> passwords list</span></p></body></html>", None))
        self.lableVersion.setText(QCoreApplication.translate("MainWindow", u"OS / APP VERSION", None))
        self.label_6.setText("")
        self.label_2.setText("")
    # retranslateUi

