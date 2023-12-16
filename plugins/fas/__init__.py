from PySide6.QtGui import *
import PySide6.QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from qfluentwidgets import *

from sl_lib import *

from .fas_ui import Ui_fas
from .task_edit_ui import Ui_task_edit


class FAS(QWidget, Ui_fas):
    '''file auto sync'''

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)

        self.subwin_taskedit = TaskEdit(mainwindow)
        self.mainwindow=mainwindow

        self.signal_connect()
        self.init_icon()

    def signal_connect(self):
        self.btn_add.clicked.connect(self.subwin_taskedit.show)

    def init_icon(self):
        self.btn_add.setIcon(FluentIcon.ADD)
        self.btn_del.setIcon(FluentIcon.DELETE)

    def protect_table(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.item(i, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled |
                                                 Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.tableWidget.item(i, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled |
                                                 Qt.ItemIsEditable | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.tableWidget.item(i, 2).setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled |
                                                 Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    
        
        

class TaskEdit(FluentWindow, Ui_task_edit):
    '''task edit'''

    def __init__(self, mainwindow: FluentWindow):
        super().__init__()
        self.container = QWidget()
        self.setupUi(self.container)
        self.addSubInterface(
            self.container, mainwindow.windowIcon(), mainwindow.windowTitle())
        self.setWindowIcon(mainwindow.windowIcon())
        self.setWindowTitle('任务编辑')
        self.mainwindow = mainwindow
        self.navigationInterface.setVisible(False)
        self.signal_connect()
        self.init_widget()

        self.setAcceptDrops(True)

    def show(self):
        self.resize(600, 300)
        super().show()
        self.mainwindow.hide()

    def signal_connect(self):
        self.btn_save.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)
        self.btn_src_del.clicked.connect(lambda:self.listwidget_src.removeItemWidget(self.listwidget_src.selectedItems()[0]))
        
    def init_widget(self):
        self.ckb_include_later.setOnText('包含之后增加的文件')
        self.ckb_include_later.setOffText('包含之后增加的文件')

        self.btn_save.setIcon(FluentIcon.SAVE)
        self.btn_cancel.setIcon(FluentIcon.CANCEL)
        self.btn_src_add.setIcon(FluentIcon.ADD)
        self.btn_src_del.setIcon(FluentIcon.DELETE)
        self.btn_select_dst_path.setIcon(FluentIcon.FOLDER)

        # self.timeedit_interval.setTime(QTime(1,0))

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QDropEvent):
        files=[i.toLocalFile() for i in event.mimeData().urls()]
        sltk.unique_add_items(self.listwidget_src,files)
        ListWidget.remove

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        event.accept()

    def hideEvent(self, event):
        self.mainwindow.show()
        super().hide()
        
    def closeEvent(self, event):
        self.hide()
        
        event.ignore()
