from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from qfluentwidgets import *

from sl_lib import *
import theme_control

from plugins.aam import AAM
from plugins.csl import CSL
from plugins.fhc import FHC
from plugins.fas import FAS
from plugins.settings import Settings
from plugins.about import About

import os
import sys
import threading


class Main(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle('神龙工具箱v2.1')

        self.subwin_aam = AAM(self, os.path.dirname(__file__))
        self.subwin_csl = CSL()
        self.subwin_fhc = FHC()
        self.subwin_fas = FAS(self)
        self.subwin_settings = Settings(app, self, path)
        self.subwin_about = About(os.path.dirname(__file__))

        self.addSubInterface(self.subwin_aam, MyFluentIcon.Android,
                             '安卓应用管理', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.subwin_csl, FluentIcon.LINK,
                             '创建符号链接', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.subwin_fhc, FluentIcon.SEARCH,
                             '文件哈希校验', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.subwin_fas, FluentIcon.SYNC,
                             '文件自动同步', NavigationItemPosition.SCROLL)
        self.addSubInterface(
            self.subwin_settings, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.subwin_about, FluentIcon.INFO,
                             '关于', NavigationItemPosition.BOTTOM)

        self.stackedWidget.currentChanged.connect(self.window_size_change)
        self.window_size_change()
        self.subwin_settings.cfg.theme_style.valueChanged.connect(self.update_theme)
        self.update_theme()
        self.subwin_settings.cfg.theme_color.valueChanged.connect(lambda:setThemeColor(self.subwin_settings.cfg.theme_color.value))
        setThemeColor(self.subwin_settings.cfg.theme_color.value)

        self.show()

    def update_theme(self):
        theme_control.apply_theme(app, self.subwin_settings.cfg.get(self.subwin_settings.cfg.theme_style))
        # self.setWindowIcon(FluentIcon.icon(
        #     FluentIcon.DEVELOPER_TOOLS, theme()))
        self.setWindowIcon(MyFluentIcon.icon(MyFluentIcon.ToolBox))
        self.subwin_fas.subwin_taskedit.setWindowIcon(self.windowIcon())

    def window_size_change(self):
        if not self.isMaximized():
            self.animation = QPropertyAnimation(self, b'size')
            # if self.subwin_settings.ckb_enable_animation.isChecked():
            if self.subwin_settings.cfg.get(self.subwin_settings.cfg.animation_switch):
                self.animation.setDuration(500)
            else:
                self.animation.setDuration(0)
            self.animation.setEasingCurve(
                eval('QEasingCurve.'+self.subwin_settings.cfg.get(self.subwin_settings.cfg.animation_type)))
            # print(self.stackedWidget.currentIndex())
            match self.stackedWidget.currentIndex():
                case 0:
                    self.animation.setEndValue(QSize(800, 500))
                case 1:
                    self.animation.setEndValue(QSize(600, 50))
                case 2:
                    self.animation.setEndValue(QSize(800, 600))
                    self.subwin_fhc.table_update_size()
                case 3:
                    self.animation.setEndValue(QSize(500, 400))
                case 4:
                    self.animation.setEndValue(QSize(500, 75))
                case 5:
                    self.animation.setEndValue(QSize(800, 600))
            self.animation.start()

    def dragEnterEvent(self, event):
        drag_path = event.mimeData().urls()[0].toLocalFile()
        ext = os.path.splitext(drag_path)[1]
        if self.stackedWidget.currentIndex() == 0 and ext == '.apk':
            event.accept()
        elif self.stackedWidget.currentIndex() == 1 and os.path.isdir(drag_path):
            event.accept()
        elif self.stackedWidget.currentIndex() == 2 and os.path.isfile(drag_path):
            event.accept()
        # elif not self.subwin_fas.subwin_taskedit.isHidden():
        #     event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        drag_file = event.mimeData().urls()[0].toLocalFile()
        if drag_file:
            if self.stackedWidget.currentIndex() == 0:
                if self.subwin_aam.cmb_device.currentText():
                    if QMessageBox.question(self, '拖拽安装', f'你确认将\n{drag_file}\n安装到 {self.subwin_aam.cmb_device.currentText()} 上吗？') == QMessageBox.Yes:
                        self.subwin_aam.aam_install(drag_file)
                else:
                    QMessageBox.warning(self, '警告', '请先连接设备')

            elif self.stackedWidget.currentIndex() == 1:
                if self.subwin_csl.lineedit_from.hasFocus():
                    self.subwin_csl.lineedit_from.setText(drag_file)
                elif self.subwin_csl.lineedit_to_dir.hasFocus():
                    self.subwin_csl.lineedit_to_dir.setText(drag_file)

            elif self.stackedWidget.currentIndex() == 2:
                if event.pos().x() <= self.width()//2:
                    self.subwin_fhc.lineedit_A.setPlainText(
                        f'file:{drag_file}')
                else:
                    self.subwin_fhc.lineedit_B.setPlainText(
                        f'file:{drag_file}')

    def keyPressEvent(self, event: QKeyEvent) -> None:
        match self.stackedWidget.currentIndex():
            case 0:
                if event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter] and self.subwin_aam.lineedit_cmd.hasFocus():
                    def aam_cmd():
                        popen = os.popen(
                            self.subwin_aam.lineedit_cmd.text()).read()
                        self.subwin_aam.textedit_log.append(popen)
                        self.subwin_aam.textedit_log.moveCursor(QTextCursor.MoveOperation.End)
                    threading.Thread(target=aam_cmd).start()
        event.ignore()

    def closeEvent(self, event):
        app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fluent_translator=FluentTranslator()
    app.installTranslator(fluent_translator)

    path = os.path.expandvars(r'%appdata%/Avoconal')
    window = Main()

    sys.exit(app.exec())
