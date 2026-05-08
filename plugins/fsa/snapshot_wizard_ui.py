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

from qfluentwidgets import (LineEdit, Pivot, PrimaryPushButton, PushButton,
    SegmentedToolWidget, ToggleToolButton, ToolButton, TreeWidget)

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
        self.switch_filter = SegmentedToolWidget(snapshot_wizard)
        self.switch_filter.setObjectName(u"switch_filter")
        self.switch_filter.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.switch_filter)

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

        self.label = QLabel(snapshot_wizard)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.switch_scan_mode = SegmentedToolWidget(snapshot_wizard)
        self.switch_scan_mode.setObjectName(u"switch_scan_mode")
        self.switch_scan_mode.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.switch_scan_mode)


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
        QWidget.setTabOrder(self.TreeWidget, self.btn_cancel)
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
        self.label.setText(QCoreApplication.translate("snapshot_wizard", u"\u626b\u63cf\u6a21\u5f0f\uff1a", None))
        self.btn_cancel.setText(QCoreApplication.translate("snapshot_wizard", u"\u53d6\u6d88", None))
        self.btn_create.setText(QCoreApplication.translate("snapshot_wizard", u"\u521b\u5efa\u5feb\u7167", None))
    # retranslateUi

