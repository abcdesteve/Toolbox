from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .fhc_ui import Ui_fhc

from sl_lib import QMessageBox, sltk

import os
import hashlib
import zlib
import blake3
import threading


class FHC(QWidget, Ui_fhc):
    '''文件哈希校验\nfile hash check'''

    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.setupUi(self)
        self.signal_connect()
        # self.tablewidget.setBorderVisible(True)
        # self.tablewidget.setBorderRadius(10)

    def signal_connect(self):
        self.btn_A.clicked.connect(lambda: self.select_file(self.lineedit_A))
        self.btn_B.clicked.connect(lambda: self.select_file(self.lineedit_B))
        self.lineedit_A.textChanged.connect(lambda: self.update_table_data('a'))
        self.lineedit_B.textChanged.connect(lambda: self.update_table_data('b'))
        self.tablewidget.currentCellChanged.connect(self.update_table_compare)

    def select_file(self, section: QLineEdit):
        # 为了键盘tab体验移除了按钮的焦点，现在不能靠焦点判断
        # section = self.lineedit_A if self.btn_A.hasFocus() else self.lineedit_B
        path = QFileDialog.getOpenFileName(self, '请选择文件')[0]
        if path:
            # with open(path, 'br')as file:
            #     section.setPlainText(str(file.read()))
            section.setPlainText('file:' + path)
        else:
            QMessageBox.warning(self.mainwindow, '警告', '路径无效')

    def set_result(self, txt: str, col: int):
        METHOD = [self.tablewidget.verticalHeaderItem(i).text() for i in range(self.tablewidget.rowCount())]
        
        # 清空要更新的列避免新旧数据重叠
        for i in range(self.tablewidget.rowCount()):
            self.tablewidget.setItem(i, col, QTableWidgetItem('' if i<2 else '计算中...'))
        if 'file:' in txt and os.path.isfile(filename := [i[5:] for i in txt.splitlines() if 'file:' in i][0]):
            try:
                count = 0
                with open(filename, 'r')as file:
                    while True:
                        temp = file.readline()
                        if temp:
                            count += len(temp)
                        else:
                            break
                self.tablewidget.setItem(0, col, QTableWidgetItem(str(count)))
            except:
                self.tablewidget.setItem(0, col, QTableWidgetItem('非文本文件'))
            self.tablewidget.setItem(1, col, QTableWidgetItem(sltk.bit2size(os.path.getsize(filename))))
            temp = sltk.calc_hash(filename, md5=True, crc32=True, blake3=True, sha1=True, sha224=True, sha256=True, sha384=True, sha512=True)
        else:
            self.tablewidget.setItem(0, col, QTableWidgetItem(str(len(txt))))
            self.tablewidget.setItem(1, col, QTableWidgetItem(sltk.bit2size(len(txt.encode('utf-8')))))
            temp = {'md5': hashlib.md5(txt.encode('utf-8')).hexdigest().upper(),
                    'crc32': str(hex(zlib.crc32(txt.encode('utf-8'))))[2:].upper(),
                    'blake3': blake3.blake3(txt.encode('utf-8')).hexdigest().upper(),
                    'sha1': hashlib.sha1(txt.encode('utf-8')).hexdigest().upper(),
                    'sha224': hashlib.sha224(txt.encode('utf-8')).hexdigest().upper(),
                    'sha256': hashlib.sha256(txt.encode('utf-8')).hexdigest().upper(),
                    'sha384': hashlib.sha384(txt.encode('utf-8')).hexdigest().upper(),
                    'sha512': hashlib.sha512(txt.encode('utf-8')).hexdigest().upper()}
        for i in METHOD[2:]:
            self.tablewidget.setItem(METHOD.index(i), col, QTableWidgetItem(temp[i.lower()]))

        # 指定行
        for method in METHOD:
            if method + ':' in txt.upper():
                temp = [i[len(method) + 1:].upper() for i in txt.splitlines() if method + ':' in i.upper()][0]
                self.tablewidget.setItem(METHOD.index(method), col, QTableWidgetItem(temp))

    def update_table_size(self):
        self.tablewidget.setColumnWidth(
            0, self.tablewidget.width() * 0.4)
        self.tablewidget.setColumnWidth(
            1, self.tablewidget.width() * 0.1)
        self.tablewidget.setColumnWidth(
            2, self.tablewidget.width() * 0.4)

    def update_table_data(self, area: str):
        def worker():
            if area == 'a':
                self.set_result(self.lineedit_A.toPlainText(), 0)
            if area == 'b':
                self.set_result(self.lineedit_B.toPlainText(), 2)
            QMetaObject.invokeMethod(self, 'update_table_compare', Qt.ConnectionType.QueuedConnection)
        threading.Thread(target=worker).start()

    @Slot()
    def update_table_compare(self):
        for i in range(self.tablewidget.rowCount()):
            if self.tablewidget.item(i, 0) != None and self.tablewidget.item(i, 2) != None:
                if self.tablewidget.item(i, 0).text().lower() == self.tablewidget.item(i, 2).text().lower():
                    item = QTableWidgetItem('True')
                    item.setBackground(QColor('green'))
                else:
                    item = QTableWidgetItem('False')
                    item.setBackground(QColor('red'))
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                self.tablewidget.setItem(i, 1, item)
            else:
                self.tablewidget.setItem(i, 1, QTableWidgetItem())
        self.update_table_size()
