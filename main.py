import os
import sys
import math
import hashlib
import json

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# import qdarkstyle
# from qt_material import apply_stylesheet
from qfluentwidgets.common import setTheme

from gui_ui import Ui_gui
from tab_aam_ui import Ui_aam
from tab_csl_ui import Ui_csl
from tab_fhc_ui import Ui_fhc
from wireless_ui import Ui_wireless
from tab_settings_ui import Ui_settings


class Wireless(QMainWindow, Ui_wireless):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def closeEvent(self, event):
        self.hide()
        global window
        window.aam_read(self.lineedit_ip.text(), self.lineedit_port.text())


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.subwin_aam = Ui_aam()
        self.subwin_aam.setupUi(self.tab_1)
        self.subwin_csl = Ui_csl()
        self.subwin_csl.setupUi(self.tab_2)
        self.subwin_fhc = Ui_fhc()
        self.subwin_fhc.setupUi(self.tab_3)
        self.subwin_settings = Ui_settings()
        self.subwin_settings.setupUi(self.tab_4)

        self.subwin_wireless = Wireless()

        self.tabWidget.currentChanged.connect(self.window_size_change)
        self.window_size_change()

        self.drag_file = ''
        self.signal_connect()

    def signal_connect(self):
        # aam
        self.subwin_aam.btn_wireless.clicked.connect(self.subwin_wireless.show)
        self.subwin_aam.btn_device.clicked.connect(self.aam_device_update)
        self.subwin_aam.btn_getapp_high.clicked.connect(self.aam_getapp_high)
        self.subwin_aam.btn_getapp_low.clicked.connect(self.aam_getapp_low)
        self.subwin_aam.btn_clear.clicked.connect(self.subwin_aam.textedit_log.clear)
        self.subwin_aam.btn_launch.clicked.connect(self.aam_launch)
        self.subwin_aam.btn_extract.clicked.connect(self.aam_extract)
        self.subwin_aam.btn_install.clicked.connect(self.aam_install)
        self.subwin_aam.btn_uninstall.clicked.connect(self.aam_uninstall)
        self.subwin_aam.btn_freeze.clicked.connect(self.aam_freeze)
        self.subwin_aam.btn_unfreeze.clicked.connect(self.aam_unfreeze)
        self.subwin_aam.btn_backup.clicked.connect(self.aam_backup)
        self.subwin_aam.btn_restore.clicked.connect(self.aam_restore)

        self.subwin_aam.cmb_device.currentIndexChanged.connect(self.aam_app_update)

        # csl
        self.subwin_csl.btn_to.clicked.connect(self.csl_select_to)
        self.subwin_csl.btn_from.clicked.connect(self.csl_select_from)
        self.subwin_csl.btn_start.clicked.connect(self.csl_start)

        # fhc
        self.subwin_fhc.btn_A.clicked.connect(self.fhc_select)
        self.subwin_fhc.btn_B.clicked.connect(self.fhc_select)
        self.subwin_fhc.lineedit_A.textChanged.connect(self.fhc_table_update_data)
        self.subwin_fhc.lineedit_B.textChanged.connect(self.fhc_table_update_data)
        self.subwin_fhc.tablewidget.currentItemChanged.connect(
            self.fhc_table_update_data)

        # settings
        self.subwin_settings.radio_light.clicked.connect(self.settings_change_status)
        self.subwin_settings.radio_dark.clicked.connect(self.settings_change_status)
        self.subwin_settings.ckb_enable_animation.clicked.connect(
            self.settings_change_status)
        self.subwin_settings.cmb_animation.currentTextChanged.connect(
            self.settings_change_status)
        self.subwin_settings.animation_example.clicked.connect(
            self.settings_perform_animation)

        self.show()

    def read_settings(self):
        if os.path.isfile(os.path.join(path, '神龙工具箱', 'settings.json')):
            with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'r')as file:
                data = json.load(file)
            try:
                {'Auto':self.subwin_settings.radio_auto,'Light':self.subwin_settings.radio_light,'Dark':self.subwin_settings.radio_dark}[data['theme']].setChecked(True)
                self.subwin_settings.ckb_enable_animation.setChecked(data['animation'][0])
                self.subwin_settings.cmb_animation.setCurrentText(data['animation'][1])
                self.settings_change_status(False)
            except:
                print('配置文件异常，重置所有设置')
                self.save_settings()
        else:
            try:os.mkdir(path)
            except:pass
            try:os.mkdir(os.path.join(path, '神龙工具箱'))
            except:pass
            with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'w')as file:
                print('Successfully created the setting file')

    def save_settings(self):
        data = {'theme': self.subwin_settings.btn_group_theme.checkedButton().objectName()[6:].capitalize(),
                'animation': [self.subwin_settings.ckb_enable_animation.isChecked(), self.subwin_settings.cmb_animation.currentText()]}
        with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'w')as file:
            json.dump(data, file)

    def window_size_change(self):
        self.animation = QPropertyAnimation(self, b'size')
        if self.subwin_settings.ckb_enable_animation.isChecked():
            self.animation.setDuration(500)
        else:
            self.animation.setDuration(0)
        self.animation.setEasingCurve(
            eval('QEasingCurve.'+self.subwin_settings.cmb_animation.currentText()))
        match self.tabWidget.currentIndex():
            case 0:
                self.animation.setEndValue(QSize(800, 500))
                # self.resize(800, 500)
            case 1:
                self.animation.setEndValue(QSize(600, 50))
                # self.resize(600, 50)
            case 2:
                self.animation.setEndValue(QSize(800, 600))
                # self.resize(800, 600)
                self.fhc_table_update_size()
            case 3:
                self.animation.setEndValue(QSize(500, 75))
                # self.settings.animation_example.setGeometry(10,10,24,24)
        self.animation.start()
# aam
    def aam_read(self, ip, port):
        log = os.popen(f'adb connect {ip}:{port}').read()
        self.subwin_aam.textedit_log.append(log)
        if self.subwin_aam.cmb_device.findText(f'{ip}:{port}') == -1:
            QMessageBox.warning(self, '警告', '未能成功连接')
        self.subwin_aam.device_update()

    def aam_device_update(self):
        log = os.popen('adb devices').read()
        self.subwin_aam.textedit_log.append(log)
        self.subwin_aam.cmb_device.clear()
        if log.count('device') > 1:
            for i in log.split('\n')[1:]:
                if i:
                    self.subwin_aam.cmb_device.addItem(i.split('\t')[0])
        else:
            QMessageBox.warning(self, '警告', '设备连接失败')

    def aam_app_update(self):
        if self.subwin_aam.cmb_device.currentText():
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell pm list package').read()
            # self.aam.textedit_log.append(log)
            self.subwin_aam.cmb_app.clear()
            self.subwin_aam.cmb_app.addItems([i[8:] for i in log.split('\n')if i])
        else:
            QMessageBox.warning(self, '警告', '无法获取应用列表，请先连接设备')

    def aam_getapp_high(self):
        log = os.popen(
            f'adb -s {self.subwin_aam.cmb_device.currentText()} shell dumpsys activity |findstr "mResumedActivity"').read()
        if 'ActivityRecord' in log:
            self.subwin_aam.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.subwin_aam.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_getapp_low(self):
        log = os.popen(
            f'adb -s {self.subwin_aam.cmb_device.currentText()} shell dumpsys activity |findstr "mFocusedActivity"').read()
        if 'ActivityRecord' in log:
            self.subwin_aam.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.subwin_aam.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_launch(self):
        if self.subwin_aam.cmb_app.currentText():
            # 获取activity
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell monkey -p {self.subwin_aam.cmb_app.currentText()} -v -v -v 1 | findstr "cmp="').read()
            # 启动应用
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell am start -n {log.split("cmp=")[1].split(" }")[0]}').read()
            self.subwin_aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_extract(self):
        if self.subwin_aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell pm path {self.subwin_aam.cmb_app.currentText()}').read()[8:]
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} pull {log}').read()
            self.subwin_aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_install(self, apk=''):
        if self.subwin_aam.cmb_device.currentText():
            if apk:
                log = os.popen(
                    f'adb -s {self.subwin_aam.cmb_device.currentText()} install "{apk}"').read()
                self.subwin_aam.textedit_log.append(log)
            else:
                path = QFileDialog.getOpenFileName(
                    self, '请选择安装包', filter='安卓安装包 (*.apk)')[0]
                if path:
                    log = os.popen(
                        f'adb -s {self.subwin_aam.cmb_device.currentText()} install "{path}"').read()
                    self.subwin_aam.textedit_log.append(log)
                else:
                    QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先连接设备')

    def aam_uninstall(self):
        if self.subwin_aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} uninstall {self.subwin_aam.cmb_app.currentText()}').read()
            self.subwin_aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_freeze(self):
        if self.subwin_aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell pm disable-user {self.subwin_aam.cmb_app.currentText()}').read()
            self.subwin_aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_unfreeze(self):
        if self.subwin_aam.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.subwin_aam.cmb_device.currentText()} shell pm enable {self.subwin_aam.cmb_app.currentText()}').read()
            self.subwin_aam.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_backup(self):
        if self.subwin_aam.cmb_app.currentText():
            path = QFileDialog.getSaveFileName(
                self, '请选择备份文件保存位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                # -apk 含安装包备份
                log = os.popen(
                    f'adb -s {self.subwin_aam.cmb_device.currentText()} backup -nosystem -noshared -f "{path}" {self.subwin_aam.cmb_app.currentText()}').read()
                self.subwin_aam.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_restore(self):
        if self.subwin_aam.cmb_app.currentText():
            path = QFileDialog.getOpenFileName(
                self, '请选择恢复文件位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                log = os.popen(
                    f'adb -s {self.subwin_aam.cmb_device.currentText()} restore "{path}"').read()
                self.subwin_aam.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写备份文件路径')

# csl
    def csl_select_from(self):
        path = QFileDialog.getExistingDirectory(self, '请选择本体路径')
        if path:
            self.subwin_csl.lineedit_from.setText(path)
            self.subwin_csl.lineedit_to_name.setText(os.path.split(path)[1])
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_select_to(self):
        path = QFileDialog.getExistingDirectory(self, '请选择目标路径')
        if path:
            self.subwin_csl.lineedit_to_dir.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_start(self):
        if self.subwin_csl.lineedit_from.text() and self.subwin_csl.lineedit_to_dir.text() and self.subwin_csl.lineedit_to_name.text():
            log = os.popen(
                f'mklink /j "{self.subwin_csl.lineedit_to_dir.text()}/{self.subwin_csl.lineedit_to_name.text()}" "{self.subwin_csl.lineedit_from.text()}"').read()
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

# fhc
    def fhc_select(self):
        section = self.subwin_fhc.lineedit_A if self.subwin_fhc.btn_A.hasFocus() else self.subwin_fhc.lineedit_B
        path = QFileDialog.getOpenFileName(self, '请选择文件')[0]
        if path:
            # with open(path, 'br')as file:
            #     section.setPlainText(str(file.read()))
            section.setPlainText('file:'+path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def fhc_get_hash(self, method: str, txt: str):
        if method+':' in txt:
            return [i[len(method)+1:] for i in txt.split('\n') if method+':' in i][0]
        elif 'file:' in txt and os.path.isfile([i[5:] for i in txt.split('\n') if 'file:' in i][0]):
            with open(txt[5:].split('\n')[0], 'rb')as file:
                txt = file.read()
        else:
            txt = txt.encode()

        if method == '字符数':
            try:
                return str(len(txt.decode()))
            except:
                return str(len(txt))+' 未解码'
        elif method == '文件大小':
            num = sys.getsizeof(txt)
            match math.floor(math.log(num, 1024)):
                case 0:
                    return f'{num} B'
                case 1:
                    return f'{round(num/1024,2)} KiB'
                case 2:
                    return f'{round(num/1024**2,2)} MiB'
                case 3:
                    return f'{round(num/1024**3,2)} GiB'
                case 4:
                    return f'{round(num/1024**3,2)} TiB'
        elif method == 'md5':
            return hashlib.md5(txt).hexdigest()
        elif method == 'sha1':
            return hashlib.sha1(txt).hexdigest()
        elif method == 'sha224':
            return hashlib.sha224(txt).hexdigest()
        elif method == 'sha256':
            return hashlib.sha256(txt).hexdigest()
        elif method == 'sha384':
            return hashlib.sha384(txt).hexdigest()
        elif method == 'sha512':
            return hashlib.sha512(txt).hexdigest()

    def fhc_table_update_size(self):
        self.subwin_fhc.tablewidget.setColumnWidth(
            0, self.subwin_fhc.tablewidget.width()*0.4)
        self.subwin_fhc.tablewidget.setColumnWidth(
            1, self.subwin_fhc.tablewidget.width()*0.1)
        self.subwin_fhc.tablewidget.setColumnWidth(
            2, self.subwin_fhc.tablewidget.width()*0.4)

    def fhc_table_update_data(self):
        self.subwin_fhc.tablewidget.clearContents()
        self.fhc_table_update_size()
        for i in range(self.subwin_fhc.tablewidget.rowCount()):

            if self.subwin_fhc.lineedit_A.toPlainText():
                self.subwin_fhc.tablewidget.setItem(i, 0, QTableWidgetItem(self.fhc_get_hash(
                    self.subwin_fhc.tablewidget.verticalHeaderItem(i).text(), self.subwin_fhc.lineedit_A.toPlainText())))
            if self.subwin_fhc.lineedit_B.toPlainText():
                self.subwin_fhc.tablewidget.setItem(i, 2, QTableWidgetItem(self.fhc_get_hash(
                    self.subwin_fhc.tablewidget.verticalHeaderItem(i).text(), self.subwin_fhc.lineedit_B.toPlainText())))

            if self.subwin_fhc.tablewidget.item(i, 0) != None and self.subwin_fhc.tablewidget.item(i, 2) != None:
                if self.subwin_fhc.tablewidget.item(i, 0).text() == self.subwin_fhc.tablewidget.item(i, 2).text():
                    self.subwin_fhc.tablewidget.setItem(
                        i, 1, QTableWidgetItem('True'))
                    self.subwin_fhc.tablewidget.item(
                        i, 1).setBackground(QColor('green'))
                else:
                    self.subwin_fhc.tablewidget.setItem(
                        i, 1, QTableWidgetItem('False'))
                    self.subwin_fhc.tablewidget.item(
                        i, 1).setBackground(QColor('red'))
            else:
                self.subwin_fhc.tablewidget.setItem(i, 1, QTableWidgetItem())

# settings
    def settings_change_status(self, flag=True):
        # update status
        print(self.subwin_settings.btn_group_theme.checkedButton().objectName()[6:].capitalize()) #last
        setTheme(self.subwin_settings.btn_group_theme.checkedButton().objectName()[6:].capitalize())
        if self.subwin_settings.ckb_enable_animation.isChecked():
            self.subwin_settings.cmb_animation.setEnabled(True)
        else:
            self.subwin_settings.cmb_animation.setEnabled(False)

        # origin theme settings
        # if self.settings.radio_dark.isChecked():
        #     app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
        # elif self.settings.radio_colorful.isChecked():
        #     apply_stylesheet(app, self.settings.cmb_theme.currentText()+'.xml')

        self.save_settings()

        if flag:
            self.settings_perform_animation()

    def settings_perform_animation(self):
        self.animation_example = QPropertyAnimation(
            self.subwin_settings.animation_example, b'pos')
        if self.subwin_settings.ckb_enable_animation.isChecked():
            self.animation_example.setDuration(2000)
        else:
            self.animation_example.setDuration(0)
        self.animation_example.setStartValue(QPoint(10, 10))
        self.animation_example.setEndValue(
            QPoint(self.subwin_settings.widget.width()-30, 10))
        self.animation_example.setEasingCurve(
            eval('QEasingCurve.'+self.subwin_settings.cmb_animation.currentText()))
        self.animation_example.start()

# key bind
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            QMessageBox.aboutQt(self, '关于Qt')
        if self.subwin_aam.lineedit_cmd.hasFocus():
            if event.key() == Qt.Key_Return:
                popen = os.popen(self.subwin_aam.lineedit_cmd.text()).read()
                self.subwin_aam.textedit_log.append(popen)

# file drop
    def dragEnterEvent(self, event):
        drag_path = event.mimeData().urls()[0].toLocalFile()
        ext = os.path.splitext(drag_path)[1]
        # print(os.path.splitext(drag_path)[1])
        if self.tabWidget.currentIndex() == 0 and ext == '.apk':
            event.accept()
            self.drag_file = drag_path
        elif self.tabWidget.currentIndex() == 2:
            event.accept()
            self.drag_file = drag_path
        else:
            event.ignore()
            self.drag_file = ''

    def dropEvent(self, event):
        if self.drag_file:
            if self.tabWidget.currentIndex() == 0:
                if self.subwin_aam.cmb_device.currentText():
                    if QMessageBox.question(self, '拖拽安装', f'你确认将\n{self.drag_file}\n安装到 {self.subwin_aam.cmb_device.currentText()} 上吗？') == QMessageBox.Yes:
                        self.aam_install(self.drag_file)
                else:
                    QMessageBox.warning(self, '警告', '请先连接设备')
            elif self.tabWidget.currentIndex() == 2:
                if event.pos().x() <= self.width()//2:
                    self.subwin_fhc.lineedit_A.setPlainText(f'file:{self.drag_file}')
                else:
                    self.subwin_fhc.lineedit_B.setPlainText(f'file:{self.drag_file}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    path = os.path.expandvars(r'%appdata%/Avoconal')
    window = Main()

    import dark
    dark.apply_dark(app)

    sys.exit(app.exec())
