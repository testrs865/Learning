import numpy as np
from config import CSV_DIR

#--------------------------------------------------------------------
#4：保存
#--------------------------------------------------------------------
def store_csv(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    with open(CSV_DIR, mode="w") as f:
        temp_hozon = []         #リストを文字列を分解して一時的に保存するためのリスト
        comma_flag = 0          #リスト内にカンマがあるかどうか判断するフラグ
        for i in range(row_len):
            for j in range(col_len):
                temp_hozon = list(two_D_list[i][j])
                for k in range(len(temp_hozon)):
                    if temp_hozon[k] == '"':
                        del temp_hozon[k]
                        temp_hozon.insert(k, '""')
                    elif temp_hozon[k] == ',':
                        comma_flag = 1
                if comma_flag == 1:
                    temp_hozon.insert(0, '"')
                    temp_hozon.append('"')
                f.write("".join(temp_hozon))
                temp_hozon = []
                if i == row_len-1 and j == col_len-1:
                    f.write("")
                elif j == col_len-1:
                    f.write('\n')
                else:
                    f.write(",")
                comma_flag = 0
    print("保存しました。")

if __name__ == "__main__":
    store_csv()