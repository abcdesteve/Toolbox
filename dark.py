__version__ = 20230520

STYLESHHET_DARK = """
QMainWindow{background-color:#282828;  border-radius:20px}

QWidget{background-color:#282828;  border-radius:5px}

QLabel{color:#f0f0f0}

QMessageBox {background-color:#282828;  color:#f0f0f0;  }
QMessageBox QLabel {color:#f0f0f0;  }
QMessageBox QPushButton {background-color:#353535;  color:#f0f0f0;  border:none;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#585858;  }
QMessageBox QPushButton:pressed {background-color:#444444;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#f0f0f0;  border:none;  }
QMessageBox QPushButton#closeButton:hover {color:#ff0000;  }
QMessageBox QPushButton#closeButton:pressed {color:#cc0000;  }


QTabWidget {background-color:#333333;  }
QTabBar::tab {background-color:#333333;  border-radius:5px;  color:#ffffff;  padding:8px 12px;  margin-right:4px;  }
QTabBar::tab:selected {background-color:#4cc2ff;  color:#000000;  }
QTabBar::tab:!selected:hover {background-color:#585858;  }
QTabBar::tab:!selected:selected {background-color:#0078d7;  }
QTabWidget::pane {background-color:#585858;  }

"""

STYLESHHET_LIGHT = """
QMainWindow{background-color:#f5f5f5;  border-radius:20px}

QWidget{background-color:#f5f5f5;  border-radius:5px}

QLabel{color:#1e1e1e}

QMessageBox {background-color:#f5f5f5;  color:#1e1e1e;  }
QMessageBox QLabel {color:#1e1e1e;  }
QMessageBox QPushButton {background-color:#bfbfbf;  color:#1e1e1e;  border:none;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#a9a9a9;  }
QMessageBox QPushButton:pressed {background-color:#d0d0d0;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#1e1e1e;  border:none;  }
QMessageBox QPushButton#closeButton:hover {color:#ff7f7f;  }
QMessageBox QPushButton#closeButton:pressed {color:#ff6666;  }

QTabWidget {background-color:#333333;  border-radius:5px;  }
QTabBar::tab {background-color:#333333;  border-radius:5px;  color:#ffffff;  padding:8px 12px;  margin-right:4px;  }
QTabBar::tab:selected {background-color:#83b7ff;  color:#ffffff;  }
QTabBar::tab:!selected:hover {background-color:#a9a9a9;  }
QTabBar::tab:!selected:selected {background-color:#83b7ff;  }
QTabWidget::pane {background-color:#a9a9a9;  }

"""


def apply_dark(app):
    import darkdetect
    from qfluentwidgets.common import setTheme, Theme, setThemeColor

    setThemeColor("#4cc2ff")
    if darkdetect.isDark():
        setTheme(Theme.DARK)
        app.setStyleSheet(STYLESHHET_DARK)
    else:
        setTheme(Theme.LIGHT)
        # app.setStyleSheet(STYLESHHET_LIGHT)
