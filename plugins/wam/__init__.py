from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from qfluentwidgets import *

from typing import Literal
import threading

import winreg,re

from .app_manager_ui import Ui_app_manager

from sl_lib import *


class WAM(QWidget, Ui_app_manager):
    def __init__(self,mainwindow,path:str):
        super().__init__()
        self.setupUi(self)

        self.mainwindow=mainwindow
        self.path=path

        self.btn_backup.setIcon(FluentIcon.HISTORY)
        self.btn_restore.setIcon(FluentIcon.CANCEL)
        self.btn_open_folder.setIcon(FluentIcon.FOLDER)
        self.btn_open_reg.setIcon(FluentIcon.LABEL)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_refresh.setIcon(FluentIcon.SYNC)

        self.menu_reg=RoundMenu("", self.btn_open_reg.button)
        action_user_reg=Action('打开用户应用注册表')
        action_user_reg.triggered.connect(lambda:self.open_reg('user'))
        self.menu_reg.addAction(action_user_reg)

        self.app_info:dict[str,dict[str,str]]={}
        '''
        e.g. {
        'everything':
            {'main':'D://Everything//Everything.exe',
            'uninst':'D://Everything//uninst.exe',
            'version':'1.4.1.932',
            'install_date':'2023-01-01',
            'space':'100MB',
            'type':'global',
            'status':'both/reg/folder/ignore'}
        }
        '''

        self.table_app_info.horizontalHeader().setSectionsMovable(True)

        self.init_signal()

    def init_signal(self):
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_add_folder.clicked.connect(self.folders_count_changed)
        self.btn_del_folder.clicked.connect(
            lambda: self.cmb_folder.removeItem(self.cmb_folder.currentIndex()))
        self.btn_del_folder.clicked.connect(self.folders_count_changed)

        self.btn_open_reg.clicked.connect(self.open_reg)
        self.btn_open_reg.dropButton.clicked.connect(lambda:self.menu_reg.popup(QPoint(-self.menu_reg.width(),0)+self.btn_open_reg.dropButton.mapToGlobal(self.btn_open_reg.dropButton.pos())))
        self.btn_refresh.clicked.connect(self.scan_app_info)
        

    def add_folder(self):
        temp = QFileDialog().getExistingDirectory()
        if temp:
            sltk.unique_add_items(self.cmb_folder, temp)
        else:
            QMessageBox.warning(self, '提示', '文件夹无效')

    def folders_count_changed(self):
        self.btn_del_folder.setEnabled(self.cmb_folder.count() > 0)
        self.btn_backup.setEnabled(self.cmb_folder.count() > 0)
        self.btn_refresh.setEnabled(self.cmb_folder.count() > 0)

    def open_reg(self,reg_type:Literal["global","user"]='global'):
        if reg_type=='global':
            path=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        elif reg_type=='user':
            path=r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall"
        os.system(f"""reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit" /v LastKey /t REG_SZ /d {path} /f""")
        threading.Thread(target=lambda:os.system('regedit')).start()

    def try_query_reg(self, key, sub_key, value_name):
        try:
            with winreg.OpenKey(key, sub_key) as reg_key:
                return winreg.QueryValueEx(reg_key, value_name)[0]
        except FileNotFoundError:
            print(f"注册表项 {sub_key} 或值 {value_name} 不存在")
        except PermissionError:
            print(f"没有权限访问注册表项 {sub_key}")
        except Exception as e:
            print(f"发生错误: {e}")
        return ''
    

    def scan_app_info(self):
        # 1.扫描注册表获取全部应用数据
        # 2.验证注册表指向的文件是否存在
        # 3.扫描cmb_folder中的文件夹，找出注册表中缺漏的项

        # 扫描应用文件夹，找出main.exe与uninst.exe
        scan_data:dict[str,dict[str,str]]={}
        folder=self.cmb_folder.currentText()
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
        for reg_path in [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall']:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as reg_key:
                app_list=[winreg.EnumKey(reg_key,i) for i in range(winreg.QueryInfoKey(reg_key)[0])]
            for app in app_list:
                app_name=self.try_query_reg(winreg.HKEY_LOCAL_MACHINE,reg_path+'\\'+app,'DisplayName')
                app_version=self.try_query_reg(winreg.HKEY_LOCAL_MACHINE,reg_path+'\\'+app,'DisplayVersion')
                app_install_date=self.try_query_reg(winreg.HKEY_LOCAL_MACHINE,reg_path+'\\'+app,'InstallDate')
                main_file=self.try_query_reg(winreg.HKEY_LOCAL_MACHINE,reg_path+'\\'+app,'DisplayIcon')
                main_file=main_file if main_file.endswith('.exe') else ''
                uninstaller_file=self.try_query_reg(winreg.HKEY_LOCAL_MACHINE,reg_path+'\\'+app,'UninstallString')
                uninstaller_file=(uninstaller_file.split('\"')+[''])[1]
                if app_name or app_version or app_install_date or main_file or uninstaller_file:
                    scan_data[app_name]={'main':main_file,
                            'uninst':uninstaller_file,
                            'version':app_version,
                            'install_date':app_install_date,
                            'type':'global',
                            'status':'reg'}
        print(scan_data)
                    


        self.app_info.update(scan_data)
        self.refresh_app_info()
        

    def refresh_app_info(self):
        self.table_app_info.clearContents()
        self.table_update_size()
        self.table_app_info.setRowCount(len(self.app_info))
        for i in range(len(self.app_info)):
            app_name, app_info=list(self.app_info.items())[i]
            main_file,uninstaller_file,app_version,app_install_date,app_type,app_status=app_info['main'],app_info['uninst'],app_info['version'],app_info['install_date'],app_info['type'],app_info['status']
            
            # 从应用名中提取版本号
            temp=re.search(r"(\d+\.\d+(?:\.\d+)*)",app_name)
            if temp:
                app_version=temp.group(1).strip() if app_version=='' else app_version
                app_name=app_name.split(app_version)
                app_name=' '.join([i.strip() for i in app_name])
                app_name=re.sub(r'[\s-]+$','',app_name)

            if main_file:
                icon=QFileIconProvider().icon(QFileInfo(main_file))
            else:
                icon= FluentIcon.icon(FluentIcon.APPLICATION)
            self.table_app_info.setItem(i,0,QTableWidgetItem(icon,app_name))
            self.table_app_info.setItem(i,1,QTableWidgetItem(app_version))
            self.table_app_info.setItem(i,2,QTableWidgetItem(main_file))
            self.table_app_info.setItem(i,3,QTableWidgetItem(app_install_date))
            self.table_app_info.setItem(i,4,QTableWidgetItem(sltk.bit2size(os.path.getsize(os.path.split(main_file)[0])) if main_file else ''))
            self.table_app_info.setItem(i,5,QTableWidgetItem(app_type))
            self.table_app_info.setItem(i,6,QTableWidgetItem(app_status))

    def save_app_info(self):
        with open(sltk.join_path(self.path,'wam.json'),'w',encoding='utf-8') as f:
            data={'sources':sltk.expend_children_text(self.cmb_folder),'app_info':self.app_info}
            json.dump(data,f)

    def table_update_size(self):
        print(self.width())
        self.table_app_info.setColumnWidth(0, self.width()*0.3)
        self.table_app_info.setColumnWidth(1, self.width()*0.1)
        self.table_app_info.setColumnWidth(2, self.width()*0.4)
        self.table_app_info.setColumnWidth(3, self.width()*0.1)
        self.table_app_info.setColumnWidth(4, self.width()*0.1)
        self.table_app_info.setColumnWidth(5, self.width()*0.1)
        self.table_app_info.setColumnWidth(6, self.width()*0.1)
        

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
