# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(800, 500)
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.adb_backup = QWidget()
        self.adb_backup.setObjectName(u"adb_backup")
        self.verticalLayout = QVBoxLayout(self.adb_backup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.aab_btn_device = QPushButton(self.adb_backup)
        self.aab_btn_device.setObjectName(u"aab_btn_device")
        self.aab_btn_device.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_1.addWidget(self.aab_btn_device)

        self.aab_cmb_device = QComboBox(self.adb_backup)
        self.aab_cmb_device.setObjectName(u"aab_cmb_device")

        self.horizontalLayout_1.addWidget(self.aab_cmb_device)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.aab_btn_path = QPushButton(self.adb_backup)
        self.aab_btn_path.setObjectName(u"aab_btn_path")
        self.aab_btn_path.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_2.addWidget(self.aab_btn_path)

        self.aab_label_path = QLabel(self.adb_backup)
        self.aab_label_path.setObjectName(u"aab_label_path")
        self.aab_label_path.setScaledContents(True)
        self.aab_label_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.aab_label_path)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.aab_btn_clear = QPushButton(self.adb_backup)
        self.aab_btn_clear.setObjectName(u"aab_btn_clear")

        self.gridLayout_2.addWidget(self.aab_btn_clear, 0, 2, 1, 1)

        self.aab_ckb_apk = QCheckBox(self.adb_backup)
        self.aab_ckb_apk.setObjectName(u"aab_ckb_apk")

        self.gridLayout_2.addWidget(self.aab_ckb_apk, 1, 2, 1, 1)

        self.aab_btn_getapp_high = QPushButton(self.adb_backup)
        self.aab_btn_getapp_high.setObjectName(u"aab_btn_getapp_high")

        self.gridLayout_2.addWidget(self.aab_btn_getapp_high, 0, 1, 1, 1)

        self.aab_btn_backup = QPushButton(self.adb_backup)
        self.aab_btn_backup.setObjectName(u"aab_btn_backup")

        self.gridLayout_2.addWidget(self.aab_btn_backup, 0, 0, 1, 1)

        self.aab_btn_getapp_low = QPushButton(self.adb_backup)
        self.aab_btn_getapp_low.setObjectName(u"aab_btn_getapp_low")

        self.gridLayout_2.addWidget(self.aab_btn_getapp_low, 1, 1, 1, 1)

        self.aab_btn_restore = QPushButton(self.adb_backup)
        self.aab_btn_restore.setObjectName(u"aab_btn_restore")

        self.gridLayout_2.addWidget(self.aab_btn_restore, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.aab_label_name = QLabel(self.adb_backup)
        self.aab_label_name.setObjectName(u"aab_label_name")

        self.horizontalLayout_4.addWidget(self.aab_label_name)

        self.aab_lineedit_name = QLineEdit(self.adb_backup)
        self.aab_lineedit_name.setObjectName(u"aab_lineedit_name")

        self.horizontalLayout_4.addWidget(self.aab_lineedit_name)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.aab_textedit_log = QPlainTextEdit(self.adb_backup)
        self.aab_textedit_log.setObjectName(u"aab_textedit_log")
        font = QFont()
        font.setFamilies([u"FiraCode Nerd Font"])
        self.aab_textedit_log.setFont(font)

        self.verticalLayout.addWidget(self.aab_textedit_log)

        self.tabWidget.addTab(self.adb_backup, "")
        self.link = QWidget()
        self.link.setObjectName(u"link")
        self.gridLayout = QGridLayout(self.link)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(226, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.csl_btn_start = QPushButton(self.link)
        self.csl_btn_start.setObjectName(u"csl_btn_start")
        self.csl_btn_start.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.csl_btn_start, 5, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.csl_btn_from = QPushButton(self.link)
        self.csl_btn_from.setObjectName(u"csl_btn_from")
        self.csl_btn_from.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.csl_btn_from)

        self.csl_lineedit_from = QLineEdit(self.link)
        self.csl_lineedit_from.setObjectName(u"csl_lineedit_from")
        self.csl_lineedit_from.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.csl_lineedit_from)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(226, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.csl_btn_to = QPushButton(self.link)
        self.csl_btn_to.setObjectName(u"csl_btn_to")
        self.csl_btn_to.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_6.addWidget(self.csl_btn_to)

        self.csl_lineedit_to = QLineEdit(self.link)
        self.csl_lineedit_to.setObjectName(u"csl_lineedit_to")
        self.csl_lineedit_to.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.csl_lineedit_to)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.link, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u795e\u9f99\u5de5\u5177\u7bb1", None))
        self.aab_btn_device.setText(QCoreApplication.translate("gui", u"\u5237\u65b0\u8fde\u63a5\u8bbe\u5907", None))
        self.aab_btn_path.setText(QCoreApplication.translate("gui", u"\u9009\u62e9\u5907\u4efd\u6587\u4ef6\u8def\u5f84", None))
        self.aab_label_path.setText("")
        self.aab_btn_clear.setText(QCoreApplication.translate("gui", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.aab_ckb_apk.setText(QCoreApplication.translate("gui", u"\u5305\u62ec\u5b89\u88c5\u5305", None))
        self.aab_btn_getapp_high.setText(QCoreApplication.translate("gui", u"\u83b7\u53d6\u5305\u540d(\u9ad8\u7248\u672c)", None))
        self.aab_btn_backup.setText(QCoreApplication.translate("gui", u"\u5907\u4efd", None))
        self.aab_btn_getapp_low.setText(QCoreApplication.translate("gui", u"\u83b7\u53d6\u5305\u540d(\u4f4e\u7248\u672c)", None))
        self.aab_btn_restore.setText(QCoreApplication.translate("gui", u"\u6062\u590d", None))
        self.aab_label_name.setText(QCoreApplication.translate("gui", u"\u8f6f\u4ef6\u5305\u540d\uff1a", None))
        self.aab_textedit_log.setPlainText(QCoreApplication.translate("gui", u"\u795e\u9f99\u5de5\u5177\u7bb1 v1.0\n"
"\u4f5c\u8005\uff1aabcdesteve\n"
"    _                                   _   ____   ___ ____  _____ \n"
"   / \\__   _____   ___ ___  _ __   __ _| | |___ \\ / _ \\___ \\|___ / \n"
"  / _ \\ \\ / / _ \\ / __/ _ \\| '_ \\ / _` | |   __) | | | |__) | |_ \\ \n"
" / ___ \\ V / (_) | (_| (_) | | | | (_| | |  / __/| |_| / __/ ___) |\n"
"/_/   \\_\\_/ \\___/ \\___\\___/|_| |_|\\__,_|_| |_____|\\___/_____|____/ \n"
"   _   _ _       _      _   _                                       _ \n"
"  /_\\ | | |  _ _(_)__ _| |_| |_ ___  _ _ ___ ___ ___ _ ___ _____ __| |\n"
" / _ \\| | | | '_| / _` | ' \\  _(_-< | '_/ -_|_-</ -_) '_\\ V / -_) _` |\n"
"/_/ \\_\\_|_| |_| |_\\__, |_||_\\__/__/ |_| \\___/__/\\___|_|  \\_/\\___\\__,_|\n"
"                  |___/                                               ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adb_backup), QCoreApplication.translate("gui", u"\u5b89\u5353\u5e94\u7528\u5907\u4efd", None))
        self.csl_btn_start.setText(QCoreApplication.translate("gui", u"\u521b\u5efa", None))
        self.csl_btn_from.setText(QCoreApplication.translate("gui", u"\u9009\u62e9\u672c\u4f53\u8def\u5f84", None))
        self.csl_lineedit_from.setPlaceholderText(QCoreApplication.translate("gui", u"\u8bf7\u5148\u9009\u62e9\u672c\u4f53\u8def\u5f84", None))
        self.csl_btn_to.setText(QCoreApplication.translate("gui", u"\u9009\u62e9\u76ee\u6807\u8def\u5f84", None))
        self.csl_lineedit_to.setPlaceholderText(QCoreApplication.translate("gui", u"\u8bf7\u5148\u9009\u62e9\u76ee\u6807\u8def\u5f84(\u786e\u4fdd\u8be5\u8def\u5f84\u4e0d\u5b58\u5728)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.link), QCoreApplication.translate("gui", u"\u521b\u5efa\u7b26\u53f7\u94fe\u63a5", None))
    # retranslateUi

