# 神龙工具箱v2.1

## 插件名称对应表

|中文名|英文全称|缩写|
|-|-|-|
|~~*安卓应用数据备份*~~|~~*Android application backup*~~|~~*aab*~~|
|安卓应用管理|Android application manage|aam|
|文件软链接|create symbol link|csl|
|文件校验|file hash check|fhc|
|文件实时同步|file auto sync|fas|

## 依赖项目  

- **PySide6** [*https://doc.qt.io/qtforpython-6/index.html*]
- **PyQt-Fluent-Widgets** [*https://qfluentwidgets.com*]
- **python_downloader** [*https://github.com/panmeibing/python_downloader*]
- **Nuitka** [*https://nuitka.net*]
- **Pyinstaller** [*https://www.pyinstaller.org*]

## 更新日志

### v1.0

- 安卓应用数据备份

- 文件软链接

### v1.1

- ~~*安卓应用数据备份*~~ --> 安卓应用管理

- 新增安装、卸载、冻结、解冻、命令行等功能

- 更改了 ***暗黑主题*** `qdarkstyle`

### v1.2

- 新增文件校验功能

- 新增设置，支持本地保存

- 允许自定义主题和动画

- 新增文件拖拽校验

- 新增apk拖拽安装

### v2.0

- 更换设计风格为 `fluent design`

- 修复 [v1.2版本](#v12) 中 [fhc组件](#插件名称对应表) 拖拽文件变为 `file:///` 的bug

- 将各窗口独立为plugins,减少 [main.py](main.py) 中的代码

- [csl组件](#插件名称对应表) 支持拖拽文件夹

- [aam组件](#插件名称对应表) 支持筛选应用类型

- [aam组件](#插件名称对应表) 支持包名自动填充

- [aam组件](#插件名称对应表) 新增应用图标/名称、安卓版本、应用数量统计

## v2.1

- 新增文件实时同步功能 [fas组件](#插件名称对应表)

- [fhc组件](#插件名称对应表) 新增CRC校验

- [fhc组件](#插件名称对应表) 引入多线程，同时支持分块校验