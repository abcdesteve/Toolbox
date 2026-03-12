# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wireless.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton)

class Ui_wireless(object):
    def setupUi(self, wireless):
        if not wireless.objectName():
            wireless.setObjectName(u"wireless")
        wireless.resize(300, 190)
        wireless.setMinimumSize(QSize(300, 190))
        wireless.setMaximumSize(QSize(300, 190))
        self.verticalLayout_3 = QVBoxLayout(wireless)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(wireless)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_ip = QLabel(self.frame)
        self.label_ip.setObjectName(u"label_ip")

        self.verticalLayout.addWidget(self.label_ip)

        self.label_port = QLabel(self.frame)
        self.label_port.setObjectName(u"label_port")

        self.verticalLayout.addWidget(self.label_port)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineedit_ip = LineEdit(self.frame)
        self.lineedit_ip.setObjectName(u"lineedit_ip")
        self.lineedit_ip.setCursorPosition(0)
        self.lineedit_ip.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineedit_ip)

        self.lineedit_port = LineEdit(self.frame)
        self.lineedit_port.setObjectName(u"lineedit_port")
        self.lineedit_port.setCursorPosition(0)
        self.lineedit_port.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineedit_port)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(wireless)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.btn_cancel = PushButton(self.frame_2)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_connect = PrimaryPushButton(self.frame_2)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.btn_connect)


        self.verticalLayout_3.addWidget(self.frame_2)

        QWidget.setTabOrder(self.lineedit_ip, self.lineedit_port)
        QWidget.setTabOrder(self.lineedit_port, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_connect)

        self.retranslateUi(wireless)

        QMetaObject.connectSlotsByName(wireless)
    # setupUi

    def retranslateUi(self, wireless):
        wireless.setWindowTitle(QCoreApplication.translate("wireless", u"\u65e0\u7ebf\u8c03\u8bd5", None))
        self.label_ip.setText(QCoreApplication.translate("wireless", u"IP\u5730\u5740\uff1a", None))
        self.label_port.setText(QCoreApplication.translate("wireless", u"\u7aef\u53e3\uff1a", None))
        self.lineedit_ip.setText(QCoreApplication.translate("wireless", u"127.0.0.1", None))
        self.lineedit_port.setText(QCoreApplication.translate("wireless", u"5555", None))
#if QT_CONFIG(accessibility)
        self.frame_2.setAccessibleDescription(QCoreApplication.translate("wireless", u"dialog_lower_frame", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cancel.setText(QCoreApplication.translate("wireless", u"\u53d6\u6d88", None))
        self.btn_connect.setText(QCoreApplication.translate("wireless", u"\u8fde\u63a5", None))
    # retranslateUi

