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

from qfluentwidgets import (CheckBox, PrimaryPushButton, PushButton, ToolButton,
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

        self.horizontalLayout_2.addWidget(self.btn_del)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.TreeWidget = TreeWidget(snapshot_wizard)
        self.TreeWidget.setObjectName(u"TreeWidget")
        self.TreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.TreeWidget.setTabKeyNavigation(True)
        self.TreeWidget.setAlternatingRowColors(True)
        self.TreeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.TreeWidget.setUniformRowHeights(True)
        self.TreeWidget.setAnimated(True)
        self.TreeWidget.header().setHighlightSections(True)
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

        self.horizontalLayout_3.addWidget(self.btn_create)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(snapshot_wizard)

        QMetaObject.connectSlotsByName(snapshot_wizard)
    # setupUi

    def retranslateUi(self, snapshot_wizard):
        snapshot_wizard.setWindowTitle(QCoreApplication.translate("snapshot_wizard", u"\u5feb\u7167\u5411\u5bfc", None))
        self.btn_add_file.setText(QCoreApplication.translate("snapshot_wizard", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_add_folder.setText(QCoreApplication.translate("snapshot_wizard", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        ___qtreewidgetitem = self.TreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("snapshot_wizard", u"\u6587\u4ef6\u5939", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("snapshot_wizard", u"\u8def\u5f84", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("snapshot_wizard", u"\u540d\u79f0", None));
        self.label_count.setText(QCoreApplication.translate("snapshot_wizard", u"\u6587\u4ef6\u603b\u6570\uff1a", None))
        self.label_count_data.setText(QCoreApplication.translate("snapshot_wizard", u"0", None))
#if QT_CONFIG(tooltip)
        self.ckb_calc_hash.setToolTip(QCoreApplication.translate("snapshot_wizard", u"\u5efa\u8bae\u52fe\u9009\uff0c\u53ef\u7528\u4e8e\u9a8c\u8bc1\u6587\u4ef6\u662f\u5426\u88ab\u4fee\u6539\u6216\u538b\u7f29\uff0c\u53d6\u6d88\u52fe\u9009\u540e\u5c06\u53ea\u8bb0\u5f55\u6587\u4ef6\u540d\n"
"\u4ec5\u5728\u6587\u4ef6\u5b58\u5728\u4e91\u7aef\u4e0d\u65b9\u4fbf\u4e0b\u8f7d\u65f6\u53d6\u6d88\u52fe\u9009", None))
#endif // QT_CONFIG(tooltip)
        self.ckb_calc_hash.setText(QCoreApplication.translate("snapshot_wizard", u"\u8ba1\u7b97\u6587\u4ef6\u54c8\u5e0c", None))
        self.btn_cancel.setText(QCoreApplication.translate("snapshot_wizard", u"\u53d6\u6d88", None))
        self.btn_create.setText(QCoreApplication.translate("snapshot_wizard", u"\u521b\u5efa\u5feb\u7167", None))
    # retranslateUi

