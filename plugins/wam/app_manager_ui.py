# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, PrimaryPushButton, PushButton, SplitPushButton,
    TableWidget, ToolButton)

class Ui_app_manager(object):
    def setupUi(self, app_manager):
        if not app_manager.objectName():
            app_manager.setObjectName(u"app_manager")
        app_manager.resize(750, 500)
        self.verticalLayout = QVBoxLayout(app_manager)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_install_folder = QLabel(app_manager)
        self.label_install_folder.setObjectName(u"label_install_folder")

        self.horizontalLayout.addWidget(self.label_install_folder)

        self.cmb_folder = ComboBox(app_manager)
        self.cmb_folder.setObjectName(u"cmb_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_folder.sizePolicy().hasHeightForWidth())
        self.cmb_folder.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cmb_folder)

        self.btn_refresh = ToolButton(app_manager)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.btn_add_folder = ToolButton(app_manager)
        self.btn_add_folder.setObjectName(u"btn_add_folder")

        self.horizontalLayout.addWidget(self.btn_add_folder)

        self.btn_del_folder = ToolButton(app_manager)
        self.btn_del_folder.setObjectName(u"btn_del_folder")
        self.btn_del_folder.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_del_folder)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.table_app_info = TableWidget(app_manager)
        if (self.table_app_info.columnCount() < 7):
            self.table_app_info.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_app_info.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_app_info.setObjectName(u"table_app_info")
        self.table_app_info.setDragEnabled(True)
        self.table_app_info.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_app_info.setSortingEnabled(True)
        self.table_app_info.horizontalHeader().setCascadingSectionResizes(True)
        self.table_app_info.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_app_info)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_open_folder = PushButton(app_manager)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        self.btn_open_folder.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btn_open_folder)

        self.btn_open_reg = SplitPushButton(app_manager)
        self.btn_open_reg.setObjectName(u"btn_open_reg")

        self.horizontalLayout_4.addWidget(self.btn_open_reg)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_backup = PrimaryPushButton(app_manager)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_backup)

        self.btn_restore = PushButton(app_manager)
        self.btn_restore.setObjectName(u"btn_restore")

        self.horizontalLayout_3.addWidget(self.btn_restore)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(app_manager)

        QMetaObject.connectSlotsByName(app_manager)
    # setupUi

    def retranslateUi(self, app_manager):
        app_manager.setWindowTitle(QCoreApplication.translate("app_manager", u"Form", None))
        self.label_install_folder.setText(QCoreApplication.translate("app_manager", u"\u5e94\u7528\u5b89\u88c5\u4f4d\u7f6e\uff1a", None))
        ___qtablewidgetitem = self.table_app_info.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("app_manager", u"\u5e94\u7528\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.table_app_info.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("app_manager", u"\u7248\u672c", None));
        ___qtablewidgetitem2 = self.table_app_info.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("app_manager", u"\u8def\u5f84", None));
        ___qtablewidgetitem3 = self.table_app_info.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("app_manager", u"\u5b89\u88c5\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.table_app_info.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("app_manager", u"\u5360\u7528\u7a7a\u95f4", None));
        ___qtablewidgetitem5 = self.table_app_info.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("app_manager", u"\u5b89\u88c5\u7c7b\u578b", None));
        ___qtablewidgetitem6 = self.table_app_info.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("app_manager", u"\u72b6\u6001", None));
        self.btn_open_folder.setText(QCoreApplication.translate("app_manager", u"\u6253\u5f00\u8f6f\u4ef6\u76ee\u5f55", None))
        self.btn_open_reg.setProperty(u"text_", QCoreApplication.translate("app_manager", u"\u6253\u5f00\u5168\u5c40\u5e94\u7528\u6ce8\u518c\u8868", None))
        self.btn_backup.setText(QCoreApplication.translate("app_manager", u"\u5907\u4efd", None))
        self.btn_restore.setText(QCoreApplication.translate("app_manager", u"\u6062\u590d", None))
    # retranslateUi

