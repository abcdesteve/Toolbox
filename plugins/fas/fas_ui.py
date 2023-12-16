# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidgetItem, QWidget)

from qfluentwidgets import (PrimaryPushButton, PushButton, TableWidget)

class Ui_fas(object):
    def setupUi(self, fas):
        if not fas.objectName():
            fas.setObjectName(u"fas")
        fas.resize(747, 522)
        self.gridLayout = QGridLayout(fas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = TableWidget(fas)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)

        self.btn_del = PushButton(fas)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setEnabled(False)

        self.gridLayout.addWidget(self.btn_del, 1, 0, 1, 1)

        self.btn_add = PrimaryPushButton(fas)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout.addWidget(self.btn_add, 1, 1, 1, 1)


        self.retranslateUi(fas)

        QMetaObject.connectSlotsByName(fas)
    # setupUi

    def retranslateUi(self, fas):
        fas.setWindowTitle(QCoreApplication.translate("fas", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("fas", u"\u4efb\u52a1\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("fas", u"\u53cc\u5411\u540c\u6b65\uff1f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("fas", u"\u6267\u884c\u95f4\u9694", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("fas", u"\u4e0a\u6b21\u6267\u884c\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("fas", u"\u6267\u884c\u6b21\u6570", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("fas", u"\u64cd\u4f5c\u6587\u4ef6\u6570\u7edf\u8ba1", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("fas", u"\u64cd\u4f5c\u6587\u4ef6\u5927\u5c0f\u7edf\u8ba1", None));
        self.btn_del.setText(QCoreApplication.translate("fas", u"\u5220\u9664", None))
        self.btn_del.setProperty("lightCustonQss", QCoreApplication.translate("fas", u"PushButton{background-color:#e81123;}\n"
"PushButton:hover{background-color:#e63342;}", None))
        self.btn_del.setProperty("darkCustomQss", QCoreApplication.translate("fas", u"PushButton{background-color:#e81123;}\n"
"PushButton:hover{background-color:#e63342;}", None))
        self.btn_add.setText(QCoreApplication.translate("fas", u"\u6dfb\u52a0", None))
    # retranslateUi

