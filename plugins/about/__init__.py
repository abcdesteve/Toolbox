from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .about_ui import Ui_about

from qfluentwidgets import FluentIcon

from sl_lib import sltk

import webbrowser,os

class About(QWidget,Ui_about):
    '''About page'''
    def __init__(self,parent_dir:str):
        super().__init__()
        self.setupUi(self)
        self.btn_github.setIcon(FluentIcon.GITHUB)
        # self.btn_bilibili.setIcon(FluentIcon.HOME)
        self.btn_bilibili.setIcon(QIcon(sltk.join_path(parent_dir,'icons','bilibili.svg')))
        self.btn_tour.setIcon(FluentIcon.MOVIE)
        self.signal_connect()
        try:
            with open(sltk.join_path(parent_dir,'update.md'),'r',encoding='utf-8')as file:
                self.textEdit.setMarkdown('\n'.join(file.readlines()[9:]))
        except:
            pass

    def signal_connect(self):
        self.btn_github.clicked.connect(lambda:webbrowser.open('https://www.github.com/abcdesteve'))
        self.btn_bilibili.clicked.connect(lambda:webbrowser.open('https://space.bilibili.com/520340464'))
        self.btn_tour.clicked.connect(lambda:webbrowser.open('https://space.bilibili.com/1247794668'))