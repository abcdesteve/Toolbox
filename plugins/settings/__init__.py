from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from qfluentwidgets import *

from sl_lib import *

class Settings(ScrollArea):
    '''setting page'''
    def __init__(self,app:QApplication,mainwindow:QMainWindow,path:str):
        super().__init__()
        self.setObjectName('settings')
        self.container=QWidget()
        self.container.setStyleSheet('QWidget#container{background-color:transparent}')
        self.expendLayout = ExpandLayout(self.container)

        self.cfg=AppConfig()
        qconfig.load(sltk.join_path(path,'神龙工具箱','config.json'),self.cfg)
        print(sltk.join_path(path,'神龙工具箱','config.json'))
        self.scGroup_theme=SettingCardGroup('主题',self.container)
        self.sc_theme_style=ComboBoxSettingCard(self.cfg.theme_style,FluentIcon.PALETTE,'主题','设置主题',['AUTO','LIGHT','DARK'])
        self.sc_theme_color=CustomColorSettingCard(self.cfg.theme_color,FluentIcon.PALETTE,'主题颜色','设置主题颜色')
        self.scGroup_theme.addSettingCards([self.sc_theme_style,self.sc_theme_color])
        self.expendLayout.addWidget(self.scGroup_theme)

        self.scGroup_animation=SettingCardGroup('动画',self.container)
        self.sc_animation_switch=SwitchSettingCard(FluentIcon.ZOOM,'动画','设置窗口切换动画开关',self.cfg.animation_switch)
        self.sc_animation_type=ComboBoxSettingCard(self.cfg.animation_type,FluentIcon.ZOOM,'动画','设置动画样式',['Linear','InOutQuad','InOutCubic','InOutSine','InOutElastic','InOutBack','InOutBounce'])
        self.scGroup_animation.addSettingCards([self.sc_animation_switch,self.sc_animation_type])
        self.expendLayout.addWidget(self.scGroup_animation)

        
        self.container.setLayout(self.expendLayout)
        self.setWidget(self.container)
        self.setWidgetResizable(True)
        

        # self.verticalLayout.addWidget(self.settingcard_theme)
        # self.verticalLayout.addWidget(self.settingCardGroup_animation)
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
        # self.mainwindow.update_theme()
        # if self.ckb_enable_animation.isChecked():
        #     self.cmb_animation.setEnabled(True)
        # else:
        #     self.cmb_animation.setEnabled(False)

        # self.mainwindow.save_settings()
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
    theme_style=OptionsConfigItem('main','theme_mode','AUTO',OptionsValidator(['AUTO','LIGHT','DARK']),restart=True)
    theme_color=ColorConfigItem('main','theme_color','#4cc2ff')
    animation_type=OptionsConfigItem('main','animation_type','InOutCubic',OptionsValidator(['Linear','InOutQuad','InOutCubic','InOutSine','InOutElastic','InOutBack','InOutBounce']))
    animation_switch=ConfigItem('main','animation_switch',True)
