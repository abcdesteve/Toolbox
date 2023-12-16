# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidgetItem,
    QSizePolicy, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, ListWidget, PrimaryPushButton, PushButton,
    RadioButton, SwitchButton, TimePicker)

class Ui_task_edit(object):
    def setupUi(self, task_edit):
        if not task_edit.objectName():
            task_edit.setObjectName(u"task_edit")
        task_edit.resize(600, 438)
        self.verticalLayout = QVBoxLayout(task_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_type = QLabel(task_edit)
        self.label_type.setObjectName(u"label_type")

        self.horizontalLayout.addWidget(self.label_type)

        self.radio_type_single = RadioButton(task_edit)
        self.btngp_sync_type = QButtonGroup(task_edit)
        self.btngp_sync_type.setObjectName(u"btngp_sync_type")
        self.btngp_sync_type.addButton(self.radio_type_single)
        self.radio_type_single.setObjectName(u"radio_type_single")
        self.radio_type_single.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_type_single)

        self.radio_type_double = RadioButton(task_edit)
        self.btngp_sync_type.addButton(self.radio_type_double)
        self.radio_type_double.setObjectName(u"radio_type_double")

        self.horizontalLayout.addWidget(self.radio_type_double)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter_3 = QSplitter(task_edit)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.grpbox_src = QGroupBox(self.splitter_2)
        self.grpbox_src.setObjectName(u"grpbox_src")
        self.gridLayout = QGridLayout(self.grpbox_src)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listwidget_src = ListWidget(self.grpbox_src)
        self.listwidget_src.setObjectName(u"listwidget_src")

        self.gridLayout.addWidget(self.listwidget_src, 0, 0, 1, 2)

        self.btn_src_del = PushButton(self.grpbox_src)
        self.btn_src_del.setObjectName(u"btn_src_del")

        self.gridLayout.addWidget(self.btn_src_del, 1, 0, 1, 1)

        self.btn_src_add = PrimaryPushButton(self.grpbox_src)
        self.btn_src_add.setObjectName(u"btn_src_add")

        self.gridLayout.addWidget(self.btn_src_add, 1, 1, 1, 1)

        self.splitter_2.addWidget(self.grpbox_src)
        self.grpbox_dst = QGroupBox(self.splitter_2)
        self.grpbox_dst.setObjectName(u"grpbox_dst")
        self.horizontalLayout_2 = QHBoxLayout(self.grpbox_dst)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_select_dst_path = PushButton(self.grpbox_dst)
        self.btn_select_dst_path.setObjectName(u"btn_select_dst_path")

        self.horizontalLayout_2.addWidget(self.btn_select_dst_path)

        self.lineedit_dst_path = LineEdit(self.grpbox_dst)
        self.lineedit_dst_path.setObjectName(u"lineedit_dst_path")

        self.horizontalLayout_2.addWidget(self.lineedit_dst_path)

        self.splitter_2.addWidget(self.grpbox_dst)
        self.splitter_3.addWidget(self.splitter_2)
        self.line = QFrame(self.splitter_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.splitter_3.addWidget(self.line)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.grpbox_task = QGroupBox(self.splitter)
        self.grpbox_task.setObjectName(u"grpbox_task")
        self.verticalLayout_2 = QVBoxLayout(self.grpbox_task)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_interval = QLabel(self.grpbox_task)
        self.label_interval.setObjectName(u"label_interval")

        self.horizontalLayout_4.addWidget(self.label_interval)

        self.timeedit_interval = TimePicker(self.grpbox_task)
        self.timeedit_interval.setObjectName(u"timeedit_interval")

        self.horizontalLayout_4.addWidget(self.timeedit_interval)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_repeat = QLabel(self.grpbox_task)
        self.label_repeat.setObjectName(u"label_repeat")

        self.horizontalLayout_5.addWidget(self.label_repeat)

        self.radio_repeat_replace = RadioButton(self.grpbox_task)
        self.btngp_repeat_file = QButtonGroup(task_edit)
        self.btngp_repeat_file.setObjectName(u"btngp_repeat_file")
        self.btngp_repeat_file.addButton(self.radio_repeat_replace)
        self.radio_repeat_replace.setObjectName(u"radio_repeat_replace")

        self.horizontalLayout_5.addWidget(self.radio_repeat_replace)

        self.radio_repeat_ask = RadioButton(self.grpbox_task)
        self.btngp_repeat_file.addButton(self.radio_repeat_ask)
        self.radio_repeat_ask.setObjectName(u"radio_repeat_ask")
        self.radio_repeat_ask.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radio_repeat_ask)

        self.radio_repeat_ignore = RadioButton(self.grpbox_task)
        self.btngp_repeat_file.addButton(self.radio_repeat_ignore)
        self.radio_repeat_ignore.setObjectName(u"radio_repeat_ignore")

        self.horizontalLayout_5.addWidget(self.radio_repeat_ignore)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_show_result = QLabel(self.grpbox_task)
        self.label_show_result.setObjectName(u"label_show_result")

        self.horizontalLayout_6.addWidget(self.label_show_result)

        self.radio_show_result_error = RadioButton(self.grpbox_task)
        self.btngp_show_result = QButtonGroup(task_edit)
        self.btngp_show_result.setObjectName(u"btngp_show_result")
        self.btngp_show_result.addButton(self.radio_show_result_error)
        self.radio_show_result_error.setObjectName(u"radio_show_result_error")

        self.horizontalLayout_6.addWidget(self.radio_show_result_error)

        self.radio_show_result_always = RadioButton(self.grpbox_task)
        self.btngp_show_result.addButton(self.radio_show_result_always)
        self.radio_show_result_always.setObjectName(u"radio_show_result_always")
        self.radio_show_result_always.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radio_show_result_always)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.splitter.addWidget(self.grpbox_task)
        self.grpbox_file = QGroupBox(self.splitter)
        self.grpbox_file.setObjectName(u"grpbox_file")
        self.gridLayout_2 = QGridLayout(self.grpbox_file)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_file_count = QLabel(self.grpbox_file)
        self.label_file_count.setObjectName(u"label_file_count")

        self.gridLayout_2.addWidget(self.label_file_count, 0, 0, 1, 1)

        self.label_file_count_value = QLabel(self.grpbox_file)
        self.label_file_count_value.setObjectName(u"label_file_count_value")
        font = QFont()
        font.setBold(True)
        self.label_file_count_value.setFont(font)
        self.label_file_count_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_file_count_value, 0, 1, 1, 1)

        self.label_size_count = QLabel(self.grpbox_file)
        self.label_size_count.setObjectName(u"label_size_count")

        self.gridLayout_2.addWidget(self.label_size_count, 1, 0, 1, 1)

        self.label_size_count_value = QLabel(self.grpbox_file)
        self.label_size_count_value.setObjectName(u"label_size_count_value")
        self.label_size_count_value.setFont(font)
        self.label_size_count_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_size_count_value, 1, 1, 1, 1)

        self.ckb_include_later = SwitchButton(self.grpbox_file)
        self.ckb_include_later.setObjectName(u"ckb_include_later")
        self.ckb_include_later.setEnabled(False)

        self.gridLayout_2.addWidget(self.ckb_include_later, 2, 0, 1, 2)

        self.splitter.addWidget(self.grpbox_file)
        self.splitter_3.addWidget(self.splitter)

        self.verticalLayout.addWidget(self.splitter_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_cancel = PushButton(task_edit)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_8.addWidget(self.btn_cancel)

        self.btn_save = PrimaryPushButton(task_edit)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(task_edit)

        QMetaObject.connectSlotsByName(task_edit)
    # setupUi

    def retranslateUi(self, task_edit):
        task_edit.setWindowTitle(QCoreApplication.translate("task_edit", u"\u4efb\u52a1\u7f16\u8f91", None))
        self.label_type.setText(QCoreApplication.translate("task_edit", u"\u6587\u4ef6\u590d\u5236\u65b9\u5411\uff1a", None))
        self.radio_type_single.setText(QCoreApplication.translate("task_edit", u"\u5355\u5411", None))
        self.radio_type_double.setText(QCoreApplication.translate("task_edit", u"\u53cc\u5411", None))
        self.grpbox_src.setTitle(QCoreApplication.translate("task_edit", u"\u6587\u4ef6\u6e90", None))
        self.btn_src_del.setText(QCoreApplication.translate("task_edit", u"\u5220\u9664", None))
        self.btn_src_del.setProperty("lightCustomQss", QCoreApplication.translate("task_edit", u"PushButton{background-color:#e81123;}\n"
"PushButton:hover{background-color:#e63342;}", None))
        self.btn_src_del.setProperty("darkCustomQss", QCoreApplication.translate("task_edit", u"PushButton{background-color:#e81123;}\n"
"PushButton:hover{background-color:#e63342;}", None))
        self.btn_src_add.setText(QCoreApplication.translate("task_edit", u"\u6dfb\u52a0", None))
        self.grpbox_dst.setTitle(QCoreApplication.translate("task_edit", u"\u76ee\u6807\u8def\u5f84", None))
        self.btn_select_dst_path.setText(QCoreApplication.translate("task_edit", u"\u9009\u62e9\u8def\u5f84", None))
        self.grpbox_task.setTitle(QCoreApplication.translate("task_edit", u"\u4efb\u52a1\u5c5e\u6027", None))
        self.label_interval.setText(QCoreApplication.translate("task_edit", u"\u6267\u884c\u95f4\u9694\uff1a", None))
        self.label_repeat.setText(QCoreApplication.translate("task_edit", u"\u91cd\u590d\u6587\u4ef6\uff1a", None))
        self.radio_repeat_replace.setText(QCoreApplication.translate("task_edit", u"\u66ff\u6362", None))
        self.radio_repeat_ask.setText(QCoreApplication.translate("task_edit", u"\u8be2\u95ee", None))
        self.radio_repeat_ignore.setText(QCoreApplication.translate("task_edit", u"\u8df3\u8fc7", None))
        self.label_show_result.setText(QCoreApplication.translate("task_edit", u"\u6267\u884c\u540e\u5f39\u51fa\u8fd0\u884c\u7ed3\u679c\uff1a", None))
        self.radio_show_result_error.setText(QCoreApplication.translate("task_edit", u"\u4ec5\u9519\u8bef", None))
        self.radio_show_result_always.setText(QCoreApplication.translate("task_edit", u"\u59cb\u7ec8", None))
        self.grpbox_file.setTitle(QCoreApplication.translate("task_edit", u"\u6587\u4ef6/\u6587\u4ef6\u5939\u5c5e\u6027", None))
        self.label_file_count.setText(QCoreApplication.translate("task_edit", u"\u6587\u4ef6\u6570\uff1a", None))
        self.label_file_count_value.setText(QCoreApplication.translate("task_edit", u"\u672a\u77e5", None))
        self.label_size_count.setText(QCoreApplication.translate("task_edit", u"\u6587\u4ef6\u603b\u5927\u5c0f\uff1a", None))
        self.label_size_count_value.setText(QCoreApplication.translate("task_edit", u"\u672a\u77e5", None))
        self.ckb_include_later.setText(QCoreApplication.translate("task_edit", u"\u5305\u542b\u4e4b\u540e\u589e\u52a0\u7684\u6587\u4ef6", None))
        self.btn_cancel.setText(QCoreApplication.translate("task_edit", u"\u53d6\u6d88", None))
        self.btn_save.setText(QCoreApplication.translate("task_edit", u"\u4fdd\u5b58", None))
    # retranslateUi

