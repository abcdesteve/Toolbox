__version__ = 20231119

import winreg
import darkdetect
from qfluentwidgets import setTheme, Theme, setThemeColor ,theme,FluentIcon
from PySide6.QtGui import QColor

def get_system_color():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM")
            value, _ = winreg.QueryValueEx(key, "ColorizationColor")
            alpha = (value >> 24) & 0xFF
            red = (value >> 16) & 0xFF
            green = (value >> 8) & 0xFF
            blue = value & 0xFF
            return QColor(red, green, blue,alpha)
        except Exception as e:
            # print("获取个性化颜色失败:", repr(e))
            return QColor(41, 241, 255)

def apply_theme(app,goal_theme:str):
    '''supported theme:\nauto\nlight\ndark'''
    # setThemeColor("#4cc2ff")
    # setThemeColor('#e81123')
    setThemeColor(get_system_color())
    goal_theme=goal_theme.lower()
    if goal_theme=='auto':
        goal_theme=('dark' if darkdetect.isDark() else 'light')
    if goal_theme=='dark':
        setTheme(Theme.DARK)
        app.setStyleSheet(STYLESHHET_DARK)
    else:
        setTheme(Theme.LIGHT)
        app.setStyleSheet(STYLESHHET_LIGHT)


STYLESHHET_DARK = """
QLabel {color:#f0f0f0}

ScrollArea {border: none;background-color: transparent}

QGroupBox {background-color:transparent;color:#f0f0f0}
QSplitter::handle {background-color:transparent}

QMessageBox {background-color:#282828;  color:#f0f0f0;  border-radius:5px}
QMessageBox QLabel {color:#f0f0f0;  }
QMessageBox QPushButton {background-color:#353535;  color:#f0f0f0;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#585858;  }
QMessageBox QPushButton:pressed {background-color:#444444;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#f0f0f0;}
QMessageBox QPushButton#closeButton:hover {color:#ff0000;  }
QMessageBox QPushButton#closeButton:pressed {color:#cc0000;  }
"""


STYLESHHET_LIGHT ='''
/*QMainWindow{background-color:#f0f0f0;  border-radius:20px}

QWidget{background-color:#f0f0f0;  border-radius:5px}
QTabWidget{background-color:#ffffff;border-radius:0px}*/

QLabel{color:#000000}
QGroupBox{background-color:transparent;color:#000000}

QMessageBox {background-color:#f0f0f0;  color:#000000;  border-radius:5px}
QMessageBox QLabel {color:#000000;  }
QMessageBox QPushButton {background-color:#585858;  color:#000000;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#585858;  }
QMessageBox QPushButton:pressed {background-color:#444444;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#000000;}
QMessageBox QPushButton#closeButton:hover {color:#ff0000;  }
QMessageBox QPushButton#closeButton:pressed {color:#cc0000;  }

/*QTabWidget {background-color:#ffffff;  border-radius:5px;  }
QTabBar::tab {background-color:#ffffff;  border-radius:5px;  color:#000000;  padding:8px 12px;  margin-right:4px;  }
QTabBar::tab:selected {background-color:#4cc2ff;  color:#ffffff;  }
QTabBar::tab:!selected:hover {background-color:#585858;  }
QTabBar::tab:!selected:selected {background-color:#4cc2ff;  }
QTabWidget::pane {background-color:#585858;  }*/
'''