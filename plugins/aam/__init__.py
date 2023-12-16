from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from qfluentwidgets import *

from .aam_ui import Ui_aam
from .wireless_ui import Ui_wireless

from sl_lib import *

import os
import sys
import zipfile
import threading,subprocess


class AAM(QWidget, Ui_aam):
    """Android application manager"""

    def __init__(self, mainwindow: QMainWindow, parent_dir: str):
        super().__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.subwin_wireless = Wireless(self)

        self.ckb_app_user.setOnText('用户应用')
        self.ckb_app_user.setOffText('用户应用')
        self.ckb_app_sys.setOnText('系统应用')
        self.ckb_app_sys.setOffText('系统应用')

        self.app_ver=StatisticsWidget('应用版本')
        self.horizontalLayout.addWidget(self.app_ver)
        self.device_sys_ver = StatisticsWidget('安卓版本')
        self.layout_device_info.addWidget(self.device_sys_ver)
        self.device_app_cout = StatisticsWidget('应用数量')
        self.layout_device_info.addWidget(self.device_app_cout)

        self.INSIDE_DIR = parent_dir
        'using `__file__` of parent which will direct to the dir *inside* the program'
        self.NEAR_DIR = os.path.dirname(sys.argv[0])
        'using `sys.argv[0]` which will direct to the dir *near* the program'
        self.adb_path = lambda flag=False: sltk.join_path(
            self.INSIDE_DIR, 'adb.exe')+(f' -s {self.cmb_device.currentText()}' if flag else '')
        'when `flag` is `True`, a specific device is returned'

        self.init_icon()
        self.init_signal()

    def init_icon(self):
        self.btn_device.setIcon(FluentIcon.SYNC)
        self.btn_wireless.setIcon(FluentIcon.DEVELOPER_TOOLS)
        self.btn_getapp_low.setIcon(FluentIcon.SEARCH)
        self.btn_getapp_high.setIcon(FluentIcon.SEARCH)
        self.btn_clear.setIcon(FluentIcon.BROOM)

        self.btn_launch.setIcon(FluentIcon.PLAY)
        self.btn_extract.setIcon(FluentIcon.ZIP_FOLDER)
        self.btn_install.setIcon(FluentIcon.APPLICATION)
        self.btn_uninstall.setIcon(FluentIcon.APPLICATION)
        self.btn_freeze.setIcon(FluentIcon.FRIGID)
        self.btn_unfreeze.setIcon(FluentIcon.FRIGID)
        self.btn_backup.setIcon(FluentIcon.HISTORY)
        self.btn_restore.setIcon(FluentIcon.HISTORY)
        self.btn_grant_permission.setIcon(FluentIcon.)

    def init_signal(self):
        self.btn_wireless.clicked.connect(self.subwin_wireless.show)
        self.btn_device.clicked.connect(self.update_device_connection)
        self.btn_getapp_high.clicked.connect(self.aam_getapp_high)
        self.btn_getapp_low.clicked.connect(self.aam_getapp_low)
        self.btn_clear.clicked.connect(self.textedit_log.clear)
        self.btn_launch.clicked.connect(self.aam_launch)
        self.btn_extract.clicked.connect(self.aam_extract)
        self.btn_install.clicked.connect(self.aam_install)
        self.btn_uninstall.clicked.connect(self.aam_uninstall)
        self.btn_freeze.clicked.connect(self.aam_freeze)
        self.btn_unfreeze.clicked.connect(self.aam_unfreeze)
        self.btn_backup.clicked.connect(self.aam_backup)
        self.btn_restore.clicked.connect(self.aam_restore)

        self.ckb_app_user.checkedChanged.connect(self.update_device_app)
        self.ckb_app_sys.checkedChanged.connect(self.update_device_app)

        self.cmb_device.currentIndexChanged.connect(self.update_device_app)
        self.cmb_app.textChanged.connect(self.update_app_info)

    def update_wireless_connect(self, ip, port):
        try:
            log = os.popen(f'''{self.adb_path()} connect {ip}:{port}''').read()
            self.textedit_log.append(log)
            # if self.cmb_device.findText(f"{ip}:{port}") == -1:
            #     QMessageBox.warning(self.mainwindow, "警告", "未能成功连接")
        except:
            pass
        QMetaObject.invokeMethod(
            self, "update_device_connection", Qt.QueuedConnection)

    @Slot()
    def update_device_connection(self):
        '刷新连接设备'
        log = os.popen(f"{self.adb_path()} devices").read()
        self.textedit_log.append(log)
        self.cmb_device.clear()
        if log.count("device") > 1:
            for i in log.split("\n")[1:]:
                if i:
                    self.cmb_device.addItem(i.split("\t")[0])
            self.cmb_device.setCurrentIndex(0)
            self.update_device_app()
        else:
            QMessageBox.warning(self.mainwindow, "警告", "设备连接失败")

    def update_device_info(self):
        '刷新设备信息'
        try:
            self.device_sys_ver.setValue(os.popen(
                f'{self.adb_path(True)} shell getprop ro.build.version.release').read())
        except:
            self.device_sys_ver.setValue()
        try:
            self.device_app_cout.setValue(str(len(self.cmb_app.lis)))
        except:
            self.device_app_cout.setValue()

    def update_device_app(self):
        '刷新应用列表'
        if self.cmb_device.currentText():
            filter = {(False, False): 'empty', (True, False): '-3', (False, True): '-s',
                      (True, True): ''}[(self.ckb_app_user.isChecked(), self.ckb_app_sys.isChecked())]
            if filter != 'empty':
                log = os.popen(
                    f'''{self.adb_path(True)} shell pm list package {filter}''').read()
                # self.textedit_log.append(log)

                self.cmb_app.lis: list[str] = [i[8:]
                                               for i in log.split("\n") if i]
                temp = QCompleter(self.cmb_app.lis, self.cmb_app)
                temp.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
                self.cmb_app.setCompleter(temp)
                if self.cmb_app.text() not in self.cmb_app.lis:
                    self.cmb_app.setText(self.cmb_app.lis[0])
            self.update_device_info()
        else:
            QMessageBox.warning(self.mainwindow, "警告", "无法获取应用列表，请先连接设备")

    def update_app_info(self):
        '刷新应用详情'
        def name(txt):
            self.label_app_name.setText(txt)
            # self.label_app_name.setText(subprocess.run(
            #     f'''{sltk.join_path(self.INSIDE_DIR,'aapt.exe')} dump badging {zip_path} | findstr "application-label"''',stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8',shell=True).stdout.split(':')[1][1:-2])

        def icon(icon_relpath):
            try:
                # icon_relpath = os.popen(
                #     f'''{sltk.join_path(self.INSIDE_DIR,'aapt.exe')} dump badging {zip_path} | findstr "application-icon"''').readlines()[0].split(':')[1][1:-2]
                destination_folder = sltk.join_path(self.NEAR_DIR, "app_extract_icon")
                os.system(
                    f'''rmdir "{sltk.join_path(self.NEAR_DIR,'app_extract_icon')}" /q /s''')
                # 打开 ZIP 文件
                with zipfile.ZipFile(zip_path, "r") as zip_file:
                    zip_file.extract(icon_relpath, destination_folder)
                    self.label_app_icon.setPixmap(
                        QPixmap(sltk.join_path(self.NEAR_DIR, 'app_extract_icon', icon_relpath)))
                    # last 没有设置pixmap
                    # # 搜索并提取指定文件
                    # for file_info in zip_file.infolist():
                    #     if file_info.filename.endswith(file_to_extract):
                    #         zip_file.extract(
                    #             file_info, destination_folder)  # 提取文件到指定文件夹
                    #         print("图标提取成功")
                    #         self.label_app_icon.setPixmap(QPixmap(sltk.scan_file(
                    #             sltk.join_path(self.NEAR_DIR, 'app_icon'), file_to_extract, 5)[0]))
                    #         break
                    # else:
                    #     print("未找到指定图标")
            except:
                pass
        def version(txt):
            self.app_ver.setValue(txt)
            # self.app_ver.setValue(subprocess.run(
            #     f'''{sltk.join_path(self.INSIDE_DIR,'aapt.exe')} dump badging {zip_path} | findstr "versionName"''',stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8',shell=True).stdout.split('versionName=')[1][1:-2])


        if self.cmb_device.currentText() and self.cmb_app.text() in self.cmb_app.lis:
            self.label_app_name.clear()
            self.label_app_icon.clear()
            self.app_ver.setValue()
            
            zip_path = self.aam_extract(silence=True)  # ZIP 文件的路径
            try:
                # shell控制 | 管道符是否可用
                result=subprocess.run(f'''{sltk.join_path(self.INSIDE_DIR,'aapt.exe')} dump badging {zip_path}''',stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8',errors='ignore',shell=True).stdout.splitlines()
                # self.textedit_log.append('\n'.join(result))
                threading.Thread(target=name, name='get_app_name',args=[i.split(':')[1][1:-1] for i in result if 'application-label'in i][0:1]).start()
                threading.Thread(target=icon, name='get_app_icon',args=[i.split(':')[1][1:-1] for i in result if 'application-icon'in i][0:1]).start()
                threading.Thread(target=version, name='get_app_version',args=[i.split('versionName=')[1][1:-1] for i in result if 'versionName'in i][0:1]).start()
            except:pass

    def aam_getapp_high(self):
        log = os.popen(
            f'''{self.adb_path(True)} shell dumpsys activity |findstr "mResumedActivity"'''
        ).read()
        if "ActivityRecord" in log:
            self.textedit_log.append(log)
            log = log.split(" ")[7].split("/")[0]
            self.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "无法获取包名，确保手机处于亮屏状态")

    def aam_getapp_low(self):
        log = os.popen(
            f'''{self.adb_path(True)} shell dumpsys activity |findstr "mFocusedActivity"'''
        ).read()
        if "ActivityRecord" in log:
            self.textedit_log.append(log)
            log = log.split(" ")[7].split("/")[0]
            self.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "无法获取包名，确保手机处于亮屏状态")

    def aam_launch(self):
        if self.cmb_app.text():
            # 获取activity
            log = os.popen(
                f'''{self.adb_path(True)} shell monkey -p {self.cmb_app.text()} -v -v -v 1 | findstr "cmp="'''
            ).read()
            # 启动应用
            log = os.popen(
                f'''{self.adb_path(True)} shell am start -n {log.split("cmp=")[1].split(" }")[0]}'''
            ).read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_extract(self, silence=False) -> str:
        '''return .apk path in the computer like `D:\\Users\\abcdesteve\\Desktop\\神龙\\神龙工具箱\\神龙工具箱v2.0\\base-master.apk`'''
        if self.cmb_app.text():
            # path = QFileDialog.getExistingDirectory(self, "请选择保存位置")
            apk_path = sltk.join_path(self.NEAR_DIR, 'extract_apks')  # 无法指定位置
            if apk_path:
                if not os.path.exists(apk_path):
                    os.mkdir(apk_path)
                os.chdir(apk_path)
                apk_file_name = os.popen(
                    f'''{self.adb_path(True)} shell pm path {self.cmb_app.text()}''').readline().lstrip('package:').rstrip()
                log = os.popen(
                    f'''{self.adb_path(True)} pull {apk_file_name} {apk_path}''').read()
                if not silence:
                    self.textedit_log.append(log)
                return sltk.join_path(apk_path, os.path.split(apk_file_name)[1])

        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_install(self, apk=""):
        if self.cmb_device.currentText():
            if apk:
                log = os.popen(
                    f'''{self.adb_path(True)} install "{apk}"'''
                ).read()
                self.textedit_log.append(log)
            else:
                path = QFileDialog.getOpenFileName(
                    self, "请选择安装包", filter="安卓安装包 (*.apk)"
                )[0]
                if path:
                    log = os.popen(
                        f'''{self.adb_path(True)} install "{path}"'''
                    ).read()
                    self.textedit_log.append(log)
                else:
                    QMessageBox.warning(self.mainwindow, "警告", "路径无效")
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先连接设备")

    def aam_uninstall(self):
        if self.cmb_app.text():
            log = os.popen(
                f'''{self.adb_path(True)} uninstall {self.cmb_app.text()}'''
            ).read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_freeze(self):
        if self.cmb_app.text():
            log = os.popen(
                f'''{self.adb_path(True)} shell pm disable-user {self.cmb_app.text()}'''
            ).read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_unfreeze(self):
        if self.cmb_app.text():
            log = os.popen(
                f'''{self.adb_path(True)} shell pm enable {self.cmb_app.text()}'''
            ).read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_backup(self):
        if self.cmb_app.text():
            path = QFileDialog.getSaveFileName(
                self, "请选择备份文件保存位置", filter="安卓应用备份文件 (*.ab)"
            )[0]
            if path:
                # -apk 含安装包备份
                log = os.popen(
                    f'''{self.adb_path(True)} backup -nosystem -noshared -f "{path}" {self.cmb_app.text()}'''
                ).read()
                self.textedit_log.append(log)
            else:
                QMessageBox.warning(self.mainwindow, "警告", "路径无效")
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写应用包名")

    def aam_restore(self):
        if self.cmb_app.text():
            path = QFileDialog.getOpenFileName(
                self, "请选择恢复文件位置", filter="安卓应用备份文件 (*.ab)"
            )[0]
            if path:
                log = os.popen(
                    f'''{self.adb_path(True)} restore "{path}"'''
                ).read()
                self.textedit_log.append(log)
            else:
                QMessageBox.warning(self.mainwindow, "警告", "路径无效")
        else:
            QMessageBox.warning(self.mainwindow, "警告", "请先填写备份文件路径")

    # def keyPressEvent(self, event):
    #     if self.lineedit_cmd.hasFocus():
    #         if event.key() == Qt.Key_Return:
    #             popen = os.popen(self.lineedit_cmd.text()).read()
    #             self.textedit_log.append(popen)


class Wireless(QMainWindow, Ui_wireless):
    def __init__(self, parent: AAM):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.parent_window = parent

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
            self.hide()

    def hideEvent(self, event):
        # self.hide()
        threading.Thread(target=self.parent_window.update_wireless_connect, args=[
                         self.lineedit_ip.text(), self.lineedit_port.text()]).start()
