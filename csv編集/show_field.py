import numpy as np

#--------------------------------------------------------------------
#2：フィールドごとに表示
#--------------------------------------------------------------------
def show_field(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    for i in range(col_len):
        print(f"[フィールド{i+1}]")
        for j in range(row_len):
            print(f"\tレコード{j+1} : {two_D_list[j][i]}")