# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu_update_2hLhGjx.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)
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
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/newPrefix/app_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
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
        self.lableListBackground = QLabel(self.centralwidget)
        self.lableListBackground.setObjectName(u"lableListBackground")
        self.lableListBackground.setGeometry(QRect(28, 133, 452, 447))
        font = QFont()
        font.setFamilies([u"Google Sans"])
        font.setPointSize(17)
        font.setWeight(QFont.Medium)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        self.lableListBackground.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.PasswordList.setFont(font1)
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
        self.lableVersion.setGeometry(QRect(160, 580, 188, 28))
        font2 = QFont()
        font2.setFamilies([u"Google Sans"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.lableVersion.setFont(font2)
        self.lableVersion.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.lableVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.settings_frame = QFrame(self.centralwidget)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(131, 269, 246, 291))
        self.settings_frame.setMouseTracking(False)
        self.settings_frame.setAcceptDrops(False)
        self.settings_frame.setStyleSheet(u"border-radius: 15px;\n"
"")
        self.settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.close_setngs = QPushButton(self.settings_frame)
        self.close_setngs.setObjectName(u"close_setngs")
        self.close_setngs.setGeometry(QRect(210, 0, 24, 21))
        self.close_setngs.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"	image: url(:/newPrefix/cancel_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(118, 141, 103, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.import_csv = QPushButton(self.settings_frame)
        self.import_csv.setObjectName(u"import_csv")
        self.import_csv.setGeometry(QRect(20, 23, 206, 51))
        font3 = QFont()
        font3.setFamilies([u"Google Sans"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.import_csv.setFont(font3)
        self.import_csv.setStyleSheet(u"\n"
"QPushButton {\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"color: rgba(157, 221, 176, 219);\n"
"border: 1px solid rgb(110, 110, 110);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(128, 157, 123);\n"
"}")
        self.export_passes_1 = QPushButton(self.settings_frame)
        self.export_passes_1.setObjectName(u"export_passes_1")
        self.export_passes_1.setGeometry(QRect(20, 130, 206, 51))
        font4 = QFont()
        font4.setFamilies([u"Google Sans"])
        font4.setPointSize(12)
        font4.setWeight(QFont.ExtraBold)
        self.export_passes_1.setFont(font4)
        self.export_passes_1.setStyleSheet(u"\n"
"QPushButton {\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"color: rgba(157, 221, 176, 219);\n"
"border: 1px solid rgb(110, 110, 110);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(128, 157, 123);\n"
"}")
        self.label_7 = QLabel(self.settings_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(2, 80, 241, 21))
        font5 = QFont()
        font5.setFamilies([u"Google Sans"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.settings_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 100, 246, 31))
        font6 = QFont()
        font6.setFamilies([u"Google Sans"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.settings_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 180, 246, 31))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.export_passes_2 = QPushButton(self.settings_frame)
        self.export_passes_2.setObjectName(u"export_passes_2")
        self.export_passes_2.setGeometry(QRect(20, 210, 206, 51))
        self.export_passes_2.setFont(font4)
        self.export_passes_2.setStyleSheet(u"\n"
"QPushButton {\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"color: rgba(157, 221, 176, 219);\n"
"border: 1px solid rgb(110, 110, 110);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(128, 157, 123);\n"
"}")
        self.manage = QFrame(self.centralwidget)
        self.manage.setObjectName(u"manage")
        self.manage.setEnabled(True)
        self.manage.setGeometry(QRect(150, 13, 324, 50))
        self.manage.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.manage.setFrameShape(QFrame.Shape.StyledPanel)
        self.manage.setFrameShadow(QFrame.Shadow.Raised)
        self.mng_back = QLabel(self.manage)
        self.mng_back.setObjectName(u"mng_back")
        self.mng_back.setGeometry(QRect(0, 0, 324, 50))
        self.mng_back.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        self.VisibilityPassButton = QPushButton(self.manage)
        self.VisibilityPassButton.setObjectName(u"VisibilityPassButton")
        self.VisibilityPassButton.setEnabled(True)
        self.VisibilityPassButton.setGeometry(QRect(23, 9, 32, 32))
        self.VisibilityPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.VisibilityPassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/view_list_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.VisibilityPassButton.setIconSize(QSize(16, 16))
        self.AddPassButton = QPushButton(self.manage)
        self.AddPassButton.setObjectName(u"AddPassButton")
        self.AddPassButton.setEnabled(True)
        self.AddPassButton.setGeometry(QRect(64, 9, 32, 32))
        self.AddPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AddPassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.DeletePassButton = QPushButton(self.manage)
        self.DeletePassButton.setObjectName(u"DeletePassButton")
        self.DeletePassButton.setEnabled(True)
        self.DeletePassButton.setGeometry(QRect(105, 9, 32, 32))
        self.DeletePassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DeletePassButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/delete_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.EditPassButton = QPushButton(self.manage)
        self.EditPassButton.setObjectName(u"EditPassButton")
        self.EditPassButton.setEnabled(True)
        self.EditPassButton.setGeometry(QRect(146, 9, 32, 32))
        self.EditPassButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.EditPassButton.setStyleSheet(u"QPushButton {\n"
"image: url(:/newPrefix/edit_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.mng_1 = QLabel(self.manage)
        self.mng_1.setObjectName(u"mng_1")
        self.mng_1.setGeometry(QRect(269, 9, 32, 32))
        self.mng_1.setStyleSheet(u"image: url(:/newPrefix/content_copy_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.mng_2 = QLabel(self.manage)
        self.mng_2.setObjectName(u"mng_2")
        self.mng_2.setGeometry(QRect(187, 9, 32, 32))
        self.mng_2.setStyleSheet(u"image: url(:/newPrefix/content_copy_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.mng_20 = QLabel(self.manage)
        self.mng_20.setObjectName(u"mng_20")
        self.mng_20.setGeometry(QRect(247, 28, 18, 18))
        self.mng_20.setStyleSheet(u"image: url(:/newPrefix/mail.png);\n"
"border-radius: 2px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));\n"
"border: 1px solid rgb(110, 110, 110);")
        self.mng_10 = QLabel(self.manage)
        self.mng_10.setObjectName(u"mng_10")
        self.mng_10.setGeometry(QRect(288, 28, 18, 18))
        self.mng_10.setStyleSheet(u"image: url(:/newPrefix/password_2_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 2px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));\n"
"border: 1px solid rgb(110, 110, 110);")
        self.CopyNameButton = QPushButton(self.manage)
        self.CopyNameButton.setObjectName(u"CopyNameButton")
        self.CopyNameButton.setEnabled(True)
        self.CopyNameButton.setGeometry(QRect(187, 9, 35, 35))
        self.CopyNameButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.mng_30 = QLabel(self.manage)
        self.mng_30.setObjectName(u"mng_30")
        self.mng_30.setGeometry(QRect(206, 28, 18, 18))
        self.mng_30.setStyleSheet(u"image: url(:/newPrefix/label_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(67, 80, 59, 255), stop:1 rgba(95, 113, 83, 255));")
        self.mng_3 = QLabel(self.manage)
        self.mng_3.setObjectName(u"mng_3")
        self.mng_3.setGeometry(QRect(228, 9, 32, 32))
        self.mng_3.setStyleSheet(u"image: url(:/newPrefix/content_copy_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.CopyEmailButton = QPushButton(self.manage)
        self.CopyEmailButton.setObjectName(u"CopyEmailButton")
        self.CopyEmailButton.setEnabled(True)
        self.CopyEmailButton.setGeometry(QRect(228, 9, 35, 35))
        self.CopyEmailButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.CopyPassButton = QPushButton(self.manage)
        self.CopyPassButton.setObjectName(u"CopyPassButton")
        self.CopyPassButton.setEnabled(True)
        self.CopyPassButton.setGeometry(QRect(269, 9, 35, 35))
        self.CopyPassButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.mng_back.raise_()
        self.VisibilityPassButton.raise_()
        self.AddPassButton.raise_()
        self.DeletePassButton.raise_()
        self.EditPassButton.raise_()
        self.mng_1.raise_()
        self.mng_2.raise_()
        self.mng_10.raise_()
        self.CopyNameButton.raise_()
        self.mng_30.raise_()
        self.mng_3.raise_()
        self.CopyEmailButton.raise_()
        self.CopyPassButton.raise_()
        self.mng_20.raise_()
        self.parse = QFrame(self.centralwidget)
        self.parse.setObjectName(u"parse")
        self.parse.setGeometry(QRect(34, 13, 94, 50))
        self.parse.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.parse.setFrameShape(QFrame.Shape.StyledPanel)
        self.parse.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QPushButton(self.parse)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 94, 50))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"")
        self.OpenFile = QPushButton(self.parse)
        self.OpenFile.setObjectName(u"OpenFile")
        self.OpenFile.setGeometry(QRect(11, 9, 32, 32))
        self.OpenFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.OpenFile.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/file_open_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.OpenFile.setAutoRepeat(False)
        self.CreateFile = QPushButton(self.parse)
        self.CreateFile.setObjectName(u"CreateFile")
        self.CreateFile.setGeometry(QRect(51, 9, 32, 32))
        self.CreateFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CreateFile.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/note_add_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 16px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(125, 177, 136, 255), stop:1 rgba(98, 98, 98, 0));\n"
"}")
        self.search = QFrame(self.centralwidget)
        self.search.setObjectName(u"search")
        self.search.setEnabled(True)
        self.search.setGeometry(QRect(64, 75, 410, 66))
        self.search.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.search.setFrameShape(QFrame.Shape.StyledPanel)
        self.search.setFrameShadow(QFrame.Shadow.Raised)
        self.settings = QPushButton(self.search)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(384, 3, 26, 25))
        self.settings.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"image: url(:/newPrefix/menu_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(98, 98, 98, 255));\n"
"color: rgba(157, 221, 176, 219);\n"
"border: 1px solid rgb(110, 110, 110);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(152, 181, 133);\n"
"}")
        self.Search_Input = QLineEdit(self.search)
        self.Search_Input.setObjectName(u"Search_Input")
        self.Search_Input.setEnabled(True)
        self.Search_Input.setGeometry(QRect(0, 0, 380, 32))
        font7 = QFont()
        font7.setFamilies([u"Google Sans"])
        font7.setPointSize(18)
        font7.setBold(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.Search_Input.setFont(font7)
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
        self.label = QLabel(self.search)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 25, 380, 41))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.search)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(343, 3, 26, 26))
        self.label_2.setStyleSheet(u"image: url(:/newPrefix/search_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.saved = QFrame(self.centralwidget)
        self.saved.setObjectName(u"saved")
        self.saved.setGeometry(QRect(340, 510, 111, 51))
        self.saved.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.saved.setFrameShape(QFrame.Shape.StyledPanel)
        self.saved.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.saved)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 24, 24))
        self.label_3.setStyleSheet(u"image: url(:/newPrefix/save_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png);")
        self.label_5 = QLabel(self.saved)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 10, 61, 24))
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color: rgb(148, 201, 160);")
        self.label_6 = QLabel(self.saved)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 101, 41))
        self.label_6.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(110, 110, 110);\n"
"background-color: rgb(71, 71, 71);\n"
"")
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(28, 580, 132, 28))
        font8 = QFont()
        font8.setFamilies([u"Google Sans"])
        font8.setUnderline(True)
        self.label_10.setFont(font8)
        self.label_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setMargin(0)
        self.label_10.setIndent(20)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(348, 580, 132, 28))
        self.label_11.setFont(font8)
        self.label_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(99, 99, 99);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setIndent(20)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Passwords Safe", None))
        self.lableListBackground.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#a1c292;\">Welcome to Passwords safe</span></p><p align=\"center\"><span style=\" color:#b5b5b5;\">This is a cryptographic manager of passwords<br/><br/></span><span style=\" text-decoration: underline; color:#b5b5b5;\">Open</span><span style=\" color:#b5b5b5;\"> a file or </span><span style=\" text-decoration: underline; color:#b5b5b5;\">create new</span><span style=\" color:#b5b5b5;\"> passwords list</span></p></body></html>", None))
        self.lableVersion.setText(QCoreApplication.translate("MainWindow", u"OS / APP VERSION", None))
        self.close_setngs.setText("")
        self.import_csv.setText(QCoreApplication.translate("MainWindow", u"Import passwords .csv", None))
        self.export_passes_1.setText(QCoreApplication.translate("MainWindow", u"service / url / username / \n"
"password / misc", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Export passswords in .csv:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Google, Edge:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"moolmore Passwords Safe: ", None))
        self.export_passes_2.setText(QCoreApplication.translate("MainWindow", u"service / username /\n"
" email / password / misc", None))
        self.mng_back.setText("")
#if QT_CONFIG(tooltip)
        self.VisibilityPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Change visibility:</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#abc1af;\">Only service</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#abc1af;\">Service / Name /Misc</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#abc1af;\">Service / Email / Password</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#abc1af;\">All data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.VisibilityPassButton.setText("")
#if QT_CONFIG(tooltip)
        self.AddPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Add password data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.AddPassButton.setText("")
#if QT_CONFIG(tooltip)
        self.DeletePassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Delete password data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DeletePassButton.setText("")
#if QT_CONFIG(tooltip)
        self.EditPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Edit password data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.EditPassButton.setText("")
        self.mng_1.setText("")
        self.mng_2.setText("")
        self.mng_20.setText("")
        self.mng_10.setText("")
#if QT_CONFIG(tooltip)
        self.CopyNameButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Copy username</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CopyNameButton.setText("")
        self.mng_30.setText("")
        self.mng_3.setText("")
#if QT_CONFIG(tooltip)
        self.CopyEmailButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Copy email</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CopyEmailButton.setText("")
#if QT_CONFIG(tooltip)
        self.CopyPassButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Copy password</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CopyPassButton.setText("")
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.OpenFile.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Open passwords file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.OpenFile.setText("")
#if QT_CONFIG(tooltip)
        self.CreateFile.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">New passwords file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CreateFile.setText("")
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#82c17e;\">Open settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settings.setText("")
        self.Search_Input.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search name / email", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saved", None))
        self.label_6.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Author</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Repository</p></body></html>", None))
    # retranslateUi

