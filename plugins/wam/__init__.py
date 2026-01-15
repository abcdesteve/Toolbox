from typing import Literal
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from qfluentwidgets import *

import threading
from multiprocessing.pool import ThreadPool,Pool
from multiprocessing import cpu_count,Process

import winreg
import re
import time,logging

from .app_manager_ui import Ui_app_manager

from sl_lib import *

# 池中批量处理的函数必须是全局函数，不得依赖其他类
def calc_handler(info: tuple[str, str])-> tuple[str, str]:
    dir, path = info
    try:
        temp = sltk.bit2size(calc_size(path))
        return dir, temp
    except:
        return dir, '无法计算'


def calc_size(path):
    size = 0
    for i in os.listdir(path):
        obj = os.path.join(path, i)
        if os.path.isdir(obj):
            size += calc_size(obj)
        else:
            size += os.path.getsize(obj)
    return size

class WAM(QWidget, Ui_app_manager):
    def __init__(self, mainwindow, path: str):
        super().__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow
        self.path = path

        self.btn_backup.setIcon(FluentIcon.HISTORY)
        self.btn_restore.setIcon(FluentIcon.CANCEL)
        self.btn_open_folder.setIcon(FluentIcon.FOLDER)
        self.btn_open_reg.setIcon(FluentIcon.LABEL)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_refresh.setIcon(FluentIcon.SYNC)

        self.menu_reg = RoundMenu("", self.btn_open_reg.button)
        action_user_reg = Action('打开用户应用注册表')
        action_user_reg.triggered.connect(lambda: self.open_reg('user'))
        self.menu_reg.addAction(action_user_reg)

        self.cmb_folder.addItem('全部位置')
        self.cmb_folder.addItem('仅注册表')

        self.app_info: dict[str, dict[str, str]] = {}
        '''
        e.g. {
        'everything':
            {'icon':'',
            'main':'D://Everything//Everything.exe',
            'uninst':'D://Everything//uninst.exe',
            'version':'1.4.1.932',
            'install_date':'2023-01-01',
            'type':'global/user',
            'status':'both/reg/folder/ignore'}
        }
        '''
        self.app_size_cache:dict[str,str]={}

        self.timer_app_size = QTimer()
        self.timer_app_size.timeout.connect(self.refresh_app_info)
        self.timer_app_size.setInterval(2000)

        self.table_app_info.horizontalHeader().setSectionsMovable(True)
        self.init_signal()
        self.load_app_info()


    def init_signal(self):
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_add_folder.clicked.connect(self.change_btn_statues)
        self.btn_del_folder.clicked.connect(
            lambda: self.cmb_folder.removeItem(self.cmb_folder.currentIndex()))
        self.btn_del_folder.clicked.connect(self.change_btn_statues)
        self.cmb_folder.currentTextChanged.connect(self.change_btn_statues)

        self.btn_open_reg.clicked.connect(self.open_reg)
        self.btn_open_reg.dropButton.clicked.connect(lambda: self.menu_reg.popup(
            QPoint(-self.menu_reg.width(), 0)+self.btn_open_reg.dropButton.mapToGlobal(self.btn_open_reg.dropButton.pos())))
        self.btn_refresh.clicked.connect(self.scan_app_info)

    def add_folder(self):
        temp = QFileDialog().getExistingDirectory()
        if temp:
            sltk.unique_add_items(self.cmb_folder, temp)
        else:
            QMessageBox.warning(self, '提示', '文件夹无效')

    def change_btn_statues(self):
        flag=self.cmb_folder.count()>2 and self.cmb_folder.currentIndex()>1
        self.btn_del_folder.setEnabled(flag)

    def open_reg(self, reg_type: Literal["global", "user"] = 'global'):
        if reg_type == 'global':
            path = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        elif reg_type == 'user':
            path = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall"
        os.system(
            f"""reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit" /v LastKey /t REG_SZ /d {path} /f""")
        threading.Thread(target=lambda: os.system('regedit')).start()

    def try_query_reg(self, key, sub_key, value_name):
        try:
            with winreg.OpenKey(key, sub_key) as reg_key:
                result: str = winreg.QueryValueEx(reg_key, value_name)[0]
                return result.replace('"', '')
        except FileNotFoundError:
            logging.error(f"注册表项 {sub_key} 或值 {value_name} 不存在")
            pass
        except PermissionError:
            logging.error(f"没有权限访问注册表项 {sub_key}")
            pass
        except Exception as e:
            print(f"发生错误: {e}")
        return ''

    def scan_app_info(self):
        # 1.扫描注册表获取全部应用数据
        # 2.验证注册表指向的文件是否存在
        # 3.扫描cmb_folder中的文件夹，找出注册表中缺漏的项
        self.btn_refresh.setEnabled(False)
        # 扫描应用文件夹，找出main.exe与uninst.exe
        scan_data: dict[str, dict[str, str]] = {}
        folder = self.cmb_folder.currentText()
        # for app_name in os.listdir(folder):
        #     if os.path.isdir(os.path.join(folder, app_name)):
        #         if app_name not in list(self.app_info.keys()):
        #             lis_rel_exe=sltk.scan_file(os.path.join(folder, app_name),'.exe',3,False)
        #             lis_rel_exe=[os.path.relpath(i,sltk.join_path(folder,app_name)) for i in lis_rel_exe if i.endswith('.exe')] # 转相对路径
        #             if (app_name+'.exe').lower() in [os.path.basename(i).lower() for i in lis_rel_exe]:
        #                 main_file=app_name+'.exe'
        #             elif len(lis_rel_exe)==1:
        #                 main_file=lis_rel_exe[0]
        #             else:
        #                 if len(lis_rel_exe)==0:
        #                     lis_rel_exe=sltk.scan_file(os.path.join(folder, app_name),'.exe',6,False)
        #                     lis_rel_exe=[os.path.relpath(i,sltk.join_path(folder,app_name)) for i in lis_rel_exe if i.endswith('.exe')] # 转相对路径
        #                 main_file=InputDialog().run(self,f'选择 {app_name} 的🏠主程序','请从下列列表中选择应用的主程序或手动输入主程序相对路径',lis_rel_exe)
        #             uninstaller_file=[i for i in lis_rel_exe if 'unins' in i.lower()]
        #             if len(uninstaller_file)>1: # 找不到/有多个结果
        #                 uninstaller_file=InputDialog().run(self,f'选择 {app_name} 的🗑️卸载程序','请从下列列表中选择卸载程序或手动输入卸载程序相对路径',uninstaller_file)
        #             elif len(uninstaller_file)==0:
        #                 uninstaller_file=''
        #             else:
        #                 uninstaller_file=uninstaller_file[0]
        #             main_file=sltk.join_path(folder,app_name,main_file) if main_file else ''
        #             uninstaller_file=sltk.join_path(folder,app_name,uninstaller_file) if uninstaller_file else ''
        #             scan_data[app_name]=(main_file,uninstaller_file)

        # 扫描注册表
        for reg_type in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
            for reg_path in [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall']:
                with winreg.OpenKey(reg_type, reg_path) as reg_key:
                    app_list = [winreg.EnumKey(reg_key, i) for i in range(
                        winreg.QueryInfoKey(reg_key)[0])]
                for app in app_list:
                    app_icon = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'DisplayIcon')
                    app_name = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'DisplayName').replace('版本', '')
                    app_version = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'DisplayVersion')
                    app_install_date = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'InstallDate')
                    app_main_file = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'DisplayIcon')
                    app_main_file = app_main_file if app_main_file.endswith(
                        '.exe') else ''
                    app_uninst_file = self.try_query_reg(
                        reg_type, reg_path+'\\'+app, 'UninstallString').strip()
                    # app_uninst_file = [i for i in app_uninst_file.split('\"') if i][0]
                    app_uninst_file = (app_uninst_file.split('\"')+[''])[1]

                    # 从应用名中删除版本号
                    temp = re.search(
                        r"(v?\d+[\.\-_]\d+(?:[\.\-_]\d+)*)", app_name)
                    if temp:
                        temp = temp.group(1)
                        app_name = re.sub(temp, '', app_name)
                        app_name = re.sub(" {2,}", ' ', app_name)
                        app_name = re.sub(r'[\s-]+$', '', app_name).strip()
                    else:
                        temp = ''
                    if not app_version:
                        app_version = temp

                    # 部分应用的图标写成 `*.exe,0` 需要剔除无用参数
                    app_icon = app_icon.split(',')[0].strip()
                    app_main_file = app_main_file.split(',')[0].strip()
                    # 删除版本号前的 `v`
                    app_version = app_version.replace('v', '').strip()

                    # 在缺少数据的情况之下让 主程序 与 图标 互相补充路径
                    if not app_icon:
                        if app_main_file:
                            app_icon = app_main_file
                    if not app_main_file:
                        if app_icon.endswith('.exe'):
                            app_main_file = app_icon

                    # 格式化安装日期
                    if app_install_date:
                        app_install_date = re.sub('\D', '', app_install_date)
                        try:
                            app_install_date = time.strptime(
                                app_install_date, r'%m%d%Y')
                        except:
                            try:
                                app_install_date = time.strptime(
                                    app_install_date, r'%Y%m%d')
                            except:
                                QMessageBox.warning(
                                    self, '错误', f'无法解析日期 {app_install_date}')
                        app_install_date = time.strftime(
                            '%Y/%m/%d', app_install_date)

                    if app_name or app_version or app_install_date or app_main_file or app_uninst_file:
                        scan_data[app_name] = {'icon': app_icon,
                                               'main': app_main_file,
                                               'uninst': app_uninst_file,
                                               'version': app_version,
                                               'install_date': app_install_date,
                                               'type': 'global'if reg_type == winreg.HKEY_LOCAL_MACHINE else 'user',
                                               'status': 'reg'}
        # 原有数据保持不变，合入新增数据
        for i in scan_data.keys():
            if i not in self.app_info:
                self.app_info[i]=scan_data[i]

        self.save_app_info()

        threading.Thread(target=self.calc_app_size).start()
        # Process(target=self.calc_app_size).start()

        self.timer_app_size.start()

    def refresh_app_info(self):
        # ResizeToContents不要长期打开，第二次刷新时会直接卡死
        self.table_app_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.table_app_info.clearContents()
        self.table_app_info.setRowCount(len(self.app_info))
        flag_size_done=True
        for i in range(len(self.app_info)):
            app_name, app_info = list(self.app_info.items())[i]
            app_icon, app_main_file, app_uninst_file, app_version, app_install_date, app_type, app_status = app_info['icon'], app_info[
                'main'], app_info['uninst'], app_info['version'], app_info['install_date'], app_info['type'], app_info['status']

            if app_icon:
                app_icon = QFileIconProvider().icon(QFileInfo(app_icon))
            else:
                app_icon = FluentIcon.icon(FluentIcon.APPLICATION)
            self.table_app_info.setItem(
                i, 0, QTableWidgetItem(app_icon, app_name))
            self.table_app_info.setItem(i, 1, QTableWidgetItem(app_version))
            self.table_app_info.setItem(i, 2, QTableWidgetItem(app_main_file))
            self.table_app_info.setItem(
                i, 3, QTableWidgetItem(app_install_date))
            self.table_app_info.setItem(i, 4, QTableWidgetItem(self.app_size_cache.get(app_name, '计算中……')))
            if app_name not in self.app_size_cache:
                flag_size_done=False
            self.table_app_info.setItem(i, 5, QTableWidgetItem(app_type))
            self.table_app_info.setItem(i, 6, QTableWidgetItem(app_status))
            
        if flag_size_done:
            self.timer_app_size.stop()
            self.table_app_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def calc_app_size(self):
        task_list=[]
        for i in list(self.app_info.keys()):
            if i not in self.app_size_cache:
                task_list.append((i,os.path.dirname(self.app_info[i]['main'])))

        # 单线程27s，多线程23s，多进程17s
        with Pool(max(cpu_count()//2,1)) as pool:
            for app_name, size in pool.imap(calc_handler, task_list):
                self.app_size_cache[app_name] = size
                # self.table_app_info.setItem(app_name, 4, QTableWidgetItem(size))
                # self.update()
                # time.sleep(0.1) # 旧方案：同步刷新时引入延迟以等待界面更新，防止扫盘长时间吃满CPU
        self.btn_refresh.setEnabled(True)

    def load_app_info(self):
        try:
            with open(sltk.join_path(self.path, 'wam.json'), 'r', encoding='utf-8') as f:
                data = json.load(f)
                sltk.unique_add_items(self.cmb_folder, data['sources'], False)
                self.app_info = data['app_info']
            threading.Thread(target=self.calc_app_size).start()

            self.timer_app_size.start()
        except:pass
            
    def save_app_info(self):
        with open(sltk.join_path(self.path, 'wam.json'), 'w', encoding='utf-8') as f:
            data = {'sources': sltk.expend_children_text(
                self.cmb_folder)[2:], 'app_info': self.app_info}
            json.dump(data, f)


class Utility(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setObjectName('container')
        # self.container=QWidget(self)
        # self.container.setObjectName('container')
        self.setStyleSheet('QWidget#container{background-color:transparent}')
        self.expandLayout = ExpandLayout(self)
        # self.container.setLayout(self.expandLayout)
        self.setLayout(self.expandLayout)

        self.gp_startup = SettingCardGroup('「启动」文件夹', self)
        self.btn_user_startup = PushButton('用户「启动」文件夹')
        self.btn_global_startup = PrimaryPushButton('全局「启动」文件夹')
        self.wrapper_startup = QWidget()
        self.layout_startup = QHBoxLayout()
        self.wrapper_startup.setLayout(self.layout_startup)
        self.layout_startup.addWidget(self.btn_user_startup)
        self.layout_startup.addWidget(self.btn_global_startup)
        self.gp_startup.addSettingCard(self.wrapper_startup)
        self.expandLayout.addWidget(self.gp_startup)

        self.gp_menu = SettingCardGroup('「开始菜单」文件夹', self)
        self.btn_user_menu = PushButton('用户「启动」文件夹')
        self.btn_global_menu = PrimaryPushButton('全局「启动」文件夹')
        self.gp_menu.addSettingCards(
            [self.btn_user_menu, self.btn_global_menu])
        self.expandLayout.addWidget(self.gp_menu)
        self.show()
