import os
import logging
import zipfile

from qfluentwidgets import *
from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


from input_dialog_ui import Ui_Input_dialog


class sltk:
    "神龙工具集"

    def scan_file(dir_name: str, goal: str, depth: int, black_list: list[str] = ['C:\\Windows', 'C:\\$RECYCLE.BIN', 'C:\\Recovery', 'C:\\System Volume Information', 'D:\\$RECYCLE.BIN', 'D:\\System Volume Information']) -> list[str]:
        """
        Find the goal in the given dir.
        Return mutiple results if found.

        argvs:
            dir: The location to scan.
            goal: The file to be found.
            depth: Decide how many folders to be scan.  1 means no child folder is scaned
            black_list: Jump through to save time

        e.g. scan_file('C:\\ ','python.exe',5)
        >>> ["C:\\user\\abcdesteve\\python\\python.exe","C:\\python\\python.exe"]
        """
        results = []
        if os.path.isdir(dir_name) and depth > 0 and dir_name not in black_list:
            try:
                lis = os.listdir(dir_name)
                if goal in lis:
                    results.append(sltk.join_path(dir_name, goal))
                temp = [
                    results.extend(
                        sltk.scan_file(sltk.join_path(
                            dir_name, i), goal, depth - 1)
                    )
                    for i in lis
                    if os.path.isdir(sltk.join_path(dir_name, i))
                ]
                # print(f'temp:{temp}')
                return results
            except PermissionError:
                logging.warning(
                    f"Not enough permission when trying to scan dir: {dir_name}")
                return []
        else:
            return []

    def safe_load(self, origin: dict[str, str | dict], data: dict[str, str | dict]) -> dict[str, str | dict]:
        '''安全加载json配置，避免因版本不同导致配置冲突'''
        for okey, ovalue in origin.items():
            if okey in list(data.keys()):
                if type(ovalue) == dict:
                    origin[okey] = self.safe_load(sltk, ovalue, data[okey])
                else:
                    origin[okey] = data[okey]
        return origin

    def unique_add_items(widget: QComboBox | ComboBox | QListWidget | ListWidget, *items: str | list[str], format_item: bool = True):
        '''为ComboBox不重复地添加一个或多个item，同时格式化路径（如果可以）'''
        previous_items = [(widget.itemText(i) if type(widget) in [
                           QComboBox, ComboBox]else widget.item(i).text()) for i in range(widget.count())]
        if type(items[0]) == list:
            items = items[0]
        for i in items:
            if format_item:
                i = os.path.realpath(i)
            if i not in previous_items:
                widget.addItem(i)

    def unique_set_items(widget: QComboBox | ComboBox, *items: str | list[str], format_item: bool = True):
        '''先清空ComboBox，再运行 `sltk.unique_add_items` ，并尝试恢复原来的选项'''
        previous_txt = widget.currentText()
        widget.clear()
        sltk.unique_add_items(widget, *items, format_item=format_item)
        lis = sltk.expend_children_text(widget)
        if previous_txt in lis:
            widget.setCurrentText(previous_txt)
        else:
            widget.setCurrentIndex(0)

    def file_get_root_items(file: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
        '''
        Return all files and dirs in the root folder\n
        `[a.txt, b, b/a.txt]`  
        >>> [a.txt, b]
        '''
        root_count: list[zipfile.ZipInfo] = []
        for i in file.infolist():
            if i.filename.removesuffix('/').count('/') == 0 and i.is_dir():
                root_count.append(i)
        return root_count

    def smart_extract(file: zipfile.ZipFile, dst: str):
        root = sltk.file_get_root_items(file)
        if len(root) == 1:
            results = []
            for i in file.namelist():
                temp = root[0].filename
                if i.startswith(temp) and i != temp:
                    file.extract(i, os.path.dirname(dst))
        else:
            file.extractall(dst)

    def join_path(*argv: str) -> str:
        return os.path.realpath(os.path.join(*argv))

    def expend_children_text(widget: QComboBox | QListWidget | QTableWidget | QTreeWidget | ComboBox | ListWidget | TableWidget | TreeWidget) -> list[str]:
        '''
        Return all item text in the widget\n
        `ComboBox` -> list[str]\n
        `ListWidget` -> list[str]\n
        `TableWidget` -> list[list[str]]\n
        `TreeWidget` -> list[str]
        '''
        # if type(widget) in [QComboBox, ComboBox]:
        if isinstance(widget, (QComboBox, ComboBox, EditableComboBox)):
            return [widget.itemText(i) for i in range(widget.count())]

        # elif type(widget) in [QListWidget, ListWidget]:
        elif isinstance(widget, (QListWidget, ListWidget)):
            return [widget.item(i)for i in range(widget.count())]

        # elif type(widget) in [QTableWidget, TableWidget,]:
        elif isinstance(widget, (QTableWidget, TableWidget)):
            return [
                [widget.item(row, col).text()
                 for col in range(widget.columnCount())]
                for row in range(widget.rowCount())]

        # elif type(widget) in [QTreeWidget, TreeWidget]:
        elif isinstance(widget, (QTreeWidget, TreeWidget)):
            return [widget.topLevelItem(i).text(0) for i in range(widget.topLevelItemCount())]
        else:
            raise TypeError(f'Unsupported widget type: {type(widget)}')


class QMessageBox:
    """
    窗口类型支持 `information` | `warning` | `question`

    `mask` 指定窗口是否有遮罩
    """

    Yes = True
    No = False

    def base(parent, title, content, mask=False):
        if mask:
            widget = MessageBox(title, content, parent)
        else:
            # Dialog不支持圆角
            widget = Dialog(title, content, parent)
            widget.setTitleBarVisible(False)
            # MessageBox不支持关闭遮罩
            # widget = MessageBox(title, content, parent)
            # widget.clearMask()

        widget.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        return widget

    def information(parent: QMainWindow, title, content, mask=True, text='OK') -> None:
        widget = QMessageBox.base(parent, title, content, mask)

        widget.cancelButton.hide()

        widget.yesButton.setShortcut('alt+y')
        widget.yesButton.setText(text)

        widget.exec()

    def warning(parent: QMainWindow, title, content, mask=True, text='OK') -> None:
        widget = QMessageBox.base(parent, title, content, mask)

        # widget.yesButton.setStyleSheet('color:#ff0000')
        logging.debug("unfinished")
        widget.cancelButton.hide()

        widget.yesButton.setShortcut('alt+y')
        widget.yesButton.setText(text)

        widget.exec()

    def question(parent: QMainWindow, title, content, mask=True, yes_text='继续', no_text='取消') -> bool:
        widget = QMessageBox.base(parent, title, content, mask)

        widget.yesButton.setShortcut('alt+y')
        widget.cancelButton.setShortcut('alt+n')
        widget.yesButton.setText(yes_text)
        widget.cancelButton.setText(no_text)

        return QMessageBox.Yes if widget.exec() else QMessageBox.No


class InputDialog(MaskDialogBase, Ui_Input_dialog):
    def __init__(self):
        pass

    def run(self, parent, title: str, content: str, options: list[str] = [], editable: bool = True) -> str:
        '''
        Receive an optional argv `options` which will be shown in the `ComboBox`\n
        Return input txt
        '''
        super().__init__(parent)
        self.setupUi(self.widget)
        self.widget.setFixedSize(360, 220)
        FluentStyleSheet.DIALOG.apply(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.btn_cancel.setShortcut('Alt+N')
        self.btn_ok.setShortcut('Alt+Y')
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_ok.clicked.connect(self.ok)
        self.title.setText(title)
        self.content.setText(content)
        sltk.unique_add_items(self.comboBox, options, format_item=False)
        self.comboBox.setReadOnly(not editable)
        # self.show()
        self.exec()
        return self.comboBox.currentText() if self.status else None

    def cancel(self):
        self.status = False
        self.close()

    def ok(self):
        self.status = True
        self.close()

    # def closeEvent(self, arg: QCloseEvent):
    #     self.done(1)

    # def keyPressEvent(self, event: QKeyEvent):
    #     if event.key() in [Qt.Key.Key_Enter, Qt.Key.Key_Return]:
    #         self.close()


class StatisticsWidget(QWidget):
    """ 状态数值对应组件 """

    def __init__(self, title: str, value: str = '未知', parent=None):
        super().__init__(parent=parent)
        self.titleLabel = CaptionLabel(title, self)
        self.valueLabel = BodyLabel(value, self)
        self.vBoxLayout = QVBoxLayout(self)

        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.valueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vBoxLayout.setContentsMargins(16, 0, 16, 0)
        self.vBoxLayout.addWidget(self.valueLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignBottom)

        setFont(self.valueLabel, 18, QFont.DemiBold)
        self.titleLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))

    def setTitle(self, title: str = ''):
        self.titleLabel.setText(str(title))

    def setValue(self, value: str = '未知'):
        self.valueLabel.setText(str(value))


class MyFluentIcon(FluentIconBase, Enum):
    ToolBox = 'toolbox'
    Sheild = 'shield'
    Android = 'android'
    Frigid = 'frigid'
    UnFrigid = 'unfrigid'

    def path(self, theme=Theme.AUTO) -> str:
        return sltk.join_path(os.path.dirname(__file__), 'icons', f'{self.value}_{getIconColor(theme)}.svg')
        # return f'{os.path.dirname(__file__)}icons/{self.value}'
