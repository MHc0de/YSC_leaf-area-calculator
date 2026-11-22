import os
os.environ["QT_FONT_DPI"] = "96"
import sys
import ctypes
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QTimer, Qt

from resource_utils import resource_path
from splash import SplashScreen
from gui.main_window import MainWindow

if __name__ == "__main__":
    myappid = 'yippee_sizecalculator_2.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("logo_icon.ico")))
    pixmap = QPixmap(resource_path("gui/images/logo_home_text.png"))
    splash = SplashScreen(pixmap)
    splash.show()
    splash.showMessage("Launching Yippee Size Calculator...", Qt.AlignBottom | Qt.AlignCenter, Qt.black)
    fade_anim = splash.fade_in(duration=1000)
    app.processEvents()

    # Taskbar dummy(선택, 필요 시만)
    dummy = QMainWindow()
    dummy.setWindowIcon(QIcon(resource_path("logo_icon.ico")))
    dummy.show()
    dummy.hide()

    def show_main():
        window = MainWindow()
        splash.finish(window)
        window.show()

    QTimer.singleShot(2000, show_main)
    sys.exit(app.exec())
