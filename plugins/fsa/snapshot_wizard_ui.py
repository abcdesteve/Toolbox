# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'snapshot_wizard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, LineEdit, Pivot, PrimaryPushButton,
    PushButton, SegmentedToolWidget, ToggleToolButton, ToolButton,
    TreeWidget)

class Ui_snapshot_wizard(object):
    def setupUi(self, snapshot_wizard):
        if not snapshot_wizard.objectName():
            snapshot_wizard.setObjectName(u"snapshot_wizard")
        snapshot_wizard.resize(500, 300)
        self.verticalLayout = QVBoxLayout(snapshot_wizard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_file = PushButton(snapshot_wizard)
        self.btn_add_file.setObjectName(u"btn_add_file")

        self.horizontalLayout_2.addWidget(self.btn_add_file)

        self.btn_add_folder = PushButton(snapshot_wizard)
        self.btn_add_folder.setObjectName(u"btn_add_folder")

        self.horizontalLayout_2.addWidget(self.btn_add_folder)

        self.btn_del = ToolButton(snapshot_wizard)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_del)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toggle_filter = SegmentedToolWidget(snapshot_wizard)
        self.toggle_filter.setObjectName(u"toggle_filter")
        self.toggle_filter.setMinimumSize(QSize(118, 33))
        self.toggle_filter.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.toggle_filter)

        self.lineedit_filter = LineEdit(snapshot_wizard)
        self.lineedit_filter.setObjectName(u"lineedit_filter")
        self.lineedit_filter.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineedit_filter)

        self.label_hidden = QLabel(snapshot_wizard)
        self.label_hidden.setObjectName(u"label_hidden")

        self.horizontalLayout_4.addWidget(self.label_hidden)

        self.toggle_windows = ToggleToolButton(snapshot_wizard)
        self.toggle_windows.setObjectName(u"toggle_windows")
        self.toggle_windows.setMinimumSize(QSize(32, 32))
        self.toggle_windows.setMaximumSize(QSize(32, 32))
        self.toggle_windows.setChecked(True)

        self.horizontalLayout_4.addWidget(self.toggle_windows)

        self.toggle_unix = ToggleToolButton(snapshot_wizard)
        self.toggle_unix.setObjectName(u"toggle_unix")
        self.toggle_unix.setMinimumSize(QSize(32, 32))
        self.toggle_unix.setMaximumSize(QSize(32, 32))
        self.toggle_unix.setChecked(True)

        self.horizontalLayout_4.addWidget(self.toggle_unix)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.TreeWidget = TreeWidget(snapshot_wizard)
        self.TreeWidget.setObjectName(u"TreeWidget")
        self.TreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.TreeWidget.setTabKeyNavigation(True)
        self.TreeWidget.setAlternatingRowColors(True)
        self.TreeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.TreeWidget.setUniformRowHeights(True)
        self.TreeWidget.setAnimated(True)
        self.TreeWidget.header().setProperty(u"showSortIndicator", True)

        self.verticalLayout.addWidget(self.TreeWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_count = QLabel(snapshot_wizard)
        self.label_count.setObjectName(u"label_count")

        self.horizontalLayout.addWidget(self.label_count)

        self.label_count_data = QLabel(snapshot_wizard)
        self.label_count_data.setObjectName(u"label_count_data")

        self.horizontalLayout.addWidget(self.label_count_data)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ckb_calc_hash = CheckBox(snapshot_wizard)
        self.ckb_calc_hash.setObjectName(u"ckb_calc_hash")
        self.ckb_calc_hash.setChecked(True)

        self.horizontalLayout.addWidget(self.ckb_calc_hash)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_cancel = PushButton(snapshot_wizard)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.btn_create = PrimaryPushButton(snapshot_wizard)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_create)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.btn_add_file, self.btn_add_folder)
        QWidget.setTabOrder(self.btn_add_folder, self.btn_del)
        QWidget.setTabOrder(self.btn_del, self.TreeWidget)
        QWidget.setTabOrder(self.TreeWidget, self.ckb_calc_hash)
        QWidget.setTabOrder(self.ckb_calc_hash, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_create)

        self.retranslateUi(snapshot_wizard)

        QMetaObject.connectSlotsByName(snapshot_wizard)
    # setupUi

    def retranslateUi(self, snapshot_wizard):
        snapshot_wizard.setWindowTitle(QCoreApplication.translate("snapshot_wizard", u"\u5feb\u7167\u5411\u5bfc", None))
        self.btn_add_file.setText(QCoreApplication.translate("snapshot_wizard", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_add_folder.setText(QCoreApplication.translate("snapshot_wizard", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.lineedit_filter.setPlaceholderText(QCoreApplication.translate("snapshot_wizard", u"\u5728\u6b64\u952e\u5165\u7b5b\u9009\u540e\u7f00\u540d \u5982 jpg,png", None))
        self.label_hidden.setText(QCoreApplication.translate("snapshot_wizard", u"\u6392\u9664\u9690\u85cf\uff1a", None))
#if QT_CONFIG(tooltip)
        self.toggle_windows.setToolTip(QCoreApplication.translate("snapshot_wizard", u"\u6392\u9664Windows\u7cfb\u7edf\u4e0a\u7684\u9690\u85cf\u6587\u4ef6\u4e0e\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.toggle_unix.setToolTip(QCoreApplication.translate("snapshot_wizard", u"\u6392\u9664Unix\u7c7b\u7cfb\u7edf\uff08Linux/Android/MacOS\uff09\u4e0a\u7684\u9690\u85cf\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.TreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("snapshot_wizard", u"\u8def\u5f84", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("snapshot_wizard", u"\u540d\u79f0", None));
        self.label_count.setText(QCoreApplication.translate("snapshot_wizard", u"\u6587\u4ef6\u603b\u6570\uff1a", None))
        self.label_count_data.setText(QCoreApplication.translate("snapshot_wizard", u"0", None))
#if QT_CONFIG(tooltip)
        self.ckb_calc_hash.setToolTip(QCoreApplication.translate("snapshot_wizard", u"\u5efa\u8bae\u52fe\u9009\uff0c\u53ef\u7528\u4e8e\u9a8c\u8bc1\u6587\u4ef6\u662f\u5426\u88ab\u4fee\u6539\u6216\u538b\u7f29\uff0c\u53d6\u6d88\u52fe\u9009\u540e\u5c06\u53ea\u8bb0\u5f55\u6587\u4ef6\u540d\n"
"\u4ec5\u5728\u6587\u4ef6\u5b58\u5728\u4e91\u7aef\u4e0d\u65b9\u4fbf\u4e0b\u8f7d\u65f6\u53d6\u6d88\u52fe\u9009", None))
#endif // QT_CONFIG(tooltip)
        self.ckb_calc_hash.setText(QCoreApplication.translate("snapshot_wizard", u"\u8ba1\u7b97\u6587\u4ef6\u54c8\u5e0c/\u751f\u6210\u7f29\u7565\u56fe", None))
        self.btn_cancel.setText(QCoreApplication.translate("snapshot_wizard", u"\u53d6\u6d88", None))
        self.btn_create.setText(QCoreApplication.translate("snapshot_wizard", u"\u521b\u5efa\u5feb\u7167", None))
    # retranslateUi

