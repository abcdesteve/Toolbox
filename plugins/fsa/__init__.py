from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qfluentwidgets.common.icon import FluentIcon
from qfluentwidgets import FluentWindow

from sl_lib import *
import os,json

from .fsa_ui import Ui_fsa
from .snapshot_wizard_ui import Ui_snapshot_wizard

class FSA(QWidget,Ui_fsa):
    """文件快照归档\nfile snapshot archive"""
    def __init__(self,mainwindow,settings_path):
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
        self.subwin_snapshot_wizard=SnapshotWizard(self.mainwindow)
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
            self.cmb_folder.addItem(path)
            config_file=sltk.join_path(path,'index.json')
            if not os.path.isfile(config_file):
                with open(config_file,'w',encoding='utf-8') as f:
                    json.dump({"version":1,"head":"","latest":"","snapshots":[]},f)
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
    def __init__(self,mainwindow:QWidget):
        super().__init__()
        self.mainwindow=mainwindow
        self.container = QWidget()
        self.setupUi(self.container)
        self.addSubInterface(self.container,None,"")
        self.setWindowTitle('快照向导')
        self.navigationInterface.setVisible(False)

        self.TreeWidget.setColumnWidth(0,200)
        self.TreeWidget.setColumnWidth(1,300)

        self.btn_del.setIcon(FluentIcon.DELETE)
        self.btn_add_file.setIcon(FluentIcon.DOCUMENT)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER)
        self.btn_cancel.setIcon(FluentIcon.CANCEL)
        self.btn_create.setIcon(FluentIcon.CAMERA)
        self.init_signal()

    def init_signal(self):
        self.btn_cancel.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.create_snap)
        self.btn_add_file.clicked.connect(self.add_file)
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del.clicked.connect(self.del_item)

    def create_snap(self):
        pass

    def add_file(self):
        path=[os.path.realpath(i)for i in QFileDialog.getOpenFileNames(self,"选择一个或多个文件")[0]]
        previous_items=[sltk.join_path(item[1],item[0]) for item in sltk.expend_children_text(self.TreeWidget)]
        for i in path:
            if i not in previous_items:
                temp=QTreeWidgetItem()
                temp.setText(0,os.path.basename(i))
                temp.setIcon(0,self.map_icon(i,False))
                temp.setText(1,os.path.dirname(i))
                temp.setCheckState(2,Qt.CheckState.Unchecked)
                temp.setFlags(temp.flags()&~Qt.ItemFlag.ItemIsEditable&~Qt.ItemFlag.ItemIsUserCheckable&~Qt.ItemFlag.ItemIsUserTristate)
                self.TreeWidget.addTopLevelItem(temp)
                self.label_count_data.setText(str(int(self.label_count_data.text())+1))

    def add_folder(self):
        path=QFileDialog.getExistingDirectory(self,"选择一个文件夹")
        if path:
            path=os.path.realpath(path)
            flag_include_children=QMessageBox.question(self,"提示","是否包含子文件夹",yes_text="是",no_text="否")
            previous_items=[sltk.join_path(item[1],item[0]) for item in sltk.expend_children_text(self.TreeWidget)]
            self.recurse_folder(path,flag_include_children,previous_items)

    def recurse_folder(self,path:str,flag_include_children:bool,previous_items:list[str],parent:QTreeWidgetItem=None):
        for i in os.listdir(path):
            item=sltk.join_path(path,i)
            if item not in previous_items:
                temp=QTreeWidgetItem(parent)
                temp.setFlags(temp.flags()&~Qt.ItemFlag.ItemIsEditable&~Qt.ItemFlag.ItemIsUserCheckable&~Qt.ItemFlag.ItemIsUserTristate)
                temp.setText(0,i)
                temp.setText(1,path)
        
                if parent:
                    parent.addChild(temp)
                else:
                    self.TreeWidget.addTopLevelItem(temp)

                if os.path.isfile(item):
                    temp.setIcon(0,self.map_icon(i,False))
                    temp.setCheckState(2,Qt.CheckState.Unchecked)
                    self.label_count_data.setText(str(int(self.label_count_data.text())+1))
                else:
                    temp.setIcon(0,self.map_icon(i,True))
                    temp.setCheckState(2,Qt.CheckState.Checked)
                    if flag_include_children:
                        self.recurse_folder(item,flag_include_children,previous_items,temp)

    def calc_file_count(self):
        return sum([item.checkState(2)==Qt.CheckState.Unchecked for item in self.TreeWidget.findItems("*",Qt.MatchFlag.MatchWildcard|Qt.MatchFlag.MatchRecursive,2)])

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