from PySide6.QtWidgets import QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from config import UI_DIR

error_window_not_exist = None

def error_ui():
    global error_window_not_exist
    loader = QUiLoader()
    ui_file = QFile(UI_DIR/"not_exist.ui")
    if not ui_file.open(QFile.ReadOnly):
        #print("UIファイルを開けません")
        return
    error_window_not_exist = loader.load(ui_file)  # QFile を渡す
    ui_file.close()

    ok_button : QPushButton = error_window_not_exist.findChild(QPushButton, "ok_button")

    ok_button.clicked.connect(error_window_not_exist.close)

    error_window_not_exist.show()