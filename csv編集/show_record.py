import numpy as np
from PySide6.QtGui import QStandardItem

#--------------------------------------------------------------------
#1：レコードごとに表示
#--------------------------------------------------------------------
def show_record_ui(two_D_list, model):
    model.clear()  # 前のデータを消す
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    for i in range(row_len):
        model.appendRow(QStandardItem(f"[レコード{i+1}]"))
        for j in range(col_len):
            model.appendRow(QStandardItem(f"\tフィールド{j+1} : {two_D_list[i][j]}"))