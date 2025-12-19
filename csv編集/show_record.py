import numpy as np

#--------------------------------------------------------------------
#1：レコードごとに表示
#--------------------------------------------------------------------
def show_record(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    for i in range(row_len):
        print(f"[レコード{i+1}]")
        for j in range(col_len):
            print(f"\tフィールド{j+1} : {two_D_list[i][j]}")
