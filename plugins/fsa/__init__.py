from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qfluentwidgets.common.icon import FluentIcon
from qfluentwidgets import FluentWindow

from sl_lib import *
import os,json,threading

from .fsa_ui import Ui_fsa
from .snapshot_wizard_ui import Ui_snapshot_wizard

class FSA(QWidget,Ui_fsa):
    """文件快照归档\nfile snapshot archive"""
    def __init__(self,mainwindow,settings_path,parent_dir):
        super().__init__()
        self.setupUi(self)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_crt_snap.setIcon(FluentIcon.CAMERA)
        self.btn_del_snap.setIcon(FluentIcon.DELETE)
        self.btn_export_snap.setIcon(FluentIcon.SHARE)
        # 不知道为啥全局设定无效，必须在这里设置
        # ScrollArea的背景在scrollAreaWidgetContents里
        self.setStyleSheet("QWidget#scrollAreaWidgetContents {background-color:transparent}")

        self.mainwindow = mainwindow
        self.settings_path = settings_path
        self.subwin_snapshot_wizard=SnapshotWizard(self.mainwindow,parent_dir)
        self.init_signal()
        self.read_settings()

    def init_signal(self):
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del_folder.clicked.connect(self.del_folder)
        self.btn_crt_snap.clicked.connect(self.subwin_snapshot_wizard.show)
        self.btn_del_snap.clicked.connect(self.del_snap)
        self.btn_export_snap.clicked.connect(self.export_snap)

        self.cmb_folder.currentTextChanged.connect(self.update_btn_status)
        self.TableWidget.itemSelectionChanged.connect(self.update_btn_status)

    def update_btn_status(self):
        self.btn_del_folder.setEnabled(bool(self.cmb_folder.currentText()))
        self.btn_crt_snap.setEnabled(bool(self.cmb_folder.currentText()))
        self.btn_del_snap.setEnabled(bool(self.TableWidget.selectedItems()))
        self.btn_export_snap.setEnabled(bool(self.TableWidget.selectedItems()))

    def add_folder(self):
        path=QFileDialog.getExistingDirectory(self,"选择快照存档文件夹")
        if not os.path.isdir(path):
            QMessageBox.warning(self,"警告","文件夹无效")
        else:
            sltk.unique_add_items(self.cmb_folder,path)
            config_file=sltk.join_path(path,'index.json')
            if not os.path.isfile(config_file):
                with open(config_file,'w',encoding='utf-8') as f:
                    json.dump({"version":1,"head":"","current":"","snapshots":[]},f)
                    os.makedirs(sltk.join_path(path,'snapshots'),exist_ok=True)
        self.save_settings()

    def del_folder(self):
        temp=self.cmb_folder.currentText()
        self.cmb_folder.removeItem(self.cmb_folder.currentIndex())
        self.save_settings()
        QMessageBox.information(self,"提示",f"成功移除快照存档库 {temp}\n库中的文件仍然存在，可在稍后重新导入")

    def read_settings(self):
        try:
            with open(sltk.join_path(self.settings_path,'fsa.json'),'r',encoding='utf-8') as file:
                data=json.load(file)
                sltk.unique_set_items(self.cmb_folder,data['vaults'])
        except:
            pass

    def save_settings(self):
        os.makedirs(self.settings_path,exist_ok=True)
        with open(sltk.join_path(self.settings_path,'fsa.json'),'w',encoding='utf-8') as file:
            json.dump({"vaults":sltk.expend_children_text(self.cmb_folder)},file)

    def del_snap(self):
        pass

    def export_snap(self):
        pass

class SnapshotWizard(FluentWindow,Ui_snapshot_wizard):
    def __init__(self,mainwindow:QWidget,parent_dir):
        super().__init__()
        self.setAcceptDrops(True)
        self.mainwindow=mainwindow
        self.container = QWidget()
        self.setupUi(self.container)
        self.addSubInterface(self.container,None,"")
        self.setWindowTitle('快照向导')
        self.navigationInterface.setVisible(False)

        self.init_signal()

        self.TreeWidget.setColumnWidth(0,250)

        self.btn_del.setIcon(FluentIcon.DELETE)
        self.btn_add_file.setIcon(FluentIcon.DOCUMENT)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER)
        self.btn_cancel.setIcon(FluentIcon.CANCEL)
        self.btn_create.setIcon(FluentIcon.CAMERA)
        self.toggle_filter.addItem("All",MyFluentIcon.Prohibited)
        self.toggle_filter.addItem("Include",FluentIcon.FILTER)
        self.toggle_filter.addItem("Exclude",FluentIcon.REMOVE_FROM)
        self.toggle_filter.setCurrentItem('Exclude')
        self.toggle_windows.setIcon(QIcon(sltk.join_path(parent_dir,'sl_lib','icons','windows.svg')))
        self.toggle_unix.setIcon(QIcon(sltk.join_path(parent_dir,'sl_lib','icons','linux.svg')))

    def init_signal(self):
        self.btn_cancel.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.create_snap)
        self.btn_add_file.clicked.connect(self.add_file)
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del.clicked.connect(self.del_item)
        self.toggle_filter.currentItemChanged.connect(self.update_filter)

    def file_filter(self,path):
        # 默认放行
        try:
            flag_filter,flag_hidden=True,False
            # 文件夹不需要检测后缀名
            if self.toggle_filter.currentRouteKey()!='All' and os.path.isfile(path):
                is_match=os.path.splitext(path)[1][1:].lower() in self.lineedit_filter.text().lower().split(',')
                flag_filter=(self.toggle_filter.currentRouteKey()=='Include')==is_match

            if self.toggle_windows.isChecked():
                flag_hidden|=os.stat(path).st_file_attributes&0x2
            if self.toggle_unix.isChecked():
                flag_hidden|=os.path.basename(path).startswith('.')
            return flag_filter and not flag_hidden
        except Exception as e:
            print("过滤文件 ",path," 时出现错误，已默认放行：",e)
            return True

    def update_filter(self):
        INCLUDE_EXT='jpg,jpeg,png,heif,heic,avif,jxl,raw,dng'
        EXCLUDE_EXT='lnk,url,ini,conf,config,log,db'
        match self.toggle_filter.currentRouteKey():
            case "All":
                self.lineedit_filter.setDisabled(True)
                if self.lineedit_filter.text() in [INCLUDE_EXT,EXCLUDE_EXT]:
                    self.lineedit_filter.clear()
            case "Include":
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['',EXCLUDE_EXT]:
                    self.lineedit_filter.setText(INCLUDE_EXT)
            case "Exclude":
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['',INCLUDE_EXT]:
                    self.lineedit_filter.setText(EXCLUDE_EXT)

    def create_snap(self):
        pass


    @Slot(int,str)
    def show_scan_error(self,fail_count:int,error:str):
        QMessageBox.information(self,f"{fail_count}个文件添加失败",f"最后的错误信息：\n{error}")

    def add_file(self,path:list[str]=None):
        if not path:
            path=[os.path.realpath(i)for i in QFileDialog.getOpenFileNames(self,"选择一个或多个文件")[0]]
        previous_items=[sltk.join_path(item[1],item[0]) for item in sltk.expend_children_text(self.TreeWidget)]
        fail_count=0
        for i in path:
            try:
                if self.file_filter(i) and i not in previous_items:
                    temp=QTreeWidgetItem()
                    temp.setText(0,os.path.basename(i))
                    temp.setIcon(0,self.map_icon(i,False))
                    temp.setText(1,os.path.dirname(i))
                    # temp.setCheckState(2,Qt.CheckState.Unchecked)
                    temp.setData(0,Qt.ItemDataRole.UserRole,False)
                    temp.setData(1,Qt.ItemDataRole.UserRole,i)
                    temp.setFlags(temp.flags()&~Qt.ItemFlag.ItemIsEditable&~Qt.ItemFlag.ItemIsUserCheckable&~Qt.ItemFlag.ItemIsUserTristate)
                    self.TreeWidget.addTopLevelItem(temp)
                    self.label_count_data.setText(str(int(self.label_count_data.text())+1))
            except Exception as error:
                fail_count+=1
        if fail_count:
            self.show_scan_error(fail_count,error)

    def add_folder(self,path:str=None):
        if not path:
            path=QFileDialog.getExistingDirectory(self,"选择一个文件夹")
        if path:
            path=os.path.realpath(path)
            flag_include_children=QMessageBox.question(self,"是否包含此文件夹内的子文件夹？",path,yes_text="是",no_text="否")
            previous_items=[sltk.join_path(item[1],item[0]) for item in sltk.expend_children_text(self.TreeWidget)]
            
            threading.Thread(target=self.recurse_folder,args=(path,flag_include_children,previous_items)).start()
            # self.recurse_folder(path,flag_include_children,previous_items)
    
    def recurse_folder(self,path:str,flag_include_children:bool,previous_items:list[str],parent:QTreeWidgetItem=None,is_root=True)->tuple[int,str]|None:
        fail_count,error=0,'未捕捉到错误信息'
        if is_root:
            lis=[os.path.basename(path)]
            path=os.path.dirname(path)
        else:
            lis=os.listdir(path)
        for i in lis:
            try:
                item=sltk.join_path(path,i)
                if not self.file_filter(item) or item in previous_items:
                    continue
                temp=QTreeWidgetItem(parent)
                temp.setFlags(temp.flags()&~Qt.ItemFlag.ItemIsEditable&~Qt.ItemFlag.ItemIsUserCheckable&~Qt.ItemFlag.ItemIsUserTristate)
                temp.setText(0,i)

                if os.path.isfile(item):
                    temp.setIcon(0,self.map_icon(i,False))
                    # temp.setCheckState(2,Qt.CheckState.Unchecked)
                    temp.setData(0,Qt.ItemDataRole.UserRole,False)
                    temp.setData(1,Qt.ItemDataRole.UserRole,item)
                    self.label_count_data.setText(str(int(self.label_count_data.text())+1))
                # 二次判断防止无效符号链接
                elif os.path.isdir(item):
                    if flag_include_children or is_root:
                        temp.setIcon(0,self.map_icon(i,True))
                        # temp.setCheckState(2,Qt.CheckState.Checked)
                        temp.setData(0,Qt.ItemDataRole.UserRole,True)
                        temp.setData(1,Qt.ItemDataRole.UserRole,item)
                        count,error=self.recurse_folder(item,flag_include_children,previous_items,temp,False)
                        fail_count+=count
                        if temp.childCount()==0:
                            if parent:
                                parent.removeChild(temp)
                            continue
                    else:
                        if parent:
                            parent.removeChild(temp)
                        continue

                if not parent:
                    # 仅在根节点显示路径，其余路径通过UserRole隐性存储
                    temp.setText(1,path)
                    self.TreeWidget.addTopLevelItem(temp)    
            except Exception as e:
                fail_count+=1
                error=str(e)
        if is_root:
            if fail_count:
                QMetaObject.invokeMethod(self,"show_scan_error",Qt.ConnectionType.QueuedConnection,Q_ARG(int,fail_count),Q_ARG(str,str(error)))
                # QMessageBox.information(self,"提示",f"{fail_count}个文件添加失败\n最后一次错误信息：\n{error}")
        else:
            return fail_count,error

    def calc_file_count(self):
        return sum([0 if item.data(0,Qt.ItemDataRole.UserRole)else 1 for item in self.TreeWidget.findItems("*",Qt.MatchFlag.MatchWildcard|Qt.MatchFlag.MatchRecursive,0)])

    def del_item(self):
        for i in self.TreeWidget.selectedItems():
            if i.parent():
                i.parent().removeChild(i)
            else:
                self.TreeWidget.takeTopLevelItem(self.TreeWidget.indexOfTopLevelItem(i))
        self.label_count_data.setText(str(self.calc_file_count()))

    def map_icon(self,item:str,is_dir:bool)->QIcon:
        if is_dir:
            # 文件夹无图标方便区分
            return QIcon()
            return FluentIcon.FOLDER.icon()
        else:
            if os.path.splitext(item)[1].lower() in['.jpg','.jpeg','.jxl','.png','.apng',
                                                    '.gif','.bmp','.tif','.tiff','.ico',
                                                    '.svg','.webp','.heic','.heif','.avif',
                                                    '.raw','.dng','.img','.cr2','.cr3','.crf']:
                return FluentIcon.PHOTO.icon()
            elif os.path.splitext(item)[1].lower() in['.mp4','.mkv','.avi','.mov','.flv',
                                                      '.wmv','swf','.ts','.mts','.webm',
                                                      '.m2t','.m2ts','.rmvb','.bdmv','.vp6',
                                                      '.vp7','.vp8','.vp9','.vp10','.h264',
                                                      '.h265','.hevc','.h266','.vvc','.av1',
                                                      '.m3u','.m3u8','.srt','.ass']:
                return FluentIcon.MOVIE.icon()
            elif os.path.splitext(item)[1].lower() in['.mp3','.m4a','.flac','.wav','.opus',
                                                      '.wave','.aac','.ogg','.wma','.ape',
                                                      '.pcm','.ac3','.eac3','.dts','.lrc']:
                return FluentIcon.MUSIC.icon()
            elif os.path.splitext(item)[1].lower() in['.lnk','.url']:
                return FluentIcon.LINK.icon()
            elif os.path.splitext(item)[1].lower() in['.txt','.log','.md','.json','.xml',
                                                      '.ini','.yaml','.yml','.toml','.ini',
                                                      '.conf','.cfg','.config','.properties','.prop',
                                                      'htm','.html']:
                return FluentIcon.LABEL.icon()
            else:
                return FluentIcon.DOCUMENT.icon()
    def dragEnterEvent(self, event:QDragEnterEvent):
        event.accept()

    def dropEvent(self, event:QDropEvent):
        lis=event.mimeData().urls()
        if lis:
            for i in lis:
                path=os.path.realpath(i.toLocalFile())
                if os.path.isfile(path):
                    self.add_file([path])
                elif os.path.isdir(path):
                    self.add_folder(path)

    def showEvent(self, e):
        self.mainwindow.hide()
        self.resize(600,400)
        return super().showEvent(e)
    
    def closeEvent(self, e):
        if self.TreeWidget.topLevelItemCount()>0:
            if not QMessageBox.question(self,"是否保留当前数据？","快照不会被创建，但文件列表将被保留，直到应用重启",yes_text="是",no_text="否"):
                for i in range(self.TreeWidget.topLevelItemCount()):
                    self.TreeWidget.takeTopLevelItem(0)
                    self.label_count_data.setText("0")
        self.mainwindow.show()
        return super().closeEvent(e)