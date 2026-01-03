from PySide6.QtWidgets import QApplication, QListView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QStandardItemModel
from config import UI_DIR
import sys
import get_csv as gc
import show_record as sr
import show_field as sf
import edit_csv as ec
import store_csv as sc

def main():

    two_D_list = gc.get_csv()

    app = QApplication(sys.argv)

    file = QFile(UI_DIR/"csv_edit.ui")
    if not file.open(QFile.ReadOnly):
        #print("UIファイルを開けません:", file.fileName())
        sys.exit(1)

    loader = QUiLoader()
    window = loader.load(file)
    file.close()

    # モデルを作って UI の listView にセット
    list_view = window.findChild(QListView, "listView")
    model = QStandardItemModel()
    list_view.setModel(model)

    #レコード表示
    window.record_show.clicked.connect(
        lambda : sr.show_record_ui(two_D_list, model)          #実行する前に関数を呼び出す
        )

    #フィールド表示
    window.field_show.clicked.connect(
        lambda : sf.show_field_ui(two_D_list, model)
    )

    #編集
    window.edit.clicked.connect(
        lambda : ec.edit_csv_ui(two_D_list)
    )

    #保存
    window.store.clicked.connect(
        lambda : sc.store_csv_ui(two_D_list)
    )

    #終了
    window.close_button.clicked.connect(
        window.close
    )

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()