# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (EditableComboBox, LineEdit, PrimaryPushButton, PushButton)

class Ui_Input_dialog(object):
    def setupUi(self, Input_dialog):
        if not Input_dialog.objectName():
            Input_dialog.setObjectName(u"Input_dialog")
        Input_dialog.resize(350, 249)
        self.verticalLayout = QVBoxLayout(Input_dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Input_dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.title = QLabel(self.frame_2)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(16)
        self.title.setFont(font)

        self.verticalLayout_3.addWidget(self.title)

        self.content = QLabel(self.frame_2)
        self.content.setObjectName(u"content")
        font1 = QFont()
        font1.setPointSize(11)
        self.content.setFont(font1)
        self.content.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.content)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Input_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{background-color:#202020}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.comboBox = EditableComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cancel = PushButton(self.frame)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_ok = PrimaryPushButton(self.frame)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout_2.addWidget(self.btn_ok)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Input_dialog)

        QMetaObject.connectSlotsByName(Input_dialog)
    # setupUi

    def retranslateUi(self, Input_dialog):
        Input_dialog.setWindowTitle(QCoreApplication.translate("Input_dialog", u"Form", None))
        self.btn_cancel.setText(QCoreApplication.translate("Input_dialog", u"\u53d6\u6d88", None))
        self.btn_ok.setText(QCoreApplication.translate("Input_dialog", u"\u786e\u5b9a", None))
    # retranslateUi

