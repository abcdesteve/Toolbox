# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'snapshot_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QSplitter,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (HorizontalSeparator, ImageLabel, PushButton, TreeWidget)

class Ui_snapshot_viewer(object):
    def setupUi(self, snapshot_viewer):
        if not snapshot_viewer.objectName():
            snapshot_viewer.setObjectName(u"snapshot_viewer")
        snapshot_viewer.resize(800, 500)
        self.horizontalLayout_15 = QHBoxLayout(snapshot_viewer)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(snapshot_viewer)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 8, 5, 8)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.vbox_add = QVBoxLayout()
        self.vbox_add.setObjectName(u"vbox_add")
        self.label_title_add = QLabel(self.layoutWidget)
        self.label_title_add.setObjectName(u"label_title_add")
        font = QFont()
        font.setPointSize(10)
        self.label_title_add.setFont(font)
        self.label_title_add.setAlignment(Qt.AlignCenter)

        self.vbox_add.addWidget(self.label_title_add)

        self.TreeWidget_add = TreeWidget(self.layoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.TreeWidget_add.setHeaderItem(__qtreewidgetitem)
        self.TreeWidget_add.setObjectName(u"TreeWidget_add")
        self.TreeWidget_add.setAlternatingRowColors(True)
        self.TreeWidget_add.setUniformRowHeights(True)
        self.TreeWidget_add.setAnimated(True)
        self.TreeWidget_add.setHeaderHidden(True)

        self.vbox_add.addWidget(self.TreeWidget_add)


        self.horizontalLayout_13.addLayout(self.vbox_add)

        self.vbox_mod = QVBoxLayout()
        self.vbox_mod.setObjectName(u"vbox_mod")
        self.label_title_mod = QLabel(self.layoutWidget)
        self.label_title_mod.setObjectName(u"label_title_mod")
        self.label_title_mod.setFont(font)
        self.label_title_mod.setAlignment(Qt.AlignCenter)

        self.vbox_mod.addWidget(self.label_title_mod)

        self.TreeWidget_mod = TreeWidget(self.layoutWidget)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.TreeWidget_mod.setHeaderItem(__qtreewidgetitem1)
        self.TreeWidget_mod.setObjectName(u"TreeWidget_mod")
        self.TreeWidget_mod.setAlternatingRowColors(True)
        self.TreeWidget_mod.setUniformRowHeights(True)
        self.TreeWidget_mod.setAnimated(True)
        self.TreeWidget_mod.setHeaderHidden(True)

        self.vbox_mod.addWidget(self.TreeWidget_mod)


        self.horizontalLayout_13.addLayout(self.vbox_mod)

        self.vbox_del = QVBoxLayout()
        self.vbox_del.setObjectName(u"vbox_del")
        self.label_title_del = QLabel(self.layoutWidget)
        self.label_title_del.setObjectName(u"label_title_del")
        self.label_title_del.setFont(font)
        self.label_title_del.setAlignment(Qt.AlignCenter)

        self.vbox_del.addWidget(self.label_title_del)

        self.TreeWidget_del = TreeWidget(self.layoutWidget)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.TreeWidget_del.setHeaderItem(__qtreewidgetitem2)
        self.TreeWidget_del.setObjectName(u"TreeWidget_del")
        self.TreeWidget_del.setAlternatingRowColors(True)
        self.TreeWidget_del.setUniformRowHeights(True)
        self.TreeWidget_del.setAnimated(True)
        self.TreeWidget_del.setHeaderHidden(True)

        self.vbox_del.addWidget(self.TreeWidget_del)


        self.horizontalLayout_13.addLayout(self.vbox_del)

        self.vbox_move = QVBoxLayout()
        self.vbox_move.setObjectName(u"vbox_move")
        self.label_title_move = QLabel(self.layoutWidget)
        self.label_title_move.setObjectName(u"label_title_move")
        self.label_title_move.setFont(font)
        self.label_title_move.setAlignment(Qt.AlignCenter)

        self.vbox_move.addWidget(self.label_title_move)

        self.TreeWidget_move = TreeWidget(self.layoutWidget)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.TreeWidget_move.setHeaderItem(__qtreewidgetitem3)
        self.TreeWidget_move.setObjectName(u"TreeWidget_move")
        self.TreeWidget_move.setAlternatingRowColors(True)
        self.TreeWidget_move.setUniformRowHeights(True)
        self.TreeWidget_move.setAnimated(True)
        self.TreeWidget_move.setHeaderHidden(True)

        self.vbox_move.addWidget(self.TreeWidget_move)


        self.horizontalLayout_13.addLayout(self.vbox_move)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_return = PushButton(self.layoutWidget)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.btn_return)

        self.btn_show_gallery = PushButton(self.layoutWidget)
        self.btn_show_gallery.setObjectName(u"btn_show_gallery")
        self.btn_show_gallery.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_show_gallery)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.layoutWidget)
        self.info_panel = QFrame(self.splitter)
        self.info_panel.setObjectName(u"info_panel")
        self.info_panel.setStyleSheet(u"QFrame#info_panel{\n"
"	border-bottom-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.info_panel.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.info_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.ImageLabel = ImageLabel(self.info_panel)
        self.ImageLabel.setObjectName(u"ImageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.ImageLabel)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 100)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.label_file_path = QLabel(self.info_panel)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setAlignment(Qt.AlignCenter)
        self.label_file_path.setWordWrap(True)
        self.label_file_path.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_file_path)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_size = QLabel(self.info_panel)
        self.label_size.setObjectName(u"label_size")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_size.setFont(font1)

        self.horizontalLayout.addWidget(self.label_size)

        self.label_size_data = QLabel(self.info_panel)
        self.label_size_data.setObjectName(u"label_size_data")
        self.label_size_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_size_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_mtime = QLabel(self.info_panel)
        self.label_mtime.setObjectName(u"label_mtime")
        self.label_mtime.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_mtime)

        self.label_mtime_data = QLabel(self.info_panel)
        self.label_mtime_data.setObjectName(u"label_mtime_data")
        self.label_mtime_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_mtime_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.HorizontalSeparator = HorizontalSeparator(self.info_panel)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.verticalLayout_2.addWidget(self.HorizontalSeparator)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_md5 = QLabel(self.info_panel)
        self.label_md5.setObjectName(u"label_md5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_md5.sizePolicy().hasHeightForWidth())
        self.label_md5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_md5)

        self.label_md5_data = QLabel(self.info_panel)
        self.label_md5_data.setObjectName(u"label_md5_data")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_md5_data.sizePolicy().hasHeightForWidth())
        self.label_md5_data.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(True)
        self.label_md5_data.setFont(font2)
        self.label_md5_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_md5_data.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_md5_data)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_crc32 = QLabel(self.info_panel)
        self.label_crc32.setObjectName(u"label_crc32")
        sizePolicy1.setHeightForWidth(self.label_crc32.sizePolicy().hasHeightForWidth())
        self.label_crc32.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_crc32)

        self.label_crc32_data = QLabel(self.info_panel)
        self.label_crc32_data.setObjectName(u"label_crc32_data")
        sizePolicy2.setHeightForWidth(self.label_crc32_data.sizePolicy().hasHeightForWidth())
        self.label_crc32_data.setSizePolicy(sizePolicy2)
        self.label_crc32_data.setFont(font2)
        self.label_crc32_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_crc32_data.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_crc32_data)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_blake3 = QLabel(self.info_panel)
        self.label_blake3.setObjectName(u"label_blake3")
        sizePolicy1.setHeightForWidth(self.label_blake3.sizePolicy().hasHeightForWidth())
        self.label_blake3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_blake3)

        self.label_blake3_data = QLabel(self.info_panel)
        self.label_blake3_data.setObjectName(u"label_blake3_data")
        sizePolicy2.setHeightForWidth(self.label_blake3_data.sizePolicy().hasHeightForWidth())
        self.label_blake3_data.setSizePolicy(sizePolicy2)
        self.label_blake3_data.setFont(font2)
        self.label_blake3_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_blake3_data.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.label_blake3_data)

        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_sha1 = QLabel(self.info_panel)
        self.label_sha1.setObjectName(u"label_sha1")
        sizePolicy1.setHeightForWidth(self.label_sha1.sizePolicy().hasHeightForWidth())
        self.label_sha1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_sha1)

        self.label_sha1_data = QLabel(self.info_panel)
        self.label_sha1_data.setObjectName(u"label_sha1_data")
        sizePolicy2.setHeightForWidth(self.label_sha1_data.sizePolicy().hasHeightForWidth())
        self.label_sha1_data.setSizePolicy(sizePolicy2)
        self.label_sha1_data.setFont(font2)
        self.label_sha1_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_sha1_data.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_8.addWidget(self.label_sha1_data)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_sha256 = QLabel(self.info_panel)
        self.label_sha256.setObjectName(u"label_sha256")
        sizePolicy1.setHeightForWidth(self.label_sha256.sizePolicy().hasHeightForWidth())
        self.label_sha256.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.label_sha256)

        self.label_sha256_data = QLabel(self.info_panel)
        self.label_sha256_data.setObjectName(u"label_sha256_data")
        sizePolicy2.setHeightForWidth(self.label_sha256_data.sizePolicy().hasHeightForWidth())
        self.label_sha256_data.setSizePolicy(sizePolicy2)
        self.label_sha256_data.setFont(font2)
        self.label_sha256_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_sha256_data.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_9.addWidget(self.label_sha256_data)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalLayout_2.setStretch(1, 1)
        self.splitter.addWidget(self.info_panel)

        self.horizontalLayout_15.addWidget(self.splitter)


        self.retranslateUi(snapshot_viewer)

        QMetaObject.connectSlotsByName(snapshot_viewer)
    # setupUi

    def retranslateUi(self, snapshot_viewer):
        snapshot_viewer.setWindowTitle(QCoreApplication.translate("snapshot_viewer", u"Form", None))
        self.label_title_add.setText(QCoreApplication.translate("snapshot_viewer", u"\u65b0\u589e", None))
        self.label_title_mod.setText(QCoreApplication.translate("snapshot_viewer", u"\u4fee\u6539", None))
        self.label_title_del.setText(QCoreApplication.translate("snapshot_viewer", u"\u5220\u9664", None))
        self.label_title_move.setText(QCoreApplication.translate("snapshot_viewer", u"\u79fb\u52a8/\u91cd\u547d\u540d", None))
        self.btn_return.setText(QCoreApplication.translate("snapshot_viewer", u"\u8fd4\u56de", None))
        self.btn_show_gallery.setText(QCoreApplication.translate("snapshot_viewer", u"\u67e5\u770b\u7f29\u7565\u56fe\u5e93", None))
#if QT_CONFIG(accessibility)
        self.info_panel.setAccessibleDescription(QCoreApplication.translate("snapshot_viewer", u"right_info_panel", None))
#endif // QT_CONFIG(accessibility)
        self.label_file_path.setText("")
        self.label_size.setText(QCoreApplication.translate("snapshot_viewer", u"\u6587\u4ef6\u5927\u5c0f\uff1a", None))
        self.label_size_data.setText("")
        self.label_mtime.setText(QCoreApplication.translate("snapshot_viewer", u"\u4fee\u6539\u65f6\u95f4\uff1a", None))
        self.label_mtime_data.setText("")
        self.label_md5.setText(QCoreApplication.translate("snapshot_viewer", u"MD5:", None))
        self.label_crc32.setText(QCoreApplication.translate("snapshot_viewer", u"CRC32:", None))
        self.label_blake3.setText(QCoreApplication.translate("snapshot_viewer", u"BLAKE3:", None))
        self.label_sha1.setText(QCoreApplication.translate("snapshot_viewer", u"SHA1:", None))
        self.label_sha256.setText(QCoreApplication.translate("snapshot_viewer", u"SHA256:", None))
    # retranslateUi

