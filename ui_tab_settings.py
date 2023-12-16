# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QRadioButton, QSizePolicy,
    QToolButton, QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(400, 175)
        self.gridLayout = QGridLayout(settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_theme = QLabel(settings)
        self.label_theme.setObjectName(u"label_theme")

        self.gridLayout.addWidget(self.label_theme, 0, 0, 1, 1)

        self.radio_light = QRadioButton(settings)
        self.radio_light.setObjectName(u"radio_light")
        self.radio_light.setChecked(True)

        self.gridLayout.addWidget(self.radio_light, 0, 1, 1, 2)

        self.radio_dark = QRadioButton(settings)
        self.radio_dark.setObjectName(u"radio_dark")

        self.gridLayout.addWidget(self.radio_dark, 0, 3, 1, 1)

        self.radio_colorful = QRadioButton(settings)
        self.radio_colorful.setObjectName(u"radio_colorful")

        self.gridLayout.addWidget(self.radio_colorful, 0, 4, 1, 1)

        self.cmb_theme = QComboBox(settings)
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.addItem("")
        self.cmb_theme.setObjectName(u"cmb_theme")
        self.cmb_theme.setEnabled(False)

        self.gridLayout.addWidget(self.cmb_theme, 1, 1, 1, 4)

        self.line = QFrame(settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 5)

        self.label_animation = QLabel(settings)
        self.label_animation.setObjectName(u"label_animation")

        self.gridLayout.addWidget(self.label_animation, 3, 0, 1, 1)

        self.ckb_enable_animation = QCheckBox(settings)
        self.ckb_enable_animation.setObjectName(u"ckb_enable_animation")
        self.ckb_enable_animation.setChecked(True)

        self.gridLayout.addWidget(self.ckb_enable_animation, 3, 1, 1, 1)

        self.cmb_animation = QComboBox(settings)
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.setObjectName(u"cmb_animation")

        self.gridLayout.addWidget(self.cmb_animation, 3, 2, 1, 3)

        self.widget = QWidget(settings)
        self.widget.setObjectName(u"widget")
        self.animation_example = QToolButton(self.widget)
        self.animation_example.setObjectName(u"animation_example")
        self.animation_example.setGeometry(QRect(10, 10, 24, 22))

        self.gridLayout.addWidget(self.widget, 4, 0, 1, 5)


        self.retranslateUi(settings)

        self.cmb_animation.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
        self.label_theme.setText(QCoreApplication.translate("settings", u"\u4e3b\u9898\uff1a", None))
        self.radio_light.setText(QCoreApplication.translate("settings", u"\u6d45\u8272\uff08\u91cd\u542f\u751f\u6548\uff09", None))
        self.radio_dark.setText(QCoreApplication.translate("settings", u"\u6df1\u8272", None))
        self.radio_colorful.setText(QCoreApplication.translate("settings", u"\u591a\u5f69 BETA", None))
        self.cmb_theme.setItemText(0, QCoreApplication.translate("settings", u"dark_amber", None))
        self.cmb_theme.setItemText(1, QCoreApplication.translate("settings", u"dark_blue", None))
        self.cmb_theme.setItemText(2, QCoreApplication.translate("settings", u"dark_cyan", None))
        self.cmb_theme.setItemText(3, QCoreApplication.translate("settings", u"dark_lightgreen", None))
        self.cmb_theme.setItemText(4, QCoreApplication.translate("settings", u"dark_pink", None))
        self.cmb_theme.setItemText(5, QCoreApplication.translate("settings", u"dark_purple", None))
        self.cmb_theme.setItemText(6, QCoreApplication.translate("settings", u"dark_red", None))
        self.cmb_theme.setItemText(7, QCoreApplication.translate("settings", u"dark_teal", None))
        self.cmb_theme.setItemText(8, QCoreApplication.translate("settings", u"dark_yellow", None))
        self.cmb_theme.setItemText(9, QCoreApplication.translate("settings", u"light_amber", None))
        self.cmb_theme.setItemText(10, QCoreApplication.translate("settings", u"light_blue", None))
        self.cmb_theme.setItemText(11, QCoreApplication.translate("settings", u"light_cyan", None))
        self.cmb_theme.setItemText(12, QCoreApplication.translate("settings", u"light_cyan_500", None))
        self.cmb_theme.setItemText(13, QCoreApplication.translate("settings", u"light_lightgreen", None))
        self.cmb_theme.setItemText(14, QCoreApplication.translate("settings", u"light_pink", None))
        self.cmb_theme.setItemText(15, QCoreApplication.translate("settings", u"light_purple", None))
        self.cmb_theme.setItemText(16, QCoreApplication.translate("settings", u"light_red", None))
        self.cmb_theme.setItemText(17, QCoreApplication.translate("settings", u"light_teal", None))
        self.cmb_theme.setItemText(18, QCoreApplication.translate("settings", u"light_yellow", None))

        self.label_animation.setText(QCoreApplication.translate("settings", u"\u52a8\u753b\uff1a", None))
        self.ckb_enable_animation.setText(QCoreApplication.translate("settings", u"\u5f00\u542f\u52a8\u753b", None))
        self.cmb_animation.setItemText(0, QCoreApplication.translate("settings", u"Linear", None))
        self.cmb_animation.setItemText(1, QCoreApplication.translate("settings", u"InOutQuad", None))
        self.cmb_animation.setItemText(2, QCoreApplication.translate("settings", u"InOutCubic", None))
        self.cmb_animation.setItemText(3, QCoreApplication.translate("settings", u"InOutSine", None))
        self.cmb_animation.setItemText(4, QCoreApplication.translate("settings", u"InOutElastic", None))
        self.cmb_animation.setItemText(5, QCoreApplication.translate("settings", u"InOutBack", None))
        self.cmb_animation.setItemText(6, QCoreApplication.translate("settings", u"InOutBounce", None))

        self.animation_example.setText(QCoreApplication.translate("settings", u"-", None))
    # retranslateUi

