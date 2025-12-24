import numpy as np
import main as mm

#--------------------------------------------------------------------
#3：編集
#--------------------------------------------------------------------
def edit_csv(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    while True:
        r = input("レコード番号を入力してください。\n編集を中止する場合はxを入力してください。 : ")
        if r == "x":
            print("編集を中止しました。")
            return mm.main_manu(two_D_list)
        elif int(r) > row_len:
            print("存在しないレコードです。")
            print("もう一度入力してください。")
        else:
            r = int(r)
            break
    while True:
        f = input("フィールド番号を入力してください：\n編集を中止する場合はxを入力してください。 : ")
        if f == "x":
            print("編集を中止しました。")
            return mm.main_manu(two_D_list)
        elif int(f) > col_len:
            print("存在しないフィールドです。")
            print("もう一度入力してください。")
        else:
            f = int(f)
            break

    print(f"変更前のデータ：{two_D_list[r-1][f-1]}")
    del two_D_list[r-1][f-1]
    s = input("変更後のデータを入力してください：")
    two_D_list[r-1].insert(f-1,s)