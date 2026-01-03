import numpy as np
from PySide6.QtGui import QStandardItem

#--------------------------------------------------------------------
#2：フィールドごとに表示
#--------------------------------------------------------------------
def show_field_ui(two_D_list, model):
    model.clear()
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    for i in range(col_len):
        model.appendRow(QStandardItem(f"[フィールド{i+1}]"))
        for j in range(row_len):
            model.appendRow(QStandardItem(f"\tレコード{j+1} : {two_D_list[j][i]}"))