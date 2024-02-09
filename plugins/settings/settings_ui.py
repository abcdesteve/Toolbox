# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import ScrollArea

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(400, 150)
        self.verticalLayout = QVBoxLayout(settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollAreaWidget = ScrollArea(settings)
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setWidgetResizable(True)
        self.scrollArea = QWidget()
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 380, 130))
        self.verticalLayout_2 = QVBoxLayout(self.scrollArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollAreaWidget.setWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.scrollAreaWidget)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
    # retranslateUi

