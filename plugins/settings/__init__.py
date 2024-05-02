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
        self.container.setObjectName('container')
        self.container.setStyleSheet('QWidget#container{background-color:transparent}')
        self.expendLayout = ExpandLayout(self.container)

        self.cfg=AppConfig()
        qconfig.load(sltk.join_path(path,'神龙工具箱','config.json'),self.cfg)
        self.scGroup_theme=SettingCardGroup('主题',self.container)
        self.sc_theme_style=ComboBoxSettingCard(self.cfg.theme_style,FluentIcon.PALETTE,'主题','设置主题',['跟随系统','浅色','深色'])
        self.sc_theme_color=CustomColorSettingCard(self.cfg.theme_color,FluentIcon.PALETTE,'主题颜色','设置主题颜色')
        self.scGroup_theme.addSettingCards([self.sc_theme_style,self.sc_theme_color])
        self.expendLayout.addWidget(self.scGroup_theme)

        self.scGroup_animation=SettingCardGroup('动画',self.container)
        self.sc_animation_switch=SwitchSettingCard(FluentIcon.ZOOM,'动画','设置窗口切换动画开关',self.cfg.animation_switch)
        self.sc_animation_type=ComboBoxSettingCard(self.cfg.animation_type,FluentIcon.ZOOM,'动画','设置动画样式',['线性插值','四次插值','三次插值','正弦插值','弹性插值','回弹插值','弹跳插值'])
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
        if do_perform_animation:
            self.settings_perform_animation()

    # def settings_perform_animation(self):
    #     self.animation_example = QPropertyAnimation(
    #         self.btn_animation_example, b'pos')
    #     if self.ckb_enable_animation.isChecked():
    #         self.animation_example.setDuration(2000)
    #     else:
    #         self.animation_example.setDuration(0)
    #     self.animation_example.setStartValue(QPoint(10, 10))
    #     self.animation_example.setEndValue(
    #         QPoint(self.widget.width()-30, 10))
    #     self.animation_example.setEasingCurve(
    #         eval('QEasingCurve.'+self.cmb_animation.currentText()))
    #     self.animation_example.start()

class AppConfig(QConfig):
    "应用配置"
    # 小技巧：OptionsValidator当中的项为存储至配置文件中的项，在i18n当中可在上方创建设置卡时使用不同的语言，只需要保证索引对应即可
    theme_style=OptionsConfigItem('main','theme_mode','AUTO',OptionsValidator(['AUTO','LIGHT','DARK']),restart=True)
    theme_color=ColorConfigItem('main','theme_color','#4cc2ff')
    animation_type=OptionsConfigItem('main','animation_type','InOutCubic',OptionsValidator(['Linear','InOutQuad','InOutCubic','InOutSine','InOutElastic','InOutBack','InOutBounce']))
    animation_switch=ConfigItem('main','animation_switch',True)
