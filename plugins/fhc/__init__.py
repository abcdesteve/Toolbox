from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .fhc_ui import Ui_fhc

from sl_lib import QMessageBox,sltk

import os
import sys
import math
import hashlib,binascii


class FHC(QWidget, Ui_fhc):
    '''file hash check'''

    def __init__(self,mainwindow):
        super().__init__()
        self.mainwindow=mainwindow
        self.setupUi(self)
        self.signal_connect()
        self.tablewidget.setBorderVisible(True)
        self.tablewidget.setBorderRadius(10)

    def signal_connect(self):
        self.btn_A.clicked.connect(self.select_file)
        self.btn_B.clicked.connect(self.select_file)
        self.lineedit_A.textChanged.connect(lambda:self.table_update_data('a'))
        self.lineedit_B.textChanged.connect(lambda:self.table_update_data('b'))

    def select_file(self):
        section = self.lineedit_A if self.btn_A.hasFocus() else self.lineedit_B
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
                    size = sys.getsizeof(txt.encode())
                    return sltk.bit2size(size)
                case 'crc32':
                    return hex(binascii.crc32(txt.encode('utf-8'))).upper()[2:]
                case _:
                    temp=hashlib.new(method)
                    temp.update(txt.encode('utf-8'))
                    return temp.hexdigest().upper()
                

    def table_update_size(self):
        self.tablewidget.setColumnWidth(
            0, self.tablewidget.width()*0.4)
        self.tablewidget.setColumnWidth(
            1, self.tablewidget.width()*0.1)
        self.tablewidget.setColumnWidth(
            2, self.tablewidget.width()*0.4)

    def table_update_data(self,area:str):
        # self.tablewidget.clearContents()
        self.table_update_size()
        for i in range(self.tablewidget.rowCount()):

            if self.lineedit_A.toPlainText() and area=='a':
                self.tablewidget.setItem(i, 0, QTableWidgetItem(self.get_result(
                    self.tablewidget.verticalHeaderItem(i).text().lower(), self.lineedit_A.toPlainText())))
            if self.lineedit_B.toPlainText() and area=='b':
                self.tablewidget.setItem(i, 2, QTableWidgetItem(self.get_result(
                    self.tablewidget.verticalHeaderItem(i).text().lower(), self.lineedit_B.toPlainText())))

            if self.tablewidget.item(i, 0) != None and self.tablewidget.item(i, 2) != None:
                if self.tablewidget.item(i, 0).text() == self.tablewidget.item(i, 2).text():
                    item=QTableWidgetItem('True')
                    item.setBackground(QColor('green'))
                else:
                    item=QTableWidgetItem('False')
                    item.setBackground(QColor('red'))
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                self.tablewidget.setItem(i, 1, item)
            else:
                self.tablewidget.setItem(i, 1, QTableWidgetItem())

    def dragEnterEvent(self, event):
        event.accept()
        return super().dragEnterEvent(event)
    
    def dropEvent(self, event:QEvent):
        if event.mimeData().hasUrls():
            path=event.mimeData().urls()[0].toLocalFile()
            if event.position().x()<self.width()//2:
                self.lineedit_A.setPlainText('file:'+path)
            else:
                self.lineedit_B.setPlainText('file:'+path)
            event.accept()
        return super().dropEvent(event)
