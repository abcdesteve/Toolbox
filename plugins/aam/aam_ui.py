# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aam.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, EditableComboBox, LineEdit, PrimaryPushButton,
    PushButton, ScrollArea, SwitchButton, TextEdit)

class Ui_aam(object):
    def setupUi(self, aam):
        if not aam.objectName():
            aam.setObjectName(u"aam")
        aam.resize(800, 433)
        aam.setAcceptDrops(True)
        self.verticalLayout_3 = QVBoxLayout(aam)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.btn_device = PushButton(aam)
        self.btn_device.setObjectName(u"btn_device")
        self.btn_device.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_1.addWidget(self.btn_device)

        self.cmb_device = ComboBox(aam)
        self.cmb_device.setObjectName(u"cmb_device")

        self.horizontalLayout_1.addWidget(self.cmb_device)

        self.btn_wireless = PushButton(aam)
        self.btn_wireless.setObjectName(u"btn_wireless")
        self.btn_wireless.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_1.addWidget(self.btn_wireless)


        self.verticalLayout_3.addLayout(self.horizontalLayout_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_app = QLabel(aam)
        self.label_app.setObjectName(u"label_app")
        self.label_app.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.label_app)

        self.cmb_app = EditableComboBox(aam)
        self.cmb_app.setObjectName(u"cmb_app")

        self.horizontalLayout.addWidget(self.cmb_app)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_app_icon = QLabel(aam)
        self.label_app_icon.setObjectName(u"label_app_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_app_icon.sizePolicy().hasHeightForWidth())
        self.label_app_icon.setSizePolicy(sizePolicy)
        self.label_app_icon.setMaximumSize(QSize(50, 50))
        self.label_app_icon.setScaledContents(True)
        self.label_app_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_app_icon)

        self.label_app_name = QLabel(aam)
        self.label_app_name.setObjectName(u"label_app_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_app_name.sizePolicy().hasHeightForWidth())
        self.label_app_name.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_app_name.setFont(font)
        self.label_app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_app_name)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ckb_app_user = SwitchButton(aam)
        self.ckb_app_user.setObjectName(u"ckb_app_user")
        self.ckb_app_user.setChecked(True)

        self.horizontalLayout_2.addWidget(self.ckb_app_user)

        self.ckb_app_sys = SwitchButton(aam)
        self.ckb_app_sys.setObjectName(u"ckb_app_sys")

        self.horizontalLayout_2.addWidget(self.ckb_app_sys)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.layout_device_info = QHBoxLayout()
        self.layout_device_info.setSpacing(0)
        self.layout_device_info.setObjectName(u"layout_device_info")

        self.horizontalLayout_4.addLayout(self.layout_device_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.scrollArea = ScrollArea(aam)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(0, 70))
        self.scrollArea.setMaximumSize(QSize(16777215, 70))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 399, 70))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{background-color:transparent}")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_launch = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_launch.setObjectName(u"btn_launch")

        self.gridLayout.addWidget(self.btn_launch, 0, 0, 1, 1)

        self.btn_install = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_install.setObjectName(u"btn_install")

        self.gridLayout.addWidget(self.btn_install, 0, 1, 1, 1)

        self.btn_freeze = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_freeze.setObjectName(u"btn_freeze")

        self.gridLayout.addWidget(self.btn_freeze, 0, 2, 1, 1)

        self.btn_backup = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_backup.setObjectName(u"btn_backup")

        self.gridLayout.addWidget(self.btn_backup, 0, 3, 1, 1)

        self.btn_grant_permission = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_grant_permission.setObjectName(u"btn_grant_permission")

        self.gridLayout.addWidget(self.btn_grant_permission, 0, 4, 1, 1)

        self.btn_extract = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_extract.setObjectName(u"btn_extract")

        self.gridLayout.addWidget(self.btn_extract, 1, 0, 1, 1)

        self.btn_uninstall = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_uninstall.setObjectName(u"btn_uninstall")

        self.gridLayout.addWidget(self.btn_uninstall, 1, 1, 1, 1)

        self.btn_unfreeze = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_unfreeze.setObjectName(u"btn_unfreeze")

        self.gridLayout.addWidget(self.btn_unfreeze, 1, 2, 1, 1)

        self.btn_restore = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_restore.setObjectName(u"btn_restore")

        self.gridLayout.addWidget(self.btn_restore, 1, 3, 1, 1)

        self.btn_revoke_permission = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.btn_revoke_permission.setObjectName(u"btn_revoke_permission")

        self.gridLayout.addWidget(self.btn_revoke_permission, 1, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_get_app = PushButton(aam)
        self.btn_get_app.setObjectName(u"btn_get_app")

        self.verticalLayout_2.addWidget(self.btn_get_app)

        self.btn_clear = PushButton(aam)
        self.btn_clear.setObjectName(u"btn_clear")

        self.verticalLayout_2.addWidget(self.btn_clear)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.textedit_log = TextEdit(aam)
        self.textedit_log.setObjectName(u"textedit_log")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.textedit_log.setFont(font1)
        self.textedit_log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textedit_log)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cmd = QLabel(aam)
        self.label_cmd.setObjectName(u"label_cmd")

        self.horizontalLayout_3.addWidget(self.label_cmd)

        self.lineedit_cmd = LineEdit(aam)
        self.lineedit_cmd.setObjectName(u"lineedit_cmd")
        self.lineedit_cmd.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineedit_cmd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.btn_device, self.cmb_device)
        QWidget.setTabOrder(self.cmb_device, self.btn_wireless)
        QWidget.setTabOrder(self.btn_wireless, self.cmb_app)
        QWidget.setTabOrder(self.cmb_app, self.btn_launch)
        QWidget.setTabOrder(self.btn_launch, self.btn_extract)
        QWidget.setTabOrder(self.btn_extract, self.btn_install)
        QWidget.setTabOrder(self.btn_install, self.btn_uninstall)
        QWidget.setTabOrder(self.btn_uninstall, self.btn_freeze)
        QWidget.setTabOrder(self.btn_freeze, self.btn_unfreeze)
        QWidget.setTabOrder(self.btn_unfreeze, self.btn_backup)
        QWidget.setTabOrder(self.btn_backup, self.btn_restore)
        QWidget.setTabOrder(self.btn_restore, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.textedit_log)
        QWidget.setTabOrder(self.textedit_log, self.lineedit_cmd)

        self.retranslateUi(aam)

        QMetaObject.connectSlotsByName(aam)
    # setupUi

    def retranslateUi(self, aam):
        aam.setWindowTitle(QCoreApplication.translate("aam", u"Form", None))
        self.btn_device.setText(QCoreApplication.translate("aam", u"\u5237\u65b0\u8fde\u63a5\u8bbe\u5907", None))
        self.btn_wireless.setText(QCoreApplication.translate("aam", u"\u65e0\u7ebf\u8c03\u8bd5", None))
        self.label_app.setText(QCoreApplication.translate("aam", u"\u5e94\u7528\u5305\u540d\uff1a", None))
        self.label_app_icon.setText("")
        self.label_app_name.setText("")
        self.ckb_app_user.setText(QCoreApplication.translate("aam", u"\u7528\u6237\u5e94\u7528", None))
        self.ckb_app_sys.setText(QCoreApplication.translate("aam", u"\u7cfb\u7edf\u5e94\u7528", None))
        self.btn_launch.setText(QCoreApplication.translate("aam", u"\u542f\u52a8", None))
        self.btn_install.setText(QCoreApplication.translate("aam", u"\u5b89\u88c5", None))
        self.btn_freeze.setText(QCoreApplication.translate("aam", u"\u51bb\u7ed3", None))
        self.btn_backup.setText(QCoreApplication.translate("aam", u"\u5907\u4efd", None))
        self.btn_grant_permission.setText(QCoreApplication.translate("aam", u"\u63d0\u6743", None))
        self.btn_extract.setText(QCoreApplication.translate("aam", u"\u63d0\u53d6", None))
        self.btn_uninstall.setText(QCoreApplication.translate("aam", u"\u5378\u8f7d", None))
        self.btn_unfreeze.setText(QCoreApplication.translate("aam", u"\u89e3\u51bb", None))
        self.btn_restore.setText(QCoreApplication.translate("aam", u"\u6062\u590d", None))
        self.btn_revoke_permission.setText(QCoreApplication.translate("aam", u"\u964d\u6743", None))
        self.btn_get_app.setText(QCoreApplication.translate("aam", u"\u83b7\u53d6\u5305\u540d", None))
        self.btn_clear.setText(QCoreApplication.translate("aam", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.textedit_log.setMarkdown(QCoreApplication.translate("aam", u"\u795e\u9f99\u5de5\u5177\u7bb1 v2.1\n"
"\n"
"\u4f5c\u8005\uff1aabcdesteve\n"
"\n"
"`     _                                   _   ____   ___ ____  _  _             \n"
"     `\n"
"\n"
"`    / \\__   _____   ___ ___  _ __   __ _| | |___ \\ / _ \\___ \\| || |            \n"
"     `\n"
"\n"
"``   / _ \\ \\ / / _ \\ / __/ _ \\| '_ \\ / _` | |   __) | | | |__) | || |_           \n"
"     ``\n"
"\n"
"`  / ___ \\ V / (_) | (_| (_) | | | | (_| | |  / __/| |_| / __/|__   _|          \n"
"     `\n"
"\n"
"` /_/ _ \\_\\_/_\\___/ \\___\\___/|_| |_|\\__,_|_| |_____|\\___/_____|  |_|            \n"
"   _ `\n"
"\n"
"`    / \\  | | |  _ __(_) __ _| |__ | |_ ___   _ __ ___  ___  ___ _ ____   _____ \n"
"__| |`\n"
"\n"
"``   / _ \\ | | | | '__| |/ _` | '_ \\| __/ __| | '__/ _ \\/ __|/ _ \\ '__\\ \\ / / _\n"
"\\/ _` |``\n"
"\n"
"`  / ___ \\| | | | |  | | (_| | | | | |_\\__ \\ | | |  __/\\__ \\  __/ |   \\ V /  __/\n"
"(_| |`\n"
"\n"
"` /_/   \\_\\_|_| |_|  |_|\\__, |_| |_|\\__|___/ |_|  \\___||___/\\___|_|    \\_/\n"
"\\___|\\__,_|"
                        "`\n"
"\n"
"`                       |___/                                                   \n"
"     `\n"
"\n"
"", None))
        self.textedit_log.setHtml(QCoreApplication.translate("aam", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font'; font-size:9pt;\">\u795e\u9f99\u5de5\u5177\u7bb1 v2.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font'; font-size:9pt;\">\u4f5c\u8005\uff1aabcdesteve</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">     _                                   _   ____   ___ ____  _  _                   </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">    / \\__   _____   ___ ___  _ __   __ _| | |___ \\ / _ \\___ \\| || |                  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">   / _ \\ \\ / / _ \\ / __/ _ \\| '_ \\ / _` | |   __) | | | |__) | || |_                 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">  / ___ \\ V / (_) | (_| (_) | | | | (_| | |  / __/| |_| / __/|__   _|                </span></p>\n"
"<p style"
                        "=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\"> /_/ _ \\_\\_/_\\___/ \\___\\___/|_| |_|\\__,_|_| |_____|\\___/_____|  |_|                _ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">    / \\  | | |  _ __(_) __ _| |__ | |_ ___   _ __ ___  ___  ___ _ ____   _____  __| |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">   / _ \\ | | | | '__| |/ _` | '_ \\| __/ __| | '__/ _ \\/ __|/ _ \\ '__\\ \\ / / _ \\/ _` |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">  / ___ \\| | | | |  | | (_| | | | | |_\\__ \\ | | |  _"
                        "_/\\__ \\  __/ |   \\ V /  __/ (_| |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\"> /_/   \\_\\_|_| |_|  |_|\\__, |_| |_|\\__|___/ |_|  \\___||___/\\___|_|    \\_/ \\___|\\__,_|</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New';\">                       |___/                                                         </span></p></body></html>", None))
        self.label_cmd.setText(QCoreApplication.translate("aam", u"\u8fd0\u884c\u547d\u4ee4\uff1a", None))
        self.lineedit_cmd.setPlaceholderText(QCoreApplication.translate("aam", u"\u5185\u7f6eadb\u3001fastboot\u5de5\u5177", None))
    # retranslateUi

