# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fsa.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QSplitter,
    QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, HyperlinkLabel, PrimaryPushButton, ProgressBar,
    ProgressRing, PushButton, ScrollArea, TableWidget,
    ToolButton, VerticalSeparator)

class Ui_fsa(object):
    def setupUi(self, fsa):
        if not fsa.objectName():
            fsa.setObjectName(u"fsa")
        fsa.resize(718, 543)
        self.verticalLayout_3 = QVBoxLayout(fsa)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_achieve_folder = QLabel(fsa)
        self.label_achieve_folder.setObjectName(u"label_achieve_folder")

        self.horizontalLayout.addWidget(self.label_achieve_folder)

        self.cmb_folder = ComboBox(fsa)
        self.cmb_folder.setObjectName(u"cmb_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_folder.sizePolicy().hasHeightForWidth())
        self.cmb_folder.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cmb_folder)

        self.btn_add_folder = ToolButton(fsa)
        self.btn_add_folder.setObjectName(u"btn_add_folder")

        self.horizontalLayout.addWidget(self.btn_add_folder)

        self.btn_del_folder = ToolButton(fsa)
        self.btn_del_folder.setObjectName(u"btn_del_folder")
        self.btn_del_folder.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_del_folder)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(fsa)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.TableWidget = TableWidget(self.splitter)
        if (self.TableWidget.columnCount() < 4):
            self.TableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.TableWidget.setShowGrid(True)
        self.splitter.addWidget(self.TableWidget)
        self.TableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)
        self.TableWidget.verticalHeader().setStretchLastSection(True)
        self.VerticalSeparator = VerticalSeparator(self.splitter)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")
        self.splitter.addWidget(self.VerticalSeparator)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_parent = QLabel(self.layoutWidget)
        self.label_parent.setObjectName(u"label_parent")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_parent.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_parent)

        self.label_parent_data = HyperlinkLabel(self.layoutWidget)
        self.label_parent_data.setObjectName(u"label_parent_data")
        self.label_parent_data.setUnderlineVisible(True)

        self.horizontalLayout_7.addWidget(self.label_parent_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_dettime = QLabel(self.layoutWidget)
        self.label_dettime.setObjectName(u"label_dettime")
        self.label_dettime.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_dettime)

        self.label_dettime_data = QLabel(self.layoutWidget)
        self.label_dettime_data.setObjectName(u"label_dettime_data")
        self.label_dettime_data.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_dettime_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_det = QLabel(self.layoutWidget)
        self.label_det.setObjectName(u"label_det")
        self.label_det.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_det)

        self.label_det_data = QLabel(self.layoutWidget)
        self.label_det_data.setObjectName(u"label_det_data")
        self.label_det_data.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_det_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.ScrollArea = ScrollArea(self.layoutWidget)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setFrameShape(QFrame.NoFrame)
        self.ScrollArea.setFrameShadow(QFrame.Plain)
        self.ScrollArea.setLineWidth(0)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 197, 261))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_add = QLabel(self.scrollAreaWidgetContents)
        self.label_add.setObjectName(u"label_add")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_add.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_add)

        self.label_add_data = QLabel(self.scrollAreaWidgetContents)
        self.label_add_data.setObjectName(u"label_add_data")
        self.label_add_data.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_add_data)

        self.pgr_add = ProgressRing(self.scrollAreaWidgetContents)
        self.pgr_add.setObjectName(u"pgr_add")
        self.pgr_add.setMinimumSize(QSize(75, 75))
        self.pgr_add.setMaximumSize(QSize(75, 75))
        self.pgr_add.setTextVisible(True)

        self.horizontalLayout_4.addWidget(self.pgr_add)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_mod = QLabel(self.scrollAreaWidgetContents)
        self.label_mod.setObjectName(u"label_mod")
        self.label_mod.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_mod)

        self.label_mod_data = QLabel(self.scrollAreaWidgetContents)
        self.label_mod_data.setObjectName(u"label_mod_data")
        self.label_mod_data.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_mod_data)

        self.pgr_mod = ProgressRing(self.scrollAreaWidgetContents)
        self.pgr_mod.setObjectName(u"pgr_mod")
        self.pgr_mod.setMinimumSize(QSize(75, 75))
        self.pgr_mod.setMaximumSize(QSize(75, 75))
        self.pgr_mod.setTextVisible(True)

        self.horizontalLayout_5.addWidget(self.pgr_mod)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_del = QLabel(self.scrollAreaWidgetContents)
        self.label_del.setObjectName(u"label_del")
        self.label_del.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_del)

        self.label_del_data = QLabel(self.scrollAreaWidgetContents)
        self.label_del_data.setObjectName(u"label_del_data")
        self.label_del_data.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_del_data)

        self.pgr_del = ProgressRing(self.scrollAreaWidgetContents)
        self.pgr_del.setObjectName(u"pgr_del")
        self.pgr_del.setMinimumSize(QSize(75, 75))
        self.pgr_del.setMaximumSize(QSize(75, 75))
        self.pgr_del.setTextVisible(True)

        self.horizontalLayout_6.addWidget(self.pgr_del)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.ScrollArea)

        self.btn_export_snap = PushButton(self.layoutWidget)
        self.btn_export_snap.setObjectName(u"btn_export_snap")

        self.verticalLayout_2.addWidget(self.btn_export_snap)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_3.addWidget(self.splitter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_del_snap = PushButton(fsa)
        self.btn_del_snap.setObjectName(u"btn_del_snap")
        self.btn_del_snap.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_del_snap)

        self.btn_crt_snap = PrimaryPushButton(fsa)
        self.btn_crt_snap.setObjectName(u"btn_crt_snap")
        self.btn_crt_snap.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_crt_snap)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(fsa)

        QMetaObject.connectSlotsByName(fsa)
    # setupUi

    def retranslateUi(self, fsa):
        fsa.setWindowTitle(QCoreApplication.translate("fsa", u"Form", None))
        self.label_achieve_folder.setText(QCoreApplication.translate("fsa", u"\u5feb\u7167\u5b58\u6863\u5e93\uff1a", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("fsa", u"\u5feb\u7167\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("fsa", u"\u5feb\u7167\u5907\u6ce8", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("fsa", u"\u5feb\u7167\u4ee3\u53f7", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("fsa", u"\u6587\u4ef6\u8ba1\u6570", None));
        self.label_parent.setText(QCoreApplication.translate("fsa", u"\u7236\u8282\u70b9\uff1a", None))
        self.label_parent_data.setText("")
        self.label_dettime.setText(QCoreApplication.translate("fsa", u"\u8ddd\u79bb\u4e0a\u6b21\u6539\u52a8\u65f6\u95f4\uff1a", None))
        self.label_dettime_data.setText("")
        self.label_det.setText(QCoreApplication.translate("fsa", u"\u603b\u6539\u52a8\uff1a", None))
        self.label_det_data.setText(QCoreApplication.translate("fsa", u"0", None))
        self.label_add.setText(QCoreApplication.translate("fsa", u"\u65b0\u589e\uff1a", None))
        self.label_add_data.setText(QCoreApplication.translate("fsa", u"0", None))
        self.label_mod.setText(QCoreApplication.translate("fsa", u"\u4fee\u6539\uff1a", None))
        self.label_mod_data.setText(QCoreApplication.translate("fsa", u"0", None))
        self.label_del.setText(QCoreApplication.translate("fsa", u"\u5220\u9664\uff1a", None))
        self.label_del_data.setText(QCoreApplication.translate("fsa", u"0", None))
        self.btn_export_snap.setText(QCoreApplication.translate("fsa", u"\u5bfc\u51fa\u5feb\u7167", None))
        self.btn_del_snap.setText(QCoreApplication.translate("fsa", u"\u5220\u9664\u5feb\u7167", None))
        self.btn_del_snap.setProperty(u"lightCustomQss", QCoreApplication.translate("fsa", u"PushButton{background-color:#e81123;}PushButton:hover{background-color:#e63342;}", None))
        self.btn_del_snap.setProperty(u"darkCustomQss", QCoreApplication.translate("fsa", u"PushButton{background-color:#e81123;}PushButton:hover{background-color:#e63342;}", None))
        self.btn_crt_snap.setText(QCoreApplication.translate("fsa", u"\u521b\u5efa\u5feb\u7167", None))
    # retranslateUi

