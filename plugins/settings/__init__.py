from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qfluentwidgets import *

from .settings_ui import Ui_settings

class Settings(QWidget,Ui_settings):
    '''setting page'''
    def __init__(self,app:QApplication,mainwindow:QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.signal_connect()
        self.cfg=AppConfig()
        self.cfg.load('temp.config',self.cfg)
        self.settingcard=OptionsSettingCard(self.cfg.theme_mode,FluentIcon.ACCEPT,'主题','设置主题',['AUTO','LIGHT','DARK'])
        self.verticalLayout.addWidget(self.settingcard)

        self.app=app
        self.mainwindow=mainwindow

    def signal_connect(self):
        self.radio_auto.clicked.connect(self.settings_change_status)
        self.radio_light.clicked.connect(self.settings_change_status)
        self.radio_dark.clicked.connect(self.settings_change_status)
        self.ckb_enable_animation.clicked.connect(self.settings_change_status)
        self.cmb_animation.currentTextChanged.connect(self.settings_change_status)
        self.btn_animation_example.clicked.connect(self.settings_perform_animation)

    def settings_change_status(self, do_perform_animation=True):
        '''保存设置修改，同时刷新主题'''
        # update status
        self.mainwindow.update_theme()
        if self.ckb_enable_animation.isChecked():
            self.cmb_animation.setEnabled(True)
        else:
            self.cmb_animation.setEnabled(False)

        self.mainwindow.save_settings()
        if do_perform_animation:
            self.settings_perform_animation()

    def settings_perform_animation(self):
        self.animation_example = QPropertyAnimation(
            self.btn_animation_example, b'pos')
        if self.ckb_enable_animation.isChecked():
            self.animation_example.setDuration(2000)
        else:
            self.animation_example.setDuration(0)
        self.animation_example.setStartValue(QPoint(10, 10))
        self.animation_example.setEndValue(
            QPoint(self.widget.width()-30, 10))
        self.animation_example.setEasingCurve(
            eval('QEasingCurve.'+self.cmb_animation.currentText()))
        self.animation_example.start()
class AppConfig(QConfig):
    "应用配置"
    theme_mode=OptionsConfigItem('main','theme_mode','AUTO',OptionsValidator(['AUTO','DARK','LIGHT']),restart=True)
    animation_type=OptionsConfigItem('main','animation_type','InOutCubic',OptionsValidator(['Linear','InOutQuad','InOutCubic','InOutSine','InOutElastic','InOutBack','InOutBounce']))
    