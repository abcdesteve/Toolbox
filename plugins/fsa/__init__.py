from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from qfluentwidgets.common.icon import FluentIcon
from qfluentwidgets import FluentWindow

from .fsa_ui import Ui_fsa
from .snapshot_wizard_ui import Ui_snapshot_wizard
from .snapshot_viewer_ui import Ui_snapshot_viewer


from sl_lib import sltk, MyFluentIcon, InputDialog, ProgressPopUp, QMessageBox, benchmark
import os
import shutil
import time
import json
import random
import threading
import multiprocessing
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()

MAX_PROCESS = max(1, int(multiprocessing.cpu_count() * 0.7))

EXT_PICTURE = ('.jpg', '.jpeg', '.jxl', '.png', '.apng',
               '.gif', '.bmp', '.tif', '.tiff', '.ico',
               '.svg', '.webp', '.heic', '.heif', '.avif',
               '.raw', '.dng', '.img', '.cr2', '.cr3', '.crf')
EXT_VIDEO = ('.mp4', '.mkv', '.avi', '.mov', '.flv',
             '.wmv', 'swf', '.ts', '.mts', '.webm',
             '.m2t', '.m2ts', '.rmvb', '.bdmv', '.vp6',
             '.vp7', '.vp8', '.vp9', '.vp10', '.h264',
             '.h265', '.hevc', '.h266', '.vvc', '.av1',
             '.m3u', '.m3u8', '.srt', '.ass')
EXT_MUSIC = ('.mp3', '.m4a', '.flac', '.wav', '.opus',
             '.wave', '.aac', '.ogg', '.wma', '.ape',
             '.pcm', '.ac3', '.eac3', '.dts', '.lrc')
EXT_LINK = ('.lnk', '.url')
EXT_TEXT = ('.txt', '.log', '.md', '.json', '.xml',
            '.ini', '.yaml', '.yml', '.toml', '.ini',
            '.conf', '.cfg', '.config', '.properties', '.prop',
            'htm', '.html')


def map_icon(item: str, is_dir: bool) -> QIcon:
    if is_dir:
        # 文件夹无图标方便区分
        return QIcon()
        return FluentIcon.FOLDER.icon()
    else:
        if os.path.splitext(item)[1].lower() in EXT_PICTURE:
            return FluentIcon.PHOTO.icon()
        elif os.path.splitext(item)[1].lower() in EXT_VIDEO:
            return FluentIcon.MOVIE.icon()
        elif os.path.splitext(item)[1].lower() in EXT_MUSIC:
            return FluentIcon.MUSIC.icon()
        elif os.path.splitext(item)[1].lower() in EXT_LINK:
            return FluentIcon.LINK.icon()
        elif os.path.splitext(item)[1].lower() in EXT_TEXT:
            return FluentIcon.LABEL.icon()
        else:
            return FluentIcon.DOCUMENT.icon()


class FSA(QWidget, Ui_fsa):
    """文件快照归档\nfile snapshot archive"""

    def __init__(self, mainwindow, settings_path, parent_dir):
        super().__init__()
        self.setupUi(self)
        self.btn_add_folder.setIcon(FluentIcon.FOLDER_ADD)
        self.btn_del_folder.setIcon(FluentIcon.DELETE)
        self.btn_crt_snap.setIcon(FluentIcon.CAMERA)
        self.btn_del_snap.setIcon(FluentIcon.DELETE)
        self.btn_view_snap.setIcon(FluentIcon.VIEW)
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
        self.subwin_snapshot_viewer = SnapshotViewer(mainwindow)
        self.init_signal()

    def init_signal(self):
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del_folder.clicked.connect(self.del_folder)
        self.btn_crt_snap.clicked.connect(self.subwin_snapshot_wizard.show)
        self.btn_view_snap.clicked.connect(lambda: self.subwin_snapshot_viewer.view_snapshot(self.cmb_folder.currentText(), self.TableWidget.item(self.TableWidget.currentRow(), 2).text()))
        self.btn_view_snap.clicked.connect(self.mainwindow.update_theme)  # 更新主题只影响最开始存在的窗口，拆分器会附带颜色
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
        self.btn_view_snap.setEnabled(bool(self.TableWidget.selectedItems()))
        self.btn_export_snap.setEnabled(bool(self.TableWidget.selectedItems()))

    @Slot()
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
        self.label_move_data.setText('0')
        self.pgr_add.setValue(0)
        self.pgr_mod.setValue(0)
        self.pgr_del.setValue(0)
        self.pgr_move.setValue(0)
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
                                txt += f'{temp//(60*60*24*30*12)}年'
                                temp %= (60 * 60 * 24 * 30 * 12)
                            if temp >= 60 * 60 * 24 * 30:
                                txt += f'{temp//(60*60*24*30)}月'
                                temp %= (60 * 60 * 24 * 30)
                            if temp >= 60 * 60 * 24:
                                txt += f'{temp//(60*60*24)}天'
                                temp %= (60 * 60 * 24)
                            if temp >= 60 * 60:
                                txt += f'{temp//(60*60)}小时'
                                temp %= (60 * 60)
                            if temp >= 60:
                                txt += f'{temp//60}分'
                                temp %= 60
                            txt += f'{temp}秒'
                            self.label_dettime_data.setText(txt)
                        break

            self.label_det_data.setText(str(manifest['statistics'].get('delta', 0)))
            self.label_add_data.setText(str(manifest['statistics'].get('add', 0)))
            self.label_mod_data.setText(str(manifest['statistics'].get('mod', 0)))
            self.label_del_data.setText(str(manifest['statistics'].get('del', 0)))
            self.label_move_data.setText(str(manifest['statistics'].get('move', 0)))
            if manifest['statistics'].get('delta', 0):
                self.pgr_add.setValue(int(manifest['statistics'].get('add', 0) / manifest['statistics']['delta'] * 100))
                self.pgr_mod.setValue(int(manifest['statistics'].get('mod', 0) / manifest['statistics']['delta'] * 100))
                self.pgr_del.setValue(int(manifest['statistics'].get('del', 0) / manifest['statistics']['delta'] * 100))
                self.pgr_move.setValue(int(manifest['statistics'].get('move', 0) / manifest['statistics']['delta'] * 100))
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
                self.popup = ProgressPopUp().run(self, '', delay=0)
                threading.Thread(target=self.subwin_snapshot_wizard.snap_delete, args=(del_id, self.popup)).start()

    def export_snap(self):
        pass


def _gen_snap(rel_path: list[str], full_path: str, parent_files: list, lis_files: list, scan_mode: str, error_count, error_msg, lock) -> str:
    try:
        data = {"path": rel_path, "size": os.path.getsize(full_path),
                "last_edit": int(time.strftime(r"%Y%m%d%H%M%S", time.gmtime(os.path.getmtime(full_path)))),
                "hash": {}, "type": ""}
        # 暂不显示缩略图以提速
        if scan_mode == 'Loose':
            for temp in parent_files:
                if temp['path'] == rel_path:
                    if temp['size'] == data['size'] and temp['last_edit'] == data['last_edit']:
                        data['type'] = 'same'
                        # print(f'宽松模式，跳过 {full_path} 的哈希计算')
                    else:
                        data['hash'] = sltk.calc_hash(full_path, md5=True, crc32=True, blake3=True, sha1=True, sha256=True)
                    break
            else:
                data['hash'] = sltk.calc_hash(full_path, md5=True, crc32=True, blake3=True, sha1=True, sha256=True)
        elif scan_mode == 'Strict':
            data['hash'] = sltk.calc_hash(full_path, md5=True, crc32=True, blake3=True, sha1=True, sha256=True)
        lis_files.append(data)
    except Exception as e:
        with lock:
            error_count.value += 1
            error_msg.set(repr(e))
    return full_path


def _gen_thumb(rel_path: str, full_path: str, thumb_path: str, error_count, error_msg, lock) -> tuple[str, str]:
    # 多进程启动的函数不能属于类
    try:
        with Image.open(full_path) as img:
            img.thumbnail((256, 256), Image.Resampling.LANCZOS)  # LANCZOS(圈圈伪影) 6ms/BOX(块状锯齿) 4ms/NEAREST 3ms
            img = img.convert("RGB")
            # img = pillow_heif.from_pillow(img)
            img.save(thumb_path, format='WEBP', quality=90, method=1)  # 90画质好很多，0比较糊
    except Exception as e:
        print(f'生成 {full_path} 的缩略图时出现错误：{e}')
        with lock:
            error_count.value += 1
            error_msg.set(repr(e))
    return rel_path, thumb_path


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
        self.switch_filter.addItem("All", MyFluentIcon.Prohibited)
        self.switch_filter.addItem("Include", FluentIcon.FILTER)
        self.switch_filter.addItem("Exclude", FluentIcon.REMOVE_FROM)
        self.switch_filter.setCurrentItem('Exclude')
        self.switch_scan_mode.addItem("Fast", MyFluentIcon.Flash)
        self.switch_scan_mode.addItem("Loose", FluentIcon.SPEED_HIGH)
        self.switch_scan_mode.addItem("Strict", FluentIcon.SEARCH)
        self.switch_scan_mode.setCurrentItem('Loose')
        self.toggle_windows.setIcon(QIcon(sltk.join_path(main_dir, 'sl_lib', 'icons', 'windows.svg')))
        self.toggle_unix.setIcon(QIcon(sltk.join_path(main_dir, 'sl_lib', 'icons', 'linux.svg')))

    def init_signal(self):
        self.btn_cancel.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.create_snap)
        self.btn_add_file.clicked.connect(self.add_file)
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_del.clicked.connect(self.del_item)
        self.switch_filter.currentItemChanged.connect(self.update_ext_filter)
        self.switch_scan_mode.currentItemChanged.connect(self.update_scan_mode)
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
            if self.switch_filter.currentRouteKey() != 'All' and os.path.isfile(path):
                is_match = os.path.splitext(path)[1][1:].lower() in self.lineedit_filter.text().lower().split(',')
                flag_filter = (self.switch_filter.currentRouteKey() == 'Include') == is_match

            if self.toggle_windows.isChecked():
                flag_hidden |= os.stat(path).st_file_attributes & 0x2
            if self.toggle_unix.isChecked():
                flag_hidden |= os.path.basename(path).startswith('.')
            return flag_filter and not flag_hidden
        except Exception as e:
            print("过滤文件 ", path, " 时出现错误，已默认放行：", e)
            return True

    def update_ext_filter(self):
        INCLUDE_EXT = 'jpg,jpeg,png,bmp,heif,heic,avif,jxl,raw,dng'
        EXCLUDE_EXT = 'lnk,url,ini,conf,config,log,db'
        match self.switch_filter.currentRouteKey():
            case "All":
                self.switch_filter.setToolTip('当前模式：不过滤 (All)')
                self.lineedit_filter.setDisabled(True)
                if self.lineedit_filter.text() in [INCLUDE_EXT, EXCLUDE_EXT]:
                    self.lineedit_filter.clear()
            case "Include":
                self.switch_filter.setToolTip('当前模式：白名单 (Include)')
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['', EXCLUDE_EXT]:
                    self.lineedit_filter.setText(INCLUDE_EXT)
            case "Exclude":
                self.switch_filter.setToolTip('当前模式：黑名单 (Exclude)')
                self.lineedit_filter.setDisabled(False)
                if self.lineedit_filter.text() in ['', INCLUDE_EXT]:
                    self.lineedit_filter.setText(EXCLUDE_EXT)

    def update_scan_mode(self):
        match self.switch_scan_mode.currentRouteKey():
            case "Fast":
                self.switch_scan_mode.setToolTip('当前模式：急速 (Fast)\n适用于文件在云端不方便下载的场景\n\n仅扫描文件属性，不会生成预览图\n该模式下文件移动/重命名将被识别为删除添加2步操作')
            case "Loose":
                self.switch_scan_mode.setToolTip('当前模式：宽松 (Loose)\n推荐使用\n\n完整扫描文件内容并生成预览图，在修改时间和文件大小相同时跳过扫描\n在极少数场景下可能无法识别文件篡改')
            case "Strict":
                self.switch_scan_mode.setToolTip('当前模式：严格 (Strict)\n速度较慢，适用于需要确保文件不被篡改的场景\n\n始终完整扫描文件内容并生成预览图')

    def gen_uuid(self, length: int):
        while True:
            result = ""
            for i in range(length):
                result += hex(random.randint(0, 15))[2]
            if result not in self.lis_uuid:
                self.lis_uuid.append(result)
                return result

    def create_snap(self):
        def _gen_thumb_callback(result):
            '''callback函数回传单个值，要手动解包\n\n此时在启动池的进程中运行，可以动self，但由于多线程还是不能动UI'''
            rel_path, thumb_path = result
            self.popup.currentItem = rel_path
            self.popup.thumbnail = thumb_path
            self.popup.processed += 1

        def worker(config_index: dict):
            self.popup.title = '正在回溯快照……'
            parent_files, error_msg = self.snap_retrace(parent_id)
            if error_msg:
                QMessageBox.information('快照创建已被撤销', f'请手动删除当前节点 {self_id}\n错误信息：\n\n{error_msg}')
                return
            self.popup.title = '正在扫描文件……'
            all_files, thumbnail_map = self.snap_calc_new(parent_files)
            self.popup.total = len(all_files)
            self.popup.processed = 0
            self.popup.start_time = time.time()
            self.popup.title = '正在计算差异……'
            self.snap_config['statistics']['file_count'] = len(all_files)  # calc_delta后all_files被污染
            new_files, deleted_files = self.snap_calc_delta(parent_files, all_files)
            # 保存结果
            self.snap_config['statistics']['delta'] = len(new_files) + len(deleted_files)
            self.snap_config['statistics']['del'] = len(deleted_files)
            for i in new_files:
                self.snap_config['statistics'][i['type']] += 1
            self.snap_config['files'] = new_files
            self.snap_config['deleted'] = deleted_files
            # 保存快照
            with open(sltk.join_path(self.vault_dir, "snapshots", self.snap_config['id'], "manifest.json"), 'w', encoding='utf-8') as file:
                json.dump(self.snap_config, file, ensure_ascii=False, indent=4)
            # 更新index.json
            with open(sltk.join_path(self.vault_dir, 'index.json'), 'w', encoding='utf-8') as file:
                json.dump(config_index, file)

            process_count = max(1, min(MAX_PROCESS, len(new_files)))  # 无变动时可能为0
            self.popup.title = f'等待多进程启动…… ({process_count}/{multiprocessing.cpu_count()})'
            mpManager = multiprocessing.Manager()
            error_count = mpManager.Value('i', 0)
            error_msg = mpManager.Value('s', '')
            lock = mpManager.Lock()
            # 生成缩略图
            if self.switch_scan_mode.currentRouteKey() != "Fast":
                with multiprocessing.Pool(process_count)as p:
                    for i in new_files:
                        rel_path = sltk.join_path(*i['path'])
                        if rel_path in thumbnail_map:
                            full_path = thumbnail_map[rel_path]
                            thumb_path = sltk.join_path(self.vault_dir, "snapshots", self.snap_config["id"],
                                                        "thumbnails", i['hash']['blake3'] + ".webp")
                            p.apply_async(_gen_thumb, args=(rel_path, full_path, thumb_path, error_count, error_msg, lock), callback=_gen_thumb_callback, error_callback=print)
                    # 这两步必须在with中，一离开with池就被销毁了
                    self.popup.title = '正在生成缩略图……'
                    p.close()  # 拒绝新提交
                    p.join()  # 等待所有任务完成
            if error_count.get() > 0:
                self.popup.done_msg = [f'快照 {snap_comment} ({self_id}) 创建完成', f"{error_count.get()}个文件生成缩略图失败，最后一次错误信息：\n{error_msg.get()}\n\n\
                                        快照包含{self.snap_config['statistics']['file_count']}个文件\n\
                                        - 新增{self.snap_config['statistics']['add']}个文件\n\
                                        - 修改{self.snap_config['statistics']['mod']}个文件\n\
                                        - 删除{self.snap_config['statistics']['del']}个文件\n\
                                        - 移动/重命名{self.snap_config['statistics']['move']}个文件"]
            else:
                self.popup.done_msg = [f'快照 {snap_comment} ({self_id}) 创建成功',
                                       f"快照包含{self.snap_config['statistics']['file_count']}个文件\n\
                                        - 新增{self.snap_config['statistics']['add']}个文件\n\
                                        - 修改{self.snap_config['statistics']['mod']}个文件\n\
                                        - 删除{self.snap_config['statistics']['del']}个文件\n\
                                        - 移动/重命名{self.snap_config['statistics']['move']}个文件"]
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
        self.snap_config = {"version": 2, "id": self_id, "parent": parent_id,
                            "timestamp": int(time.strftime(r"%Y%m%d%H%M%S")), "comment": snap_comment,
                            "statistics": {"file_count": 0, "delta": 0, "add": 0, "del": 0, "mod": 0, 'move': 0}, "files": [], "deleted": []}
        with open(sltk.join_path(self.vault_dir, "snapshots", self_id, "manifest.json"), 'w', encoding='utf-8') as file:
            json.dump(self.snap_config, file)

        self.popup = ProgressPopUp().run(self, '')
        threading.Thread(target=worker, args=[index_config]).start()

    def snap_calc_new(self, parent_files) -> tuple[list[dict], dict[str, str]]:
        '''由选中的文件生成快照信息，不会计算缩略图\n\n提供thumbnail_map以解决文件信息中不含绝对路径的问题\n\n注意未勾选`检查哈希`时字典中`hash`项为空'''
        def _gen_snap_callback(result):
            full_path = result
            self.popup.processed += 1
            self.popup.currentItem = full_path

        lis: list[QTreeWidgetItem] = [i for i in self.TreeWidget.findItems(
            "*", Qt.MatchFlag.MatchWildcard | Qt.MatchFlag.MatchRecursive, 0) if not i.data(0, Qt.ItemDataRole.UserRole)]
        self.popup.total = len(lis)
        process_count = max(1, min(MAX_PROCESS, len(lis)))  # 无变动时可能为0
        self.popup.title = f'等待多进程启动…… ({process_count}/{multiprocessing.cpu_count()})'
        mpManager = multiprocessing.Manager()
        error_count = mpManager.Value('i', 0)
        error_msg = mpManager.Value('s', '')
        lock = mpManager.Lock()
        lis_files: list[dict] = mpManager.list()
        thumbnail_map: dict[str, str] = {}
        with multiprocessing.Pool(process_count) as p:
            for i in lis:
                path: list[list[str], list[str]] = i.data(1, Qt.ItemDataRole.UserRole)
                full_path: str = sltk.join_path(*path[0], *path[1])
                if os.path.isfile(full_path):
                    if full_path.lower().endswith(EXT_PICTURE):
                        thumbnail_map[sltk.join_path(*path[1])] = full_path
                    p.apply_async(_gen_snap, args=(path[1], full_path, parent_files, lis_files, self.switch_scan_mode.currentRouteKey(), error_count, error_msg, lock), callback=_gen_snap_callback, error_callback=print)
            self.popup.title = '正在扫描文件……'
            p.close()
            p.join()
        if error_count.get() > 0:  # ValueProxy不直接支持比较
            QMetaObject.invokeMethod(self, "show_scan_error", Qt.ConnectionType.QueuedConnection,
                                     Q_ARG(str, 'create'), Q_ARG(int, error_count.get()), Q_ARG(str, str(error_msg.get())))
        return list(lis_files), thumbnail_map  # 记得转回正常类型，共享类型很多功能不完善

    def snap_retrace(self, from_id: str) -> tuple[list[dict] | str, str]:
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
            return lis_file, ''
        except Exception as e:
            QMessageBox.warning(self, "快照回溯失败", f"回溯节点 {from_id} 时出现异常，节点可能已经损坏或被异常删除")
            return '', repr(e)

    def snap_calc_delta(self, ref: list[dict[str, str | int | list | dict]], obj: list[dict[str, str | int | list | dict]]) -> tuple[list[dict[str, str | int | list | dict]], list[dict[str, list[str]]]]:
        '''!!!会修改obj，不要在该方法后复用obj!!!\n\n比较两个快照，返回`files`与`deleted`两个列表，格式与`manifest.json`相同'''
        lis_files: list[dict] = []
        lis_deleted: list[dict[str, list[str]]] = []
        for i in obj:
            # calc_delta在create/rebase快照时用到
            # rebase时obj中的type没有参考价值且不可能为same
            # create时same表示使用宽松模式跳过哈希计算，ref必定为父快照，此项一定在ref中不用判断
            if i['type'] != 'same':
                i['type'] = 'add'
        for old_item in ref:
            is_match = False
            for new_item in obj:
                if new_item['type'] == 'same':
                    is_match = True
                    break
                if old_item['path'] == new_item['path']:
                    is_match = True
                    # 都有hash时才严格比较，否则宽松比较并更新new_item的hash
                    if 'blake3' in new_item['hash'] and 'blake3' in old_item['hash']:
                        if old_item['hash']['blake3'] == new_item['hash']['blake3']:
                            new_item['type'] = 'same'
                        else:
                            new_item['type'] = 'mod'
                    else:
                        if old_item['size'] == new_item['size'] and old_item['last_edit'] == new_item['last_edit']:
                            new_item['type'] = 'same'
                            new_item['hash'] = old_item['hash'] if 'blake3' in old_item['hash'] else new_item['hash']
                        else:
                            new_item['type'] = 'mod'
                    break
                # 依赖and短路，不能改顺序
                elif 'blake3' in new_item['hash'] and 'blake3' in old_item['hash'] and old_item['hash']['blake3'] == new_item['hash']['blake3']:
                    is_match = True
                    new_item['type'] = 'move'
            if not is_match:
                lis_deleted.append({'path': old_item['path']})
        # 从后往前删不会影响索引
        for i in range(len(obj) - 1, -1, -1):
            if obj[i]['type'] in ['add', 'mod', 'move']:
                lis_files.append(obj[i])
        # 过程中修改了obj，防止复用并释放内存
        del obj
        return lis_files, lis_deleted

    def snap_rebase(self, obj_id: str, new_parent_id: str):
        '''将快照obj_id的父节点改为new_parent_id'''
        with open(sltk.join_path(self.vault_dir, "snapshots", obj_id, "manifest.json"), 'r', encoding='utf-8') as file:
            obj_config = json.load(file)
        try:
            obj_state, _ = self.snap_retrace(obj_id)
            new_parent_state, _ = self.snap_retrace(new_parent_id)
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

    def snap_delete(self, obj_id: str, popup: ProgressPopUp):
        '''删除快照obj_id'''
        history = []
        with open(sltk.join_path(self.vault_dir, "snapshots", obj_id, "manifest.json"), 'r', encoding='utf-8') as file:
            obj_config = json.load(file)
        popup.title = f'删除快照 {obj_config["comment"]} ({obj_id})'
        parent_id = obj_config['parent']
        try:
            for i in os.listdir(sltk.join_path(self.vault_dir, "snapshots")):
                manifest_path = sltk.join_path(self.vault_dir, "snapshots", i, "manifest.json")
                if not os.path.isfile(manifest_path):
                    continue
                with open(manifest_path, 'r', encoding='utf-8') as file:
                    config: dict = json.load(file)
                if config['parent'] == obj_id:
                    popup.currentItem = f'正在变基子快照 {config["comment"]} ({config["id"]})'
                    self.snap_rebase(config['id'], parent_id)
                    history.append(config['id'])
                    # 迁移缩略图，变基之后需要重新读取manifest
                    old_thumbnails = os.listdir(sltk.join_path(self.vault_dir, "snapshots", obj_id, "thumbnails"))
                    with open(manifest_path, 'r', encoding='utf-8') as file:
                        config: dict = json.load(file)
                    for j in config['files']:
                        thumbnail_name = j['hash'].get('blake3', '') + '.webp'
                        if thumbnail_name in old_thumbnails:
                            shutil.copy2(sltk.join_path(self.vault_dir, "snapshots", obj_id, "thumbnails", thumbnail_name), sltk.join_path(self.vault_dir, "snapshots", i, "thumbnails"))
            with open(sltk.join_path(self.vault_dir, "index.json"), 'r', encoding='utf-8') as file:
                index = json.load(file)
            if index['head'] == obj_id:
                index['head'] = ''
            if index['latest'] == obj_id:
                index['latest'] = parent_id
            with open(sltk.join_path(self.vault_dir, "index.json"), 'w', encoding='utf-8') as file:
                json.dump(index, file)
            shutil.rmtree(sltk.join_path(self.vault_dir, "snapshots", obj_id))
            popup.done_msg = [f'删除快照 {obj_config["comment"]} ({obj_id}) 成功', f'以下快照的父节点已从 {obj_id} 变更为 {parent_id if parent_id else "无"} ：\n{"、".join(history)}']
        except Exception as e:
            temp = self if self.isVisible() else self.mainwindow
            # QMessageBox.warning(temp, '删除快照失败', f"尝试删除快照 {obj_config['comment']} ({obj_id}) 时出现异常，删除操作已中断\n以下快照的父节点已从 {obj_id} 变更为 {parent_id if parent_id else '无'} ：\n{'、'.join(history)} \n\n{e}")
            popup.done_msg = [f'删除快照 {obj_config["comment"]} ({obj_id}) 失败', f'以下快照的父节点已从 {obj_id} 变更为 {parent_id if parent_id else "无"} ：\n{"、".join(history)} \n\n错误信息：\n{e}']
        popup.is_done = True
        QMetaObject.invokeMethod(self.mainwindow.subwin_fsa, "update_snap_list", Qt.ConnectionType.QueuedConnection)

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
                    treeWidgetItem.setIcon(0, map_icon(i, False))
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
                error_msg = repr(e)  # e离开缩进之后不可用
        if error_count:
            self.show_scan_error('scan', error_count, error_msg)
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
                    treeWidgetItem.setIcon(0, map_icon(final_path, False))
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
                            0, map_icon(final_path, True))
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


class SnapshotViewer(FluentWindow, Ui_snapshot_viewer):
    sig_setTreeWidgetItemParent = Signal(QTreeWidgetItem, QTreeWidgetItem)

    def __init__(self, mainwindow: QMainWindow):
        super().__init__()
        self.container = QWidget()
        self.setupUi(self.container)
        self.addSubInterface(self.container, None, '')
        self.setWindowTitle('快照详情')
        self.navigationInterface.setVisible(False)

        self.mainwindow = mainwindow

        self.btn_return.setIcon(FluentIcon.CANCEL)
        self.btn_show_gallery.setIcon(FluentIcon.VIEW)

        self.btn_return.clicked.connect(self.close)
        self.sig_setTreeWidgetItemParent.connect(self._setTreeWidgetItemParent)
        self.TreeWidget_add.itemSelectionChanged.connect(lambda: self.load_detail('add'))
        self.TreeWidget_mod.itemSelectionChanged.connect(lambda: self.load_detail('mod'))
        self.TreeWidget_del.itemSelectionChanged.connect(lambda: self.load_detail('del'))
        self.TreeWidget_move.itemSelectionChanged.connect(lambda: self.load_detail('move'))
        def update_show_gallery(): return self.btn_show_gallery.setEnabled(bool(len(self.TreeWidget_add.selectedIndexes()) + len(self.TreeWidget_mod.selectedIndexes()) + len(self.TreeWidget_del.selectedIndexes()) + len(self.TreeWidget_move.selectedIndexes())))
        self.TreeWidget_add.itemSelectionChanged.connect(update_show_gallery)
        self.TreeWidget_mod.itemSelectionChanged.connect(update_show_gallery)
        self.TreeWidget_del.itemSelectionChanged.connect(update_show_gallery)
        self.TreeWidget_move.itemSelectionChanged.connect(update_show_gallery)

    def _setTreeWidgetItemParent(self, child: QTreeWidgetItem, parent: QTreeWidgetItem):
        '''Slot+invokeMethod缺点是只能传递部分基本类型，而Signal可以传递任意类型'''
        parent.addChild(child)
        self._flag_setParent_done = True

    def _locateTreeWidget(self, path: list[str], file_type: str):
        '''root节点不能在子线程动，其他可以，而且建议用invisibleRootItem来统一所有节点的方法名'''
        MAP_TYPE = {'add': self.TreeWidget_add, 'mod': self.TreeWidget_mod, 'del': self.TreeWidget_del, 'move': self.TreeWidget_move}[file_type]
        current_parent = MAP_TYPE.invisibleRootItem()
        for dep in range(len(path)):  # 含头不含尾
            for i in range(current_parent.childCount()):
                if current_parent.child(i).data(0, Qt.ItemDataRole.UserRole) == path[:dep + 1]:
                    current_parent = current_parent.child(i)
                    break
            else:
                temp = QTreeWidgetItem(current_parent)
                temp.setData(0, Qt.ItemDataRole.UserRole, path[:dep + 1])
                temp.setText(0, path[dep])
                temp.setExpanded(False)
                self._flag_setParent_done = False
                self.sig_setTreeWidgetItemParent.emit(temp, current_parent)
                while self._flag_setParent_done == False:
                    time.sleep(0)
                current_parent = temp
        # lis_items=w.findItems('*', Qt.MatchFlag.MatchWildcard | Qt.MatchFlag.MatchRecursive, 0)
        # for dep in range(0,len(path)): # 含头不含尾，但下方切片又不含尾，且[:0]为空没意义，要+1
        #     for i in lis_items:
        #         if i.data(0, Qt.ItemDataRole.UserRole) == path[:dep+1]:
        #             current_parent = i
        #             break
        #     else:
        #         temp = QTreeWidgetItem(current_parent)
        #         temp.setData(0, Qt.ItemDataRole.UserRole, path[:dep+1])
        #         temp.setText(0, path[dep])
        #         temp.setExpanded(False)
        #         current_parent = temp

    def view_snapshot(self, vault_dir, snap_id):
        self.vault_dir = vault_dir
        self.snap_id = snap_id
        self.TreeWidget_add.clear()
        self.TreeWidget_mod.clear()
        self.TreeWidget_del.clear()
        self.TreeWidget_move.clear()
        with open(sltk.join_path(vault_dir, 'snapshots', snap_id, 'manifest.json'), 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        def worker():
            QMetaObject.invokeMethod(self, 'setWindowTitle', Qt.ConnectionType.QueuedConnection, Q_ARG(str, f'快照详情 ({snap_id}) - 加载中...'))
            for i in manifest['files']:
                if not self.flag_running:
                    return
                self._locateTreeWidget(i['path'], i['type'])
            for i in manifest['deleted']:
                if not self.flag_running:
                    return
                self._locateTreeWidget(i['path'], 'del')
            QMetaObject.invokeMethod(self, 'setWindowTitle', Qt.ConnectionType.QueuedConnection, Q_ARG(str, f'快照详情 ({snap_id})'))
        self.show()  # 先修改flag_running的值
        threading.Thread(target=worker).start()

    def load_detail(self, trigger: str):
        def update_data(data: dict[str, str | dict[str, str]]) -> str:
            self.label_file_path.setText(sltk.join_path(*data['path']))
            self.label_size_data.setText(sltk.bit2size(data.get('size', 0)))
            self.label_mtime_data.setText(time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(str(data.get('last_edit', 19700101000000)), r"%Y%m%d%H%M%S")))
            self.label_md5_data.setText(data.get('hash', {}).get('md5', ''))
            self.label_crc32_data.setText(data.get('hash', {}).get('crc32', ''))
            self.label_blake3_data.setText(thumb_name := data.get('hash', {}).get('blake3', ''))
            self.label_sha1_data.setText(data.get('hash', {}).get('sha1', ''))
            self.label_sha256_data.setText(data.get('hash', {}).get('sha256', ''))
            return thumb_name
        lis_type = ['add', 'mod', 'del', 'move']
        MAP_TYPE = {'add': self.TreeWidget_add, 'mod': self.TreeWidget_mod, 'del': self.TreeWidget_del, 'move': self.TreeWidget_move}
        selected_item = MAP_TYPE[trigger].selectedItems()
        if selected_item:
            selected_item = selected_item[0]
        else:
            return
        path: list[str] = selected_item.data(0, Qt.ItemDataRole.UserRole)
        lis_type.remove(trigger)
        MAP_TYPE[lis_type[0]].clearSelection()
        MAP_TYPE[lis_type[1]].clearSelection()
        MAP_TYPE[lis_type[2]].clearSelection()
        if selected_item.childCount() > 0:
            update_data({'path': path})
            self.ImageLabel.setImage(FluentIcon.icon(FluentIcon.FOLDER).pixmap(256, 256))
            self.ImageLabel.scaledToWidth(100)
            return

        with open(sltk.join_path(self.vault_dir, 'snapshots', self.snap_id, 'manifest.json'), 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        if trigger == 'del':
            parent_id = manifest['parent']
            while parent_id:
                with open(sltk.join_path(self.vault_dir, 'snapshots', parent_id, 'manifest.json'), 'r', encoding='utf-8') as f:
                    manifest = json.load(f)
                for i in manifest['files']:
                    if i['path'] == path:
                        i['path'].insert(0, f'@{parent_id}')
                        thumb_name = sltk.join_path(self.vault_dir, 'snapshots', parent_id, 'thumbnails', update_data(i) + '.webp')
                        parent_id = ''
                        break
                else:
                    parent_id = manifest['parent']
        else:
            for i in manifest['files']:
                if i['path'] == path:
                    thumb_name = sltk.join_path(self.vault_dir, 'snapshots', self.snap_id, 'thumbnails', update_data(i) + '.webp')
                    break

        if os.path.isfile(thumb_name):
            self.ImageLabel.setImage(thumb_name)
        else:
            self.ImageLabel.setImage(map_icon(path[-1], False).pixmap(256, 256))
            self.ImageLabel.scaledToWidth(100)

    def showEvent(self, e):
        self.flag_running = True
        self.mainwindow.hide()
        self.resize(800, 500)
        return super().showEvent(e)

    def closeEvent(self, e):
        self.flag_running = False
        self.mainwindow.show()
        return super().closeEvent(e)
