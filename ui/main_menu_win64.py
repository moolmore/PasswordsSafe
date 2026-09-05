# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu_update_2ExftUy.ui'
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
        MainWindow.resize(508, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(508, 608))
        MainWindow.setMaximumSize(QSize(508, 608))
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"border: none;\n"
"background-color: rgb(53, 53, 53);")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(508, 608))
        self.centralwidget.setStyleSheet(u"")
        self.CreateFile = QPushButton(self.centralwidget)
        self.CreateFile.setObjectName(u"CreateFile")
        self.CreateFile.setGeometry(QRect(85, 22, 32, 32))
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
        self.OpenFile.setGeometry(QRect(45, 22, 32, 32))
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
        self.AddPassButton.setGeometry(QRect(214, 22, 32, 32))
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
        self.DeletePassButton.setGeometry(QRect(255, 22, 32, 32))
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
        self.EditPassButton.setGeometry(QRect(296, 22, 32, 32))
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
        self.copy_name_a = QPushButton(self.centralwidget)
        self.copy_name_a.setObjectName(u"copy_name_a")
        self.copy_name_a.setEnabled(False)
        self.copy_name_a.setGeometry(QRect(337, 22, 32, 32))
        self.copy_name_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copy_name_a.setStyleSheet(u"QPushButton {\n"
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
        self.VisibilityPassButton.setGeometry(QRect(173, 22, 32, 32))
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
        self.label_4.setGeometry(QRect(34, 13, 94, 50))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        self.Search_Input = QLineEdit(self.centralwidget)
        self.Search_Input.setObjectName(u"Search_Input")
        self.Search_Input.setEnabled(False)
        self.Search_Input.setGeometry(QRect(64, 75, 380, 32))
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Search_Input.setFont(font1)
        self.Search_Input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.Search_Input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.lableListBackground = QLabel(self.centralwidget)
        self.lableListBackground.setObjectName(u"lableListBackground")
        self.lableListBackground.setGeometry(QRect(28, 133, 452, 447))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(17)
        font2.setWeight(QFont.Medium)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        font2.setHintingPreference(QFont.PreferNoHinting)
        self.lableListBackground.setFont(font2)
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
        self.PasswordList.setGeometry(QRect(28, 133, 452, 447))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.PasswordList.setFont(font3)
        self.PasswordList.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.CrossCursor))
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
"	margin-right: 4px;\n"
"    border-radius: 15px;        /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 "
                        "\u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 (\u0445\u043e\u0432\u0435\u0440) */\n"
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
"/* ################################## SCROLL BAR ################\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a"
                        "\u0438 \u0441\u0430\u043c\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438: \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u0438 \u0437\u0430\u0434\u0430\u0435\u043c \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"QListView QScrollBar:vertical {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 85, 194), stop:0.137931 rgba(69, 69, 69, 197));\n"
"    width: 7px;\n"
"    margin: 0px;\n"
"	\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0431\u0435\u0433\u0443\u043d\u043a\u0430: \u0437\u0430\u0434\u0430\u0435\u043c \u0446\u0432\u0435\u0442, \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0438 \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0438 */\n"
"QListView QScrollBar::handle:vertical {\n"
"    \n"
"	background: rgb(109, 109, 109); \n"
"    min-height: 20px;\n"
"    border-radius: 3px;   /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438"
                        "\u0435 (\u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u043e\u0442 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0433\u043e \u043e\u0432\u0430\u043b\u044c\u043d\u044b\u043c) */\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0426\u0432\u0435\u0442 \u0431\u0435\u0433\u0443\u043d\u043a\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"QListView QScrollBar::handle:vertical:hover {\n"
"    background: rgb(114, 136, 100); /* \u0426\u0432\u0435\u0442 \u0431\u0435\u0433\u0443\u043d\u043a\u0430 (\u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c) */\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0441\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u0441\u0442\u0440\u0435\u043b\u043e\u0447\u043a\u0438 \u0441\u0432\u0435\u0440\u0445\u0443 \u0438 \u0441\u043d\u0438\u0437\u0443 */\n"
"QListView QScrollBar::add-line:vertical, \n"
"QListView QScrollBar::sub-line:vertical {\n"
"  "
                        "  background: none;\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0444\u043e\u043d\u0430 */\n"
"QListView QScrollBar::add-page:vertical, \n"
"QListView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.PasswordList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.PasswordList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.lableVersion = QLabel(self.centralwidget)
        self.lableVersion.setObjectName(u"lableVersion")
        self.lableVersion.setGeometry(QRect(25, 580, 452, 21))
        font4 = QFont()
        font4.setFamilies([u"Google Sans"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.lableVersion.setFont(font4)
        self.lableVersion.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.lableVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 13, 324, 50))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(64, 100, 380, 41))
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SearchButton = QPushButton(self.centralwidget)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(True)
        self.SearchButton.setGeometry(QRect(407, 78, 26, 26))
        self.SearchButton.setStyleSheet(u"image: url(:/newPrefix/search_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.copy_email_a = QPushButton(self.centralwidget)
        self.copy_email_a.setObjectName(u"copy_email_a")
        self.copy_email_a.setEnabled(False)
        self.copy_email_a.setGeometry(QRect(378, 22, 32, 32))
        self.copy_email_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copy_email_a.setStyleSheet(u"QPushButton {\n"
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
        self.copy_pass_a = QPushButton(self.centralwidget)
        self.copy_pass_a.setObjectName(u"copy_pass_a")
        self.copy_pass_a.setEnabled(False)
        self.copy_pass_a.setGeometry(QRect(419, 22, 32, 32))
        self.copy_pass_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copy_pass_a.setStyleSheet(u"QPushButton {\n"
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
        self.copy_name_b = QPushButton(self.centralwidget)
        self.copy_name_b.setObjectName(u"copy_name_b")
        self.copy_name_b.setGeometry(QRect(356, 41, 18, 18))
        self.copy_name_b.setStyleSheet(u"image: url(:/newPrefix/label_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));")
        self.copy_email_b = QPushButton(self.centralwidget)
        self.copy_email_b.setObjectName(u"copy_email_b")
        self.copy_email_b.setGeometry(QRect(397, 41, 18, 18))
        self.copy_email_b.setStyleSheet(u"image: url(:/newPrefix/mail.png);\n"
"border-radius: 2px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));\n"
"border: 1px solid rgb(110, 110, 110);")
        self.copy_pass_b = QPushButton(self.centralwidget)
        self.copy_pass_b.setObjectName(u"copy_pass_b")
        self.copy_pass_b.setGeometry(QRect(438, 41, 18, 18))
        self.copy_pass_b.setStyleSheet(u"image: url(:/newPrefix/password_2_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 2px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));\n"
"border: 1px solid rgb(110, 110, 110);")
        self.CopyNameButton = QPushButton(self.centralwidget)
        self.CopyNameButton.setObjectName(u"CopyNameButton")
        self.CopyNameButton.setEnabled(False)
        self.CopyNameButton.setGeometry(QRect(337, 22, 35, 35))
        self.CopyNameButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.CopyEmailButton = QPushButton(self.centralwidget)
        self.CopyEmailButton.setObjectName(u"CopyEmailButton")
        self.CopyEmailButton.setEnabled(False)
        self.CopyEmailButton.setGeometry(QRect(378, 22, 35, 35))
        self.CopyEmailButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
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
        self.CopyPassButton.setGeometry(QRect(419, 22, 35, 35))
        self.CopyPassButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.test1 = QPushButton(self.centralwidget)
        self.test1.setObjectName(u"test1")
        self.test1.setEnabled(True)
        self.test1.setGeometry(QRect(401, 174, 30, 18))
        self.test1.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
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
        self.test2 = QPushButton(self.centralwidget)
        self.test2.setObjectName(u"test2")
        self.test2.setGeometry(QRect(401, 201, 30, 18))
        self.test2.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
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
        self.test3 = QPushButton(self.centralwidget)
        self.test3.setObjectName(u"test3")
        self.test3.setGeometry(QRect(401, 228, 30, 18))
        self.test3.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
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
        self.test4 = QPushButton(self.centralwidget)
        self.test4.setObjectName(u"test4")
        self.test4.setGeometry(QRect(401, 255, 30, 18))
        self.test4.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label_4.raise_()
        self.lableListBackground.raise_()
        self.CreateFile.raise_()
        self.OpenFile.raise_()
        self.AddPassButton.raise_()
        self.DeletePassButton.raise_()
        self.EditPassButton.raise_()
        self.copy_name_a.raise_()
        self.VisibilityPassButton.raise_()
        self.Search_Input.raise_()
        self.PasswordList.raise_()
        self.lableVersion.raise_()
        self.label.raise_()
        self.SearchButton.raise_()
        self.copy_email_a.raise_()
        self.copy_pass_a.raise_()
        self.copy_name_b.raise_()
        self.copy_email_b.raise_()
        self.copy_pass_b.raise_()
        self.CopyNameButton.raise_()
        self.CopyEmailButton.raise_()
        self.CopyPassButton.raise_()
        self.test1.raise_()
        self.test2.raise_()
        self.test3.raise_()
        self.test4.raise_()

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
        self.copy_name_a.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>copy password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.copy_name_a.setText("")
#if QT_CONFIG(tooltip)
        self.VisibilityPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>change password visible</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.VisibilityPassButton.setText("")
        self.label_4.setText("")
        self.Search_Input.setText("")
        self.lableListBackground.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#a1c292;\">Welcome to Passwords safe</span></p><p align=\"center\"><span style=\" color:#b5b5b5;\">This is a cryptographic manager of passwords<br/><br/></span><span style=\" text-decoration: underline; color:#b5b5b5;\">Open</span><span style=\" color:#b5b5b5;\"> a file or </span><span style=\" text-decoration: underline; color:#b5b5b5;\">create new</span><span style=\" color:#b5b5b5;\"> passwords list</span></p></body></html>", None))
        self.lableVersion.setText(QCoreApplication.translate("MainWindow", u"OS / APP VERSION", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search name / email", None))
        self.SearchButton.setText("")
#if QT_CONFIG(tooltip)
        self.copy_email_a.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>copy password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.copy_email_a.setText("")
#if QT_CONFIG(tooltip)
        self.copy_pass_a.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>copy password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.copy_pass_a.setText("")
        self.copy_name_b.setText("")
        self.copy_email_b.setText("")
        self.copy_pass_b.setText("")
        self.CopyNameButton.setText("")
        self.CopyEmailButton.setText("")
        self.CopyPassButton.setText("")
        self.test1.setText(QCoreApplication.translate("MainWindow", u"test 1", None))
        self.test2.setText(QCoreApplication.translate("MainWindow", u"test 2", None))
        self.test3.setText(QCoreApplication.translate("MainWindow", u"test 3", None))
        self.test4.setText(QCoreApplication.translate("MainWindow", u"test 4", None))
    # retranslateUi

