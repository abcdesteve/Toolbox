import os
import sys
import qdarkstyle
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_gui import Ui_gui
from ui_tab_aam import Ui_aam
from ui_tab_csl import Ui_csl
from ui_wireless import Ui_wireless


class Wireless(QMainWindow, Ui_wireless):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def closeEvent(self, event):
        self.hide()
        global window
        window.aam_read(self.lineedit_ip.text(), self.lineedit_port.text())


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.aam = Ui_aam()
        self.aam.setupUi(self.tab_1)
        self.csl = Ui_csl()
        self.csl.setupUi(self.tab_2)

        self.subwin_wireless = Wireless()

        self.tabWidget.currentChanged.connect(self.window_size_change)
        self.window_size_change()

        # aam
        self.aam.btn_wireless.clicked.connect(self.subwin_wireless.show)
        self.aam.btn_device.clicked.connect(self.aam_device_update)
        self.aam.btn_getapp_high.clicked.connect(self.aam_getapp_high)
        self.aam.btn_getapp_low.clicked.connect(self.aam_getapp_low)
        self.aam.btn_clear.clicked.connect(self.aam.textedit_log.clear)
        self.aam.btn_launch.clicked.connect(self.aam_launch)
        self.aam.btn_extract.clicked.connect(self.aam_extract)
        self.aam.btn_install.clicked.connect(self.aam_install)
        self.aam.btn_uninstall.clicked.connect(self.aam_uninstall)
        self.aam.btn_freeze.clicked.connect(self.aam_freeze)
        self.aam.btn_unfreeze.clicked.connect(self.aam_unfreeze)
        self.aam.btn_backup.clicked.connect(self.aam_backup)
        self.aam.btn_restore.clicked.connect(self.aam_restore)

        self.aam.cmb_device.currentIndexChanged.connect(self.aam_app_update)

        # csl
        self.csl.btn_to.clicked.connect(self.csl_select_to)
        self.csl.btn_from.clicked.connect(self.csl_select_from)
        self.csl.btn_start.clicked.connect(self.csl_start)

        self.show()

    def window_size_change(self):
        match self.tabWidget.currentIndex():
            case 0:
                self.resize(800, 500)
            case 1:
                self.resize(600, 50)
# aam

    def aam_read(self, ip, port):
        log = os.popen(f'adb connect {ip}:{port}').read()
        self.aam.textedit_log.append(log)
        if self.aam.cmb_device.findText(f'{ip}:{port}') == -1:
            QMessageBox.warning(self, '警告', '未能成功连接')
        self.aam.device_update()

    def aam_device_update(self):
        log = os.popen('adb devices').read()
        self.aam.textedit_log.append(log)
        self.aam.cmb_device.clear()
        if log.count('device') > 1:
            for i in log.split('\n')[1:]:
                if i:
                    self.aam.cmb_device.addItem(i.split('\t')[0])
        else:
            QMessageBox.warning(self, '警告', '设备连接失败')

    def aam_app_update(self):
        if self.aam.cmb_device.currentText():
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell pm list package').read()
            # self.aam.textedit_log.append(log)
            self.aam.cmb_app.clear()
            self.aam.cmb_app.addItems([i[8:] for i in log.split('\n')if i])
        else:
            QMessageBox.warning(self, '警告', '无法获取应用列表，请先连接设备')

    def aam_getapp_high(self):
        log = os.popen(
            f'adb -s {self.aam.cmb_device.currentText()} shell dumpsys activity |findstr "mResumedActivity"').read()
        if 'ActivityRecord' in log:
            self.aam.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.aam.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_getapp_low(self):
        log = os.popen(
            f'adb -s {self.aam.cmb_device.currentText()} shell dumpsys activity |findstr "mFocusedActivity"').read()
        if 'ActivityRecord' in log:
            self.aam.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.aam.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_launch(self):
        if self.aam.cmb_app.currentText():
            # 获取activity
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell monkey -p {self.aam.cmb_app.currentText()} -v -v -v 1 | findstr "cmp="').read()
            # 启动应用
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell am start -n {log.split("cmp=")[1].split(" }")[0]}').read()
            self.aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_extract(self):
        if self.aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell pm path {self.aam.cmb_app.currentText()}').read()[8:]
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} pull {log}').read()
            self.aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_install(self):
        if self.aam.cmb_device.currentText():
            path = QFileDialog.getOpenFileName(
                self, '请选择安装包', filter='安卓安装包 (*.apk)')[0]
            if path:
                log = os.popen(
                    f'adb -s {self.aam.cmb_device.currentText()} install "{path}"').read()
                self.aam.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先连接设备')

    def aam_uninstall(self):
        if self.aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} uninstall {self.aam.cmb_app.currentText()}').read()
            self.aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_freeze(self):
        if self.aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell pm disable-user {self.aam.cmb_app.currentText()}').read()
            self.aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')
    def aam_unfreeze(self):
        if self.aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.aam.cmb_device.currentText()} shell pm enable {self.aam.cmb_app.currentText()}').read()
            self.aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_backup(self):
        if self.aam.cmb_app.currentText():
            path = QFileDialog.getSaveFileName(
                self, '请选择备份文件保存位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                # -apk 含安装包备份
                log = os.popen(
                    f'adb -s {self.aam.cmb_device.currentText()} backup -nosystem -noshared -f "{path}" {self.aam.cmb_app.currentText()}').read()
                self.aam.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_restore(self):
        if self.aam.cmb_app.currentText():
            path = QFileDialog.getOpenFileName(
                self, '请选择恢复文件位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                log = os.popen(
                    f'adb -s {self.aam.cmb_device.currentText()} restore "{path}"').read()
                self.aam.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写备份文件路径')

# csl
    def csl_select_from(self):
        path = QFileDialog.getExistingDirectory(self, '请选择本体路径')
        if path:
            self.csl.lineedit_from.setText(path)
            self.csl.lineedit_to_name.setText(os.path.split(path)[1])
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_select_to(self):
        path = QFileDialog.getExistingDirectory(self, '请选择目标路径')
        if path:
            self.csl.lineedit_to_dir.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_start(self):
        if self.csl.lineedit_from.text() and self.csl.lineedit_to_dir.text() and self.csl.lineedit_to_name.text():
            log = os.popen(
                f'mklink /j "{self.csl.lineedit_to_dir.text()}/{self.csl.lineedit_to_name.text()}" "{self.csl.lineedit_from.text()}"').read()
            if 'created' in log:
                QMessageBox.information(self, '成功', '符号链接创建成功')
            elif 'exists' in log:
                QMessageBox.warning(self, '警告', f'请勿选择已存在的目标路径\n{log}')
            elif 'NTFS' in log:
                QMessageBox.warning(self, '警告', f'请确保路径所在驱动盘为NTFS文件格式\n{log}')
            else:
                QMessageBox.warning(self, '警告', f'未知错误\n{log}')
        else:
            QMessageBox.warning(self, '警告', '请先选择本体路径与目标路径')
# key bind
    def keyPressEvent(self, event):
        if self.aam.lineedit_cmd.hasFocus():
            if event.key()==Qt.Key_Return:
                popen=os.popen(self.aam.lineedit_cmd.text()).read()
                self.aam.textedit_log.append(popen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = Main()
    sys.exit(app.exec())
