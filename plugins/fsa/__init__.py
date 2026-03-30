import shutil

from .snapshot_wizard_ui import Ui_snapshot_wizard
from .fsa_ui import Ui_fsa
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qfluentwidgets.common.icon import FluentIcon
from qfluentwidgets import FluentWindow

from sl_lib import sltk, MyFluentIcon, InputDialog, ProgressPopUp, QMessageBox
import os
import time
import json
import random
import threading
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()


class FSA(QWidget, Ui_fsa):
    """文件快照归档\nfile snapshot archive"""

    def __init__(self, mainwindow, settings_path, parent_dir):
        super().__init__()
        self.setupUi(self)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_crt_snap.setIcon(FluentIcon.CAMERA)
        self.btn_del_snap.setIcon(FluentIcon.DELETE)
        self.btn_show_snap.setIcon(FluentIcon.VIEW)
        self.btn_export_snap.setIcon(FluentIcon.SHARE)
        # 不知道为啥全局设定无效，必须在这里设置
        # ScrollArea的背景在scrollAreaWidgetContents里
        self.setStyleSheet("QWidget#scrollAreaWidgetContents {background-color:transparent}")

        self.mainwindow = mainwindow
        self.settings_path = settings_path
        self.read_settings()
        self.update_btn_status()
        self.update_snap_list()
        self.subwin_snapshot_wizard = SnapshotWizard(self.mainwindow, parent_dir)
        self.subwin_snapshot_wizard.update_vault(self.cmb_folder.currentText())
        self.init_signal()

    def init_signal(self):
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del_folder.clicked.connect(self.del_folder)
        self.btn_crt_snap.clicked.connect(self.subwin_snapshot_wizard.show)
        self.btn_del_snap.clicked.connect(self.del_snap)
        self.btn_export_snap.clicked.connect(self.export_snap)

        self.label_parent_data.clicked.connect(self.select_parent_row)

        self.cmb_folder.currentTextChanged.connect(self.update_btn_status)
        self.cmb_folder.currentTextChanged.connect(self.update_snap_list)
        self.cmb_folder.currentTextChanged.connect(self.update_snap_info)
        self.cmb_folder.currentTextChanged.connect(lambda: self.subwin_snapshot_wizard.update_vault(self.cmb_folder.currentText()))
        self.TableWidget.itemSelectionChanged.connect(self.update_btn_status)
        self.TableWidget.itemSelectionChanged.connect(self.update_snap_info)

    def select_parent_row(self):
        if len(self.label_parent_data.text()) == 8:
            self.TableWidget.clearSelection()
            for i in range(self.TableWidget.rowCount()):
                if self.TableWidget.item(i, 2).text() == self.label_parent_data.text():
                    self.TableWidget.selectRow(i)
                    return

    def update_btn_status(self):
        self.btn_del_folder.setEnabled(bool(self.cmb_folder.currentText()))
        self.btn_crt_snap.setEnabled(bool(self.cmb_folder.currentText()))
        self.btn_del_snap.setEnabled(bool(self.TableWidget.selectedItems()))
        self.btn_show_snap.setEnabled(bool(self.TableWidget.selectedItems()))
        self.btn_export_snap.setEnabled(bool(self.TableWidget.selectedItems()))

    def update_snap_list(self):
        self.TableWidget.clearContents()
        self.TableWidget.setRowCount(0)
        if self.cmb_folder.currentText():
            lis_snap = os.listdir(sltk.join_path(self.cmb_folder.currentText(), 'snapshots'))
            for i in lis_snap:
                try:
                    with open(sltk.join_path(self.cmb_folder.currentText(), 'snapshots', i, 'manifest.json'), 'r', encoding='utf-8') as file:
                        temp: dict = json.load(file)
                    if temp.get('comment', ''):
                        self.TableWidget.setSortingEnabled(False)
                        self.TableWidget.insertRow(0)
                        self.TableWidget.setItem(0, 0, QTableWidgetItem(time.strftime(r"%Y/%m/%d %H:%M:%S", time.strptime(str(temp.get('timestamp', 19700101000000)), r"%Y%m%d%H%M%S"))))
                        self.TableWidget.setItem(0, 1, QTableWidgetItem(temp.get('comment', '')))
                        self.TableWidget.setItem(0, 2, QTableWidgetItem(temp.get('id', '')))
                        self.TableWidget.setItem(0, 3, QTableWidgetItem(str(temp.get('statistics', {}).get('file_count', 0))))
                        self.TableWidget.setSortingEnabled(True)
                except:
                    pass
            self.TableWidget.resizeColumnsToContents()

    def update_snap_info(self):
        self.label_parent_data.setText('')
        self.label_dettime_data.setText('')
        self.label_det_data.setText('0')
        self.label_add_data.setText('0')
        self.label_mod_data.setText('0')
        self.label_del_data.setText('0')
        self.pgr_add.setValue(0)
        self.pgr_mod.setValue(0)
        self.pgr_del.setValue(0)
        try:
            with open(sltk.join_path(self.cmb_folder.currentText(), 'snapshots', self.TableWidget.item(self.TableWidget.currentRow(), 2).text(), 'manifest.json'), 'r', encoding='utf-8') as file:
                manifest: dict = json.load(file)

            if manifest.get('parent', ''):
                self.label_parent_data.setText(manifest['parent'])

                for i in range(self.TableWidget.rowCount()):
                    if self.TableWidget.item(i, 2).text() == manifest['parent']:
                        temp = time.mktime(time.strptime(str(manifest['timestamp']), r"%Y%m%d%H%M%S"))
                        temp -= time.mktime(time.strptime(self.TableWidget.item(i, 0).text(), r"%Y/%m/%d %H:%M:%S"))
                        temp = int(temp)
                        if temp >= 0:
                            txt = ''
                            if temp >= 60 * 60 * 24 * 30 * 12:
                                txt += f'{temp//(60*60*24*30*12)}年 '
                                temp %= (60 * 60 * 24 * 30 * 12)
                            if temp >= 60 * 60 * 24 * 30:
                                txt += f'{temp//(60*60*24*30)}月 '
                                temp %= (60 * 60 * 24 * 30)
                            if temp >= 60 * 60 * 24:
                                txt += f'{temp//(60*60*24)}天 '
                                temp %= (60 * 60 * 24)
                            if temp >= 60 * 60:
                                txt += f'{temp//(60*60)}小时 '
                                temp %= (60 * 60)
                            if temp >= 60:
                                txt += f'{temp//60}分 '
                                temp %= 60
                            txt += f'{temp}秒'
                            self.label_dettime_data.setText(txt)
                        break

            self.label_det_data.setText(str(manifest['statistics']['delta']))
            self.label_add_data.setText(str(manifest['statistics']['add']))
            self.label_mod_data.setText(str(manifest['statistics']['mod']))
            self.label_del_data.setText(str(manifest['statistics']['del']))
            if manifest['statistics']['delta']:
                self.pgr_add.setValue(int(manifest['statistics']['add'] / manifest['statistics']['delta'] * 100))
                self.pgr_mod.setValue(int(manifest['statistics']['mod'] / manifest['statistics']['delta'] * 100))
                self.pgr_del.setValue(int(manifest['statistics']['del'] / manifest['statistics']['delta'] * 100))
        except:
            pass

    def add_folder(self):
        path = QFileDialog.getExistingDirectory(self, "选择快照存档文件夹")
        if not os.path.isdir(path):
            QMessageBox.warning(self, "警告", "文件夹无效")
        else:
            sltk.unique_add_items(self.cmb_folder, path)
            config_file = sltk.join_path(path, 'index.json')
            if not os.path.isfile(config_file):
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump({"version": 1, "head": "", "latest": ""}, f)
                    os.makedirs(sltk.join_path(path, 'snapshots'), exist_ok=True)
        self.save_settings()

    def del_folder(self):
        temp = self.cmb_folder.currentText()
        self.cmb_folder.removeItem(self.cmb_folder.currentIndex())
        self.save_settings()
        QMessageBox.information(self, "提示", f"成功移除快照存档库 {temp}\n库中的文件仍然存在，可在稍后重新导入")

    def read_settings(self):
        try:
            with open(sltk.join_path(self.settings_path, 'fsa.json'), 'r', encoding='utf-8') as file:
                data = json.load(file)
                sltk.unique_set_items(self.cmb_folder, data['vaults'])
        except:
            pass

    def save_settings(self):
        os.makedirs(self.settings_path, exist_ok=True)
        with open(sltk.join_path(self.settings_path, 'fsa.json'), 'w', encoding='utf-8') as file:
            json.dump({"vaults": sltk.expend_children_text(self.cmb_folder)}, file)

    def del_snap(self):
        if self.TableWidget.currentRow() >= 0:
            del_id = self.TableWidget.item(self.TableWidget.currentRow(), 2).text()
            if QMessageBox.question(self, "确认删除快照？",
                                    "将永久删除快照 {} ({})\n后续快照需要重新计算".format(
                                        self.TableWidget.item(self.TableWidget.currentRow(), 1).text(), del_id),
                                    yes_text="确认删除"):
                self.subwin_snapshot_wizard.snap_delete(del_id)

    def export_snap(self):
        pass


class SnapshotWizard(FluentWindow, Ui_snapshot_wizard):
    def __init__(self, mainwindow: QMainWindow, main_dir):
        super().__init__()
        self.setAcceptDrops(True)
        self.mainwindow = mainwindow
        self.container = QWidget()
        self.setupUi(self.container)
        self.addSubInterface(self.container, None, "")
        self.setWindowTitle('快照向导')
        self.navigationInterface.setVisible(False)

        self.init_signal()

        self.TreeWidget.setColumnWidth(0, 250)

        self.btn_del.setIcon(FluentIcon.DELETE)
        self.btn_add_file.setIcon(FluentIcon.DOCUMENT)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER)
        self.btn_cancel.setIcon(FluentIcon.CANCEL)
        self.btn_create.setIcon(FluentIcon.CAMERA)
        self.toggle_filter.addItem("All", MyFluentIcon.Prohibited)
        self.toggle_filter.addItem("Include", FluentIcon.FILTER)
        self.toggle_filter.addItem("Exclude", FluentIcon.REMOVE_FROM)
        self.toggle_filter.setCurrentItem('Exclude')
        self.toggle_windows.setIcon(QIcon(sltk.join_path(main_dir, 'sl_lib', 'icons', 'windows.svg')))
        self.toggle_unix.setIcon(QIcon(sltk.join_path(main_dir, 'sl_lib', 'icons', 'linux.svg')))

    def init_signal(self):
        self.btn_cancel.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.create_snap)
        self.btn_add_file.clicked.connect(self.add_file)
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del.clicked.connect(self.del_item)
        self.toggle_filter.currentItemChanged.connect(self.update_ext_filter)
        self.TreeWidget.currentItemChanged.connect(self.update_btn_status)
        self.TreeWidget.itemCollapsed.connect(self.update_btn_status)
        self.TreeWidget.itemActivated.connect(self.update_btn_status)
        self.TreeWidget.itemClicked.connect(self.update_btn_status)

    def update_btn_status(self):
        self.btn_del.setEnabled(bool(len(self.TreeWidget.selectedItems())))
        self.btn_create.setEnabled(bool(self.TreeWidget.topLevelItemCount()))

    def file_filter(self, path):
        # 默认放行
        try:
            flag_filter, flag_hidden = True, False
            # 文件夹不需要检测后缀名
            if self.toggle_filter.currentRouteKey() != 'All' and os.path.isfile(path):
                is_match = os.path.splitext(path)[1][1:].lower() in self.lineedit_filter.text().lower().split(',')
                flag_filter = (self.toggle_filter.currentRouteKey() == 'Include') == is_match

            if self.toggle_windows.isChecked():
                flag_hidden |= os.stat(path).st_file_attributes & 0x2
            if self.toggle_unix.isChecked():
                flag_hidden |= os.path.basename(path).startswith('.')
            return flag_filter and not flag_hidden
        except Exception as e:
            print("过滤文件 ", path, " 时出现错误，已默认放行：", e)
            return True

    def update_ext_filter(self):
        INCLUDE_EXT = 'jpg,jpeg,png,heif,heic,avif,jxl,raw,dng'
        EXCLUDE_EXT = 'lnk,url,ini,conf,config,log,db'
        match self.toggle_filter.currentRouteKey():
            case "All":
                self.toggle_filter.setToolTip('当前模式：不过滤 (All)')
                self.lineedit_filter.setDisabled(True)
                if self.lineedit_filter.text() in [INCLUDE_EXT, EXCLUDE_EXT]:
                    self.lineedit_filter.clear()
            case "Include":
                self.toggle_filter.setToolTip('当前模式：白名单 (Include)')
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['', EXCLUDE_EXT]:
                    self.lineedit_filter.setText(INCLUDE_EXT)
            case "Exclude":
                self.toggle_filter.setToolTip('当前模式：黑名单 (Exclude)')
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['', INCLUDE_EXT]:
                    self.lineedit_filter.setText(EXCLUDE_EXT)

    def gen_uuid(self, length: int):
        while True:
            result = ""
            for i in range(length):
                result += hex(random.randint(0, 15))[2]
            if result not in self.lis_uuid:
                self.lis_uuid.append(result)
                return result

    def create_snap(self):
        def worker(index_config: dict):
            parent_files = self.snap_retrace(parent_id, self_id)
            if parent_files == 'error':
                return
            new_files, thumbnail_map = self.snap_calc_new()
            self.popup.total = 0
            self.popup.currentItem = '正在计算差异……'
            lis_file, lis_deleted = self.snap_calc_delta(parent_files, new_files)
            # 保存结果
            self.snap_config['statistics']['file_count'] = len(new_files)
            self.snap_config['statistics']['delta'] = len(lis_file) + len(lis_deleted)
            self.snap_config['statistics']['del'] = len(lis_deleted)
            for i in lis_file:
                self.snap_config['statistics'][i['type']] += 1
                # 生成缩略图
                if self.ckb_calc_hash.isChecked() and i['path'][-1].lower().endswith(('.jpg', '.jpeg', '.png', '.heif', '.heic', '.gif', '.bmp')):
                    try:
                        temp = thumbnail_map[sltk.join_path(*i['path'])]
                        with Image.open(temp) as img:
                            img.thumbnail((256, 256), Image.Resampling.LANCZOS)
                            img.convert("RGB")
                            thumb_path = sltk.join_path(self.vault_dir, "snapshots", self.snap_config["id"],
                                                        "thumbnails", i['hash']['blake3'] + ".heic")
                            img = pillow_heif.from_pillow(img)
                            img.save(thumb_path, format='HEIF',
                                     quality=35, subsampling="4:2:0", exif=None)
                    except Exception as e:
                        print(f'生成缩略图 {temp} 时出现错误：{e}')
            self.snap_config['files'] = lis_file
            self.snap_config['deleted'] = lis_deleted
            # 保存快照
            with open(sltk.join_path(self.vault_dir, "snapshots", self.snap_config['id'], "manifest.json"), 'w', encoding='utf-8') as file:
                json.dump(self.snap_config, file, ensure_ascii=False, indent=4)
            # 更新index.json
            with open(sltk.join_path(self.vault_dir, 'index.json'), 'w', encoding='utf-8') as file:
                json.dump(index_config, file)
            self.popup.done_msg = [
                '快照创建成功', f"快照 {snap_comment} ({self_id}) 包含{self.snap_config['statistics']['file_count']}个文件"]
            self.popup.is_done = True

        self_id = self.gen_uuid(8)
        snap_comment = InputDialog().run(self, '添加备注', f'为当前快照 {self_id} 添加备注')
        if not snap_comment:
            return
        # 在index.json中添加记录
        with open(sltk.join_path(self.vault_dir, 'index.json'), 'r', encoding='utf-8') as file:
            index_config: dict = json.load(file)
            parent_id = index_config.get('latest', '')
        if index_config.get('head', '') == '':
            index_config['head'] = self_id
        index_config['latest'] = self_id
        # 确认成功创建之后再由子线程写入

        # 初始化快照配置
        os.makedirs(sltk.join_path(self.vault_dir, "snapshots", self_id, "thumbnails"), exist_ok=True)
        self.snap_config = {"version": 1, "id": self_id, "parent": parent_id,
                            "timestamp": int(time.strftime(r"%Y%m%d%H%M%S")), "comment": snap_comment,
                            "statistics": {"file_count": 0, "delta": 0, "add": 0, "del": 0, "mod": 0}, "files": [], "deleted": []}
        with open(sltk.join_path(self.vault_dir, "snapshots", self_id, "manifest.json"), 'w', encoding='utf-8') as file:
            json.dump(self.snap_config, file)

        self.popup = ProgressPopUp().run(self, '正在创建快照')
        threading.Thread(target=worker, args=[index_config]).start()

    def snap_calc_new(self) -> tuple[list[dict], dict[str, str]]:
        '''由选中的文件生成快照信息，不会计算缩略图，但提供了图片预览展示\n\n注意未勾选`检查哈希`时字典中`hash`项为空'''
        error_count = 0
        lis: list[QTreeWidgetItem] = [i for i in self.TreeWidget.findItems(
            "*", Qt.MatchFlag.MatchWildcard | Qt.MatchFlag.MatchRecursive, 0) if not i.data(0, Qt.ItemDataRole.UserRole)]
        self.popup.total = len(lis)
        lis_file: list[dict] = []
        thumbnail_map: dict[str, str] = {}
        for i in lis:
            try:
                path: list[list[str], list[str]] = i.data(1, Qt.ItemDataRole.UserRole)
                full_path: str = sltk.join_path(*path[0], *path[1])
                self.popup.processed += 1
                self.popup.currentItem = full_path
                if os.path.isfile(full_path):
                    self.snap_config['statistics']['file_count'] += 1
                    temp = {"path": path[1], "size": os.path.getsize(full_path),
                            "last_edit": int(time.strftime(r"%Y%m%d%H%M%S", time.gmtime(os.path.getmtime(full_path)))),
                            "hash": [], "type": ""}
                    if full_path.lower().endswith(('.jpg', '.jpeg', '.png', '.heif', '.heic', '.gif', '.bmp')):
                        self.popup.thumbnail = full_path
                        thumbnail_map[sltk.join_path(*path[1])] = full_path
                    if self.ckb_calc_hash.isChecked():
                        temp['hash'] = sltk.calc_hash(full_path, md5=True, crc32=True, blake3=True, sha1=True, sha256=True)
                    lis_file.append(temp)
            except Exception as e:
                error_count += 1
                error_msg = e  # e离开缩进之后不可用
        if error_count > 0:
            QMetaObject.invokeMethod(self, "show_scan_error", Qt.ConnectionType.QueuedConnection,
                                         Q_ARG(str, 'create'), Q_ARG(int, error_count), Q_ARG(str, str(error_msg)))
        return lis_file, thumbnail_map

    def snap_retrace(self, from_id: str, self_id: str) -> list[dict] | str:
        '''从给定的快照id开始（含），一直回溯到根快照，重建给定id的完整文件信息\n\n注意回溯时不会考虑hash\n\n`self_id`只作为报错信息使用'''
        def is_duplicate(path: list[str], lis: list[dict]):
            for i in lis:
                if i["path"] == path:
                    return True
            return False
        # 从后往前用while快很多，也能减少内存传递，回溯时完全不用管hash
        lis_file: list[dict] = []
        lis_deleted: list[dict[str, list[str]]] = []
        try:
            while from_id:
                with open(sltk.join_path(self.vault_dir, "snapshots", from_id, "manifest.json"), 'r', encoding='utf-8') as file:
                    parent_config = json.load(file)
                # 先加后排除，文件移动时会同时出现在files和deleted中
                for i in parent_config['files']:
                    if not (is_duplicate(i["path"], lis_deleted) or is_duplicate(i["path"], lis_file)):
                        lis_file.append(i)
                for i in parent_config['deleted']:
                    if not is_duplicate(i["path"], lis_deleted):
                        lis_deleted.append(i)
                from_id = parent_config['parent']
            return lis_file
        except Exception as e:
            QMessageBox.warning(self, "快照回溯失败", f"回溯节点 {from_id} 时出现异常，节点可能已经损坏或被异常删除\n快照创建已被撤销，请手动删除当前节点 {self_id}\n\n{e}")
            return 'error'

    def snap_calc_delta(self, ref: list[dict[str, str | int | list | dict]], obj: list[dict[str, str | int | list | dict]]) -> tuple[list[dict[str, str | int | list | dict]], list[dict[str, list[str]]]]:
        '''比较两个快照，返回`files`与`deleted`两个列表，格式与`manifest.json`相同'''
        lis_file: list[dict] = []
        lis_deleted: list[dict[str, list[str]]] = []
        for i in obj:
            i['type'] = 'add'
        for old_file in ref:
            is_match = False
            for new_item in obj:
                if old_file['path'] == new_item['path']:
                    is_match = True
                    if 'blake3' in new_item['hash']:
                        if old_file['hash'].get('blake3', '') == new_item['hash']['blake3']:
                            new_item['type'] = 'same'
                        else:
                            new_item['type'] = 'mod'
                    else:
                        if old_file['size'] == new_item['size'] and old_file['last_edit'] == new_item['last_edit']:
                            new_item['type'] = 'same'
                        else:
                            new_item['type'] = 'mod'
                    break
            if not is_match:
                lis_deleted.append({'path': old_file['path']})
        # 从后往前删不会影响索引
        for i in range(len(obj) - 1, -1, -1):
            if obj[i]['type'] in ['add', 'mod']:
                lis_file.append(obj[i])
        return lis_file, lis_deleted

    def snap_rebase(self, obj_id: str, new_parent_id: str):
        '''将快照obj_id的父节点改为new_parent_id'''
        with open(sltk.join_path(self.vault_dir, "snapshots", obj_id, "manifest.json"), 'r', encoding='utf-8') as file:
            obj_config = json.load(file)
        try:
            obj_state = self.snap_retrace(obj_id, obj_id)
            new_parent_state = self.snap_retrace(new_parent_id, new_parent_id)
            lis_file, lis_deleted = self.snap_calc_delta(new_parent_state, obj_state)
            obj_config['parent'] = new_parent_id
            obj_config['statistics']['delta'] = len(lis_file) + len(lis_deleted)
            obj_config['statistics']['del'] = len(lis_deleted)
            obj_config['statistics']['add'] = 0
            obj_config['statistics']['mod'] = 0
            for i in lis_file:
                obj_config['statistics'][i['type']] += 1
            obj_config['files'] = lis_file
            obj_config['deleted'] = lis_deleted
            with open(sltk.join_path(self.vault_dir, "snapshots", obj_id, "manifest.json"), 'w', encoding='utf-8') as file:
                json.dump(obj_config, file, indent=4, ensure_ascii=False)
        except Exception as e:
            temp = self if self.isVisible() else self.mainwindow
            QMessageBox.warning(temp, '变更快照父节点失败', f"尝试更改快照 {obj_config['comment']} ({obj_id}) 的父节点时出现异常，变更已被撤销\n\n{e}")

    def snap_delete(self, obj_id: str):
        '''删除快照obj_id'''
        print('没有考虑删除节点里的缩略图')
        history = []
        with open(sltk.join_path(self.vault_dir, "snapshots", obj_id, "manifest.json"), 'r', encoding='utf-8') as file:
            obj_config = json.load(file)
        parent_id = obj_config['parent']
        try:
            for i in os.listdir(sltk.join_path(self.vault_dir, "snapshots")):
                manifest_path = sltk.join_path(self.vault_dir, "snapshots", i, "manifest.json")
                if not os.path.isfile(manifest_path):
                    continue
                with open(sltk.join_path(self.vault_dir, "snapshots", i, "manifest.json"), 'r', encoding='utf-8') as file:
                    config: dict = json.load(file)
                if config['parent'] == obj_id:
                    self.snap_rebase(config['id'], parent_id)
                    history.append(config['id'])
            with open(sltk.join_path(self.vault_dir, "index.json"), 'r', encoding='utf-8') as file:
                index = json.load(file)
            if index['head'] == obj_id:
                index['head'] = ''
            if index['latest'] == obj_id:
                index['latest'] = parent_id
            with open(sltk.join_path(self.vault_dir, "index.json"), 'w', encoding='utf-8') as file:
                json.dump(index, file)
            shutil.rmtree(sltk.join_path(self.vault_dir, "snapshots", obj_id))
        except Exception as e:
            temp = self if self.isVisible() else self.mainwindow
            QMessageBox.warning(temp, '删除快照失败', f"尝试删除快照 {obj_config['comment']} ({obj_id}) 时出现异常，删除操作已中断\n以下快照的父节点已从 {obj_id} 变更为 {parent_id if parent_id else '无'} ：\n{'、'.join(history)} \n\n{e}")
        self.mainwindow.subwin_fsa.update_snap_list()

    @Slot(str, int, str)
    def show_scan_error(self, step: str, error_count: int, error_msg: str):
        container = self if self.isVisible() else self.mainwindow
        match step:
            case 'scan':
                QMessageBox.warning(container, f"{error_count}个文件添加失败", f"最后的错误信息：\n{error_msg}")
            case 'create':
                QMessageBox.warning(container, "部分文件异常", f"计算快照信息时出现{error_count}个错误，已尝试跳过失败文件\n最后的报错信息：\n{error_msg}")

    def add_file(self, path: list[str] = None):
        if not path:
            path = [os.path.normpath(i)for i in QFileDialog.getOpenFileNames(
                self, "选择一个或多个文件")[0]]
        previous_items = [sltk.join_path(
            item[1], item[0]) for item in sltk.expend_children_text(self.TreeWidget)]
        error_count = 0
        for i in path:
            try:
                if self.file_filter(i) and i not in previous_items:
                    treeWidgetItem = QTreeWidgetItem()
                    treeWidgetItem.setText(0, os.path.basename(i))
                    treeWidgetItem.setIcon(0, self.map_icon(i, False))
                    treeWidgetItem.setText(1, os.path.dirname(i))
                    # temp.setCheckState(2,Qt.CheckState.Unchecked)
                    treeWidgetItem.setData(0, Qt.ItemDataRole.UserRole, False)
                    temp = sltk.split_path(i)
                    treeWidgetItem.setData(1, Qt.ItemDataRole.UserRole, [
                                           temp[:-1], temp[-1:]])  # [-1]会只剩str
                    treeWidgetItem.setFlags(treeWidgetItem.flags() & ~Qt.ItemFlag.ItemIsEditable & ~
                                            Qt.ItemFlag.ItemIsUserCheckable & ~Qt.ItemFlag.ItemIsUserTristate)
                    self.TreeWidget.addTopLevelItem(treeWidgetItem)
                    self.label_count_data.setText(
                        str(int(self.label_count_data.text()) + 1))
            except Exception as e:
                error_count += 1
                error_msg = str(e)
        if error_count:
            self.show_scan_error('scan',error_count, error_msg)
        self.update_btn_status()

    def add_folder(self, path: str = None):
        if not path:
            path = QFileDialog.getExistingDirectory(self, "选择一个文件夹")
        if path:
            path = os.path.normpath(path)
            flag_include_children = QMessageBox.question(
                self, "是否包含此文件夹内的子文件夹？", path, yes_text="是", no_text="否")
            previous_items = [sltk.join_path(
                item[1], item[0]) for item in sltk.expend_children_text(self.TreeWidget)]

            threading.Thread(target=self.recurse_folder, args=(
                path, flag_include_children, previous_items)).start()
            # self.recurse_folder(path,flag_include_children,previous_items)

    def recurse_folder(self, path: str, flag_include_children: bool, previous_items: list[str], parent: QTreeWidgetItem = None, depth: int = 0) -> tuple[int, str] | None:
        fail_count, error = 0, '未捕捉到错误信息'
        if depth == 0:
            lis = [os.path.basename(path)]
            path = os.path.dirname(path)
        else:
            lis = os.listdir(path)
        for final_path in lis:
            try:
                full_path = sltk.join_path(path, final_path)
                if not self.file_filter(full_path) or full_path in previous_items:
                    continue
                treeWidgetItem = QTreeWidgetItem(parent)
                treeWidgetItem.setFlags(treeWidgetItem.flags(
                ) & ~Qt.ItemFlag.ItemIsEditable & ~Qt.ItemFlag.ItemIsUserCheckable & ~Qt.ItemFlag.ItemIsUserTristate)
                treeWidgetItem.setText(0, final_path)

                if os.path.isfile(full_path):
                    treeWidgetItem.setIcon(0, self.map_icon(final_path, False))
                    # temp.setCheckState(2,Qt.CheckState.Unchecked)
                    treeWidgetItem.setData(0, Qt.ItemDataRole.UserRole, False)
                    temp = sltk.split_path(full_path)
                    treeWidgetItem.setData(1, Qt.ItemDataRole.UserRole, [
                                           temp[:-(depth + 1)], temp[-(depth + 1):]])
                    self.label_count_data.setText(
                        str(int(self.label_count_data.text()) + 1))
                # 二次判断防止无效符号链接
                elif os.path.isdir(full_path):
                    if flag_include_children or depth == 0:
                        treeWidgetItem.setIcon(
                            0, self.map_icon(final_path, True))
                        # temp.setCheckState(2,Qt.CheckState.Checked)
                        treeWidgetItem.setData(
                            0, Qt.ItemDataRole.UserRole, True)
                        temp = sltk.split_path(full_path)
                        treeWidgetItem.setData(1, Qt.ItemDataRole.UserRole, [
                                               temp[:-(depth + 1)], temp[-(depth + 1):]])
                        count, error = self.recurse_folder(
                            full_path, flag_include_children, previous_items, treeWidgetItem, depth + 1)
                        fail_count += count
                        if treeWidgetItem.childCount() == 0:
                            if parent:
                                parent.removeChild(treeWidgetItem)
                            continue
                    else:
                        if parent:
                            parent.removeChild(treeWidgetItem)
                        continue

                if not parent:
                    # 仅在根节点显示路径，其余路径通过UserRole隐性存储
                    treeWidgetItem.setText(1, path)
                    self.TreeWidget.addTopLevelItem(treeWidgetItem)
            except Exception as e:
                fail_count += 1
                error = str(e)
        if depth == 0:
            if fail_count:
                QMetaObject.invokeMethod(self, "show_scan_error", Qt.ConnectionType.QueuedConnection,
                                         Q_ARG(str, 'scan'), Q_ARG(int, fail_count), Q_ARG(str, str(error)))
                # QMessageBox.information(self,"提示",f"{fail_count}个文件添加失败\n最后一次错误信息：\n{error}")
        else:
            return fail_count, error
        QMetaObject.invokeMethod(
            self, "update_btn_status", Qt.ConnectionType.QueuedConnection)

    def calc_file_count(self):
        return sum([0 if item.data(0, Qt.ItemDataRole.UserRole)else 1 for item in self.TreeWidget.findItems("*", Qt.MatchFlag.MatchWildcard | Qt.MatchFlag.MatchRecursive, 0)])

    def del_item(self):
        for i in self.TreeWidget.selectedItems():
            if i.parent():
                i.parent().removeChild(i)
            else:
                self.TreeWidget.takeTopLevelItem(
                    self.TreeWidget.indexOfTopLevelItem(i))
        self.label_count_data.setText(str(self.calc_file_count()))
        self.update_btn_status()

    def map_icon(self, item: str, is_dir: bool) -> QIcon:
        if is_dir:
            # 文件夹无图标方便区分
            return QIcon()
            return FluentIcon.FOLDER.icon()
        else:
            if os.path.splitext(item)[1].lower() in ['.jpg', '.jpeg', '.jxl', '.png', '.apng',
                                                     '.gif', '.bmp', '.tif', '.tiff', '.ico',
                                                     '.svg', '.webp', '.heic', '.heif', '.avif',
                                                     '.raw', '.dng', '.img', '.cr2', '.cr3', '.crf']:
                return FluentIcon.PHOTO.icon()
            elif os.path.splitext(item)[1].lower() in ['.mp4', '.mkv', '.avi', '.mov', '.flv',
                                                       '.wmv', 'swf', '.ts', '.mts', '.webm',
                                                       '.m2t', '.m2ts', '.rmvb', '.bdmv', '.vp6',
                                                       '.vp7', '.vp8', '.vp9', '.vp10', '.h264',
                                                       '.h265', '.hevc', '.h266', '.vvc', '.av1',
                                                       '.m3u', '.m3u8', '.srt', '.ass']:
                return FluentIcon.MOVIE.icon()
            elif os.path.splitext(item)[1].lower() in ['.mp3', '.m4a', '.flac', '.wav', '.opus',
                                                       '.wave', '.aac', '.ogg', '.wma', '.ape',
                                                       '.pcm', '.ac3', '.eac3', '.dts', '.lrc']:
                return FluentIcon.MUSIC.icon()
            elif os.path.splitext(item)[1].lower() in ['.lnk', '.url']:
                return FluentIcon.LINK.icon()
            elif os.path.splitext(item)[1].lower() in ['.txt', '.log', '.md', '.json', '.xml',
                                                       '.ini', '.yaml', '.yml', '.toml', '.ini',
                                                       '.conf', '.cfg', '.config', '.properties', '.prop',
                                                       'htm', '.html']:
                return FluentIcon.LABEL.icon()
            else:
                return FluentIcon.DOCUMENT.icon()

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.accept()

    def dropEvent(self, event: QDropEvent):
        lis = event.mimeData().urls()
        if lis:
            for i in lis:
                path = os.path.normpath(i.toLocalFile())
                if os.path.isfile(path):
                    self.add_file([path])
                elif os.path.isdir(path):
                    self.add_folder(path)

    def update_vault(self, vault_dir: str):
        self.vault_dir = vault_dir
        self.lis_uuid: list[str] = os.listdir(sltk.join_path(vault_dir, 'snapshots')) if vault_dir else []

    def showEvent(self, e):
        self.mainwindow.hide()
        self.resize(600, 400)
        return super().showEvent(e)

    def closeEvent(self, e):
        if self.TreeWidget.topLevelItemCount() > 0:
            if not QMessageBox.question(self, "是否保留当前数据？", "快照不会被创建，但文件列表将被保留，直到应用重启", yes_text="是", no_text="否"):
                for i in range(self.TreeWidget.topLevelItemCount()):
                    self.TreeWidget.takeTopLevelItem(0)
                    self.label_count_data.setText("0")
        self.mainwindow.subwin_fsa.update_snap_list()
        self.mainwindow.show()
        return super().closeEvent(e)
