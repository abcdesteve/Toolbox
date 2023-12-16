# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import EditableComboBox

class Ui_Input_dialog(object):
    def setupUi(self, Input_dialog):
        if not Input_dialog.objectName():
            Input_dialog.setObjectName(u"Input_dialog")
        Input_dialog.resize(350, 125)
        self.verticalLayout = QVBoxLayout(Input_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Input_dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(10)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = EditableComboBox(Input_dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)


        self.retranslateUi(Input_dialog)

        QMetaObject.connectSlotsByName(Input_dialog)
    # setupUi

    def retranslateUi(self, Input_dialog):
        Input_dialog.setWindowTitle(QCoreApplication.translate("Input_dialog", u"Form", None))
        self.label.setText("")
    # retranslateUi

