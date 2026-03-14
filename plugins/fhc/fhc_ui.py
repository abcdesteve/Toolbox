# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fhc.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidgetItem, QWidget)

from qfluentwidgets import (PlainTextEdit, PrimaryPushButton, PushButton, TableWidget)

class Ui_fhc(object):
    def setupUi(self, fhc):
        if not fhc.objectName():
            fhc.setObjectName(u"fhc")
        fhc.resize(451, 297)
        fhc.setAcceptDrops(True)
        self.gridLayout = QGridLayout(fhc)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_A = PrimaryPushButton(fhc)
        self.btn_A.setObjectName(u"btn_A")
        self.btn_A.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.btn_A, 0, 0, 1, 1)

        self.btn_B = PrimaryPushButton(fhc)
        self.btn_B.setObjectName(u"btn_B")
        self.btn_B.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.btn_B, 0, 1, 1, 1)

        self.lineedit_A = PlainTextEdit(fhc)
        self.lineedit_A.setObjectName(u"lineedit_A")
        self.lineedit_A.setAcceptDrops(False)
        self.lineedit_A.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.lineedit_A, 1, 0, 1, 1)

        self.lineedit_B = PlainTextEdit(fhc)
        self.lineedit_B.setObjectName(u"lineedit_B")
        self.lineedit_B.setAcceptDrops(False)
        self.lineedit_B.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.lineedit_B, 1, 1, 1, 1)

        self.tablewidget = TableWidget(fhc)
        if (self.tablewidget.columnCount() < 3):
            self.tablewidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tablewidget.rowCount() < 10):
            self.tablewidget.setRowCount(10)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        self.tablewidget.setObjectName(u"tablewidget")
        self.tablewidget.setFocusPolicy(Qt.NoFocus)
        self.tablewidget.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"    /* font: 13px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"QTableView::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"}\n"
"\n"
"QTableView::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"QTableView::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}\n"
"\n"
"QTableView::indicator:checked,\n"
"QTableView::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
""
                        "    background-color: #009faa;\n"
"}\n"
"\n"
"QTableView::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"QTableView::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"QTableView::indicator:checked:hover,\n"
"QTableView::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"QTableView::indicator:checked:pressed,\n"
"QTableView::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"QTableView::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableView::indicator:checked:disabled,\n"
"QTableView::indicator:indeterminate:disabled {\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}\n"
"\n"
"\n"
"QHeaderView {\n"
"    background-color: transpa"
                        "rent;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 19);\n"
"    font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 7);\n"
"    border-left: none;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Down_black.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
""
                        "    image: url(:/qfluentwidgets/images/table_view/Up_black.svg);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(0, 0, 0, 19);\n"
"}\n"
"\n"
"QTableCornerButton::section:pressed {\n"
"    background-color: rgba(0, 0, 0, 12);\n"
"}")
        self.tablewidget.setColumnCount(3)
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tablewidget, 2, 0, 1, 2)

        QWidget.setTabOrder(self.btn_A, self.lineedit_A)
        QWidget.setTabOrder(self.lineedit_A, self.btn_B)
        QWidget.setTabOrder(self.btn_B, self.lineedit_B)
        QWidget.setTabOrder(self.lineedit_B, self.tablewidget)

        self.retranslateUi(fhc)

        QMetaObject.connectSlotsByName(fhc)
    # setupUi

    def retranslateUi(self, fhc):
        fhc.setWindowTitle(QCoreApplication.translate("fhc", u"Form", None))
        self.btn_A.setText(QCoreApplication.translate("fhc", u"\u9009\u62e9\u6587\u4ef6", None))
        self.btn_B.setText(QCoreApplication.translate("fhc", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lineedit_A.setPlaceholderText(QCoreApplication.translate("fhc", u"\u62d6\u5165\u6587\u4ef6\u5230\u6b64\u5904 \u6216\u7c98\u8d34\u54c8\u5e0c\u503c\u81f3\u4e0b\u65b9\u8868\u683c", None))
        self.lineedit_B.setPlaceholderText(QCoreApplication.translate("fhc", u"\u62d6\u5165\u6587\u4ef6\u5230\u6b64\u5904 \u6216\u7c98\u8d34\u54c8\u5e0c\u503c\u81f3\u4e0b\u65b9\u8868\u683c", None))
        ___qtablewidgetitem = self.tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("fhc", u"A\u533a\u54c8\u5e0c\u503c", None));
        ___qtablewidgetitem1 = self.tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("fhc", u"\u6bd4\u8f83\u7ed3\u679c", None));
        ___qtablewidgetitem2 = self.tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("fhc", u"B\u533a\u54c8\u5e0c\u503c", None));
        ___qtablewidgetitem3 = self.tablewidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("fhc", u"\u5b57\u7b26\u6570", None));
        ___qtablewidgetitem4 = self.tablewidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("fhc", u"\u6587\u4ef6\u5927\u5c0f", None));
        ___qtablewidgetitem5 = self.tablewidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("fhc", u"CRC32", None));
        ___qtablewidgetitem6 = self.tablewidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("fhc", u"MD5", None));
        ___qtablewidgetitem7 = self.tablewidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("fhc", u"BLAKE3", None));
        ___qtablewidgetitem8 = self.tablewidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("fhc", u"SHA1", None));
        ___qtablewidgetitem9 = self.tablewidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("fhc", u"SHA224", None));
        ___qtablewidgetitem10 = self.tablewidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("fhc", u"SHA256", None));
        ___qtablewidgetitem11 = self.tablewidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("fhc", u"SHA384", None));
        ___qtablewidgetitem12 = self.tablewidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("fhc", u"SHA512", None));
    # retranslateUi

