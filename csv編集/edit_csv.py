import numpy as np
import error as er
from PySide6.QtWidgets import QLineEdit, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from config import UI_DIR

edit_window = None      #どこかに参照を保持する（global / main の変数 / クラスの属性）

#--------------------------------------------------------------------
#3：編集
#--------------------------------------------------------------------
def edit_csv_ui(two_D_list):
    global edit_window
    loader = QUiLoader()
    ui_file = QFile(UI_DIR/"edit.ui")
    if not ui_file.open(QFile.ReadOnly):
        print("UIファイルを開けません")
        return
    edit_window = loader.load(ui_file)  # QFile を渡す
    ui_file.close()

    #UI内のウィジェットを取得
    record_edit: QLineEdit = edit_window.findChild(QLineEdit, "record_edit")         #windowの中からQLineeditのrecord_editオブジェクトを探す
    field_edit: QLineEdit = edit_window.findChild(QLineEdit, "field_edit")
    change_edit: QLineEdit = edit_window.findChild(QLineEdit, "change_edit")
    ok_button: QPushButton = edit_window.findChild(QPushButton, "ok_button")
    cancel_button: QPushButton = edit_window.findChild(QPushButton, "cancel_button_2")

    def on_ok_clicked():
        # arr_2d = np.array(two_D_list)
        # row_len, col_len = arr_2d.shape
        try:
            # int に変換して保存
            r = int(record_edit.text())
            f = int(field_edit.text())
        except ValueError:
            er.error_ui()
            #print("レコード番号・フィールド番号は整数で入力してください")

            #return  # 数字でなければ処理を中断

        # 変更後の値は文字列で保存
        s = change_edit.text()

        #print(f"変更前のデータ：{two_D_list[r-1][f-1]}")
        del two_D_list[r-1][f-1]
        two_D_list[r-1].insert(f-1,s)

        record_edit.clear()
        field_edit.clear()
        change_edit.clear()

    ok_button.clicked.connect(on_ok_clicked)
    cancel_button.clicked.connect(edit_window.close)

    edit_window.show()
