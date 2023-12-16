import os
import sys
import qdarkstyle
from PySide6.QtWidgets import *
from ui_gui import Ui_gui


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.aab_btn_device.clicked.connect(self.aab_connect)
        self.aab_btn_path.clicked.connect(self.aab_select_path)
        self.aab_btn_getapp_high.clicked.connect(self.aab_getapp_high)
        self.aab_btn_getapp_low.clicked.connect(self.aab_getapp_low)
        self.aab_btn_clear.clicked.connect(self.aab_textedit_log.clear)
        self.aab_btn_backup.clicked.connect(self.aab_backup)
        self.aab_btn_restore.clicked.connect(self.aab_restore)

        self.csl_btn_to.clicked.connect(self.csl_select_to)
        self.csl_btn_from.clicked.connect(self.csl_select_from)
        self.csl_btn_start.clicked.connect(self.csl_start)

        self.show()


# aab

    def aab_connect(self):
        log = os.popen('adb devices').read()
        self.aab_textedit_log.appendPlainText(log)
        self.aab_cmb_device.clear()
        if log.count('device') > 1:
            for i in log.split('\n')[1:]:
                if i:
                    self.aab_cmb_device.addItem(i.split('\t')[0])
        else:
            QMessageBox.warning(self, '警告', '设备连接失败')

    def aab_select_path(self):
        path = QFileDialog.getSaveFileName(self, '请选择备份文件路径', filter='*.ab')[0]
        if path:
            self.aab_label_path.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def aab_getapp_high(self):
        log = os.popen(
            f'adb -s {self.aab_cmb_device.currentText()} shell dumpsys activity |findstr "mResumedActivity"').read()
        if 'ActivityRecord' in log:
            self.aab_textedit_log.appendPlainText(log)
            log = log.split(' ')[7].split('/')[0]
            self.aab_lineedit_name.setText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aab_getapp_low(self):
        log = os.popen(
            f'adb -s {self.aab_cmb_device.currentText()} shell dumpsys activity |findstr "mFocusedActivity"').read()
        if 'ActivityRecord' in log:
            self.aab_textedit_log.appendPlainText(log)
            log = log.split(' ')[7].split('/')[0]
            self.aab_lineedit_name.setText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aab_backup(self):
        if self.aab_label_path.text() and self.aab_lineedit_name.text():
            log = os.popen(
                f"adb -s {self.aab_cmb_device.currentText()} backup -nosystem -noshared {'-apk'if self.aab_ckb_apk.isChecked() else ''} -f {self.aab_label_path.text()} {self.aab_label_name.text()}").read()
            self.aab_textedit_log.appendPlainText(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写备份文件路径与包名')

    def aab_restore(self):
        if self.aab_label_path.text():
            log = os.popen(
                f'adb -s {self.aab_cmb_device.currentText()} restore {self.aab_label_path.text()}').read()
            self.aab_textedit_log.appendPlainText(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写备份文件路径')

# csl
    def csl_select_from(self):
        path = QFileDialog.getExistingDirectory(self, '请选择本体路径')
        if path:
            self.csl_lineedit_from.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_select_to(self):
        path = QFileDialog.getExistingDirectory(self, '请选择目标路径')
        if path:
            self.csl_lineedit_to.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_start(self):
        if self.csl_lineedit_from.text() and self.csl_lineedit_to.text():
            log = os.popen(
                f'mklink /j "{self.csl_lineedit_to.text()}" "{self.csl_lineedit_from.text()}"').read()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = Main()
    sys.exit(app.exec())
