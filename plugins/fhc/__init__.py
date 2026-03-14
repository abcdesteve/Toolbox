from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .fhc_ui import Ui_fhc

from sl_lib import QMessageBox,sltk

import os
import sys
import hashlib,binascii,blake3
from concurrent.futures import ThreadPoolExecutor


class FHC(QWidget, Ui_fhc):
    '''文件哈希校验\nfile hash check'''

    def __init__(self,mainwindow):
        super().__init__()
        self.mainwindow=mainwindow
        self.setupUi(self)
        self.signal_connect()
        # self.tablewidget.setBorderVisible(True)
        # self.tablewidget.setBorderRadius(10)

    def signal_connect(self):
        self.btn_A.clicked.connect(lambda:self.select_file(self.lineedit_A))
        self.btn_B.clicked.connect(lambda:self.select_file(self.lineedit_B))
        self.lineedit_A.textChanged.connect(lambda:self.update_table_data('a'))
        self.lineedit_B.textChanged.connect(lambda:self.update_table_data('b'))
        self.tablewidget.currentCellChanged.connect(self.update_table_compare)

    def select_file(self,section: QLineEdit):
        # 为了键盘tab体验移除了按钮的焦点，现在不能靠焦点判断
        # section = self.lineedit_A if self.btn_A.hasFocus() else self.lineedit_B
        path = QFileDialog.getOpenFileName(self, '请选择文件')[0]
        if path:
            # with open(path, 'br')as file:
            #     section.setPlainText(str(file.read()))
            section.setPlainText('file:'+path)
        else:
            QMessageBox.warning(self.mainwindow, '警告', '路径无效')

    def get_result(self, method: str, txt: str):
        STEP=1024000
        if method+':' in txt.lower():
            return [i[len(method)+1:].upper() for i in txt.splitlines() if method+':' in i.lower()][0]
        
        # 文件
        elif 'file:' in txt and os.path.isfile([i[5:] for i in txt.splitlines() if 'file:' in i][0]):
            filename=txt.split('file:')[1].split('\n')[0]
            with open(filename, 'rb')as file:
                match method:
                    case '字符数':
                        count = 0
                        while True:
                            data = file.read(STEP)
                            if not data:
                                break
                            count += len(data)
                        return str(count)
                    case '文件大小':
                        size = os.path.getsize(filename)
                        return sltk.bit2size(size)
                    case 'crc32':
                        temp=0
                        while True:
                            data = file.read(STEP)
                            if not data:
                                break
                            temp=binascii.crc32(data,temp)
                        return hex(temp).upper()[2:]
                    case 'blake3':
                        temp=blake3.blake3()
                        while True:
                            data = file.read(STEP)
                            if not data:
                                break
                            temp.update(data)
                        return temp.hexdigest().upper()
                    case _:
                        temp=hashlib.new(method)
                        while True:
                            data = file.read(STEP)
                            if not data:
                                break
                            temp.update(data)
                        return temp.hexdigest().upper()
        # 文本
        else: 
            match method:
                case '字符数':
                    return str(len(txt))
                case '文件大小':
                    # sys.getsizeof()函数返回的是对象的大小
                    size = len(txt.encode("utf-8"))
                    return sltk.bit2size(size)
                case 'crc32':
                    return hex(binascii.crc32(txt.encode('utf-8'))).upper()[2:]
                case 'blake3':
                    return blake3.blake3(txt.encode('utf-8')).hexdigest().upper()
                case _:
                    temp=hashlib.new(method)
                    temp.update(txt.encode('utf-8'))
                    return temp.hexdigest().upper()
                

    def update_table_size(self):
        self.tablewidget.setColumnWidth(
            0, self.tablewidget.width()*0.4)
        self.tablewidget.setColumnWidth(
            1, self.tablewidget.width()*0.1)
        self.tablewidget.setColumnWidth(
            2, self.tablewidget.width()*0.4)

    def update_table_data(self,area:str):
        for i in range(self.tablewidget.rowCount()):
            if self.lineedit_A.toPlainText() and area=='a':
                self.tablewidget.setItem(i, 0, QTableWidgetItem(self.get_result(
                    self.tablewidget.verticalHeaderItem(i).text().lower(), self.lineedit_A.toPlainText())))
            if self.lineedit_B.toPlainText() and area=='b':
                self.tablewidget.setItem(i, 2, QTableWidgetItem(self.get_result(
                    self.tablewidget.verticalHeaderItem(i).text().lower(), self.lineedit_B.toPlainText())))
        self.update_table_compare()

    def update_table_compare(self):
        for i in range(self.tablewidget.rowCount()):
            if self.tablewidget.item(i, 0) != None and self.tablewidget.item(i, 2) != None:
                if self.tablewidget.item(i, 0).text().lower() == self.tablewidget.item(i, 2).text().lower():
                    item=QTableWidgetItem('True')
                    item.setBackground(QColor('green'))
                else:
                    item=QTableWidgetItem('False')
                    item.setBackground(QColor('red'))
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                self.tablewidget.setItem(i, 1, item)
            else:
                self.tablewidget.setItem(i, 1, QTableWidgetItem())
        self.update_table_size()
