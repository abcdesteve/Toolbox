from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qfluentwidgets.common.icon import FluentIcon

from .fsa_ui import Ui_fsa

class FSA(QWidget,Ui_fsa):
    """文件快照归档\nfile snapshot archive"""
    def __init__(self,mainwindow):
        super().__init__()
        self.setupUi(self)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_crt_snap.setIcon(FluentIcon.CAMERA)
        self.btn_del_snap.setIcon(FluentIcon.DELETE)
        self.btn_export_snap.setIcon(FluentIcon.SHARE)
        # 不知道为啥全局设定无效，必须在这里设置
        # ScrollArea的背景在scrollAreaWidgetContents里
        self.setStyleSheet("QWidget#scrollAreaWidgetContents {background-color:transparent}")

        self.mainwindow = mainwindow
        self.init_signal()

    def init_signal(self):
        pass