import sys                  #正常終了するために導入したライブラリ
import numpy as np          #2次元配列の行の要素数と列の要素数を取得するために導入したライブラリ
from pathlib import Path    #/Users/yourname/下のcsvディレクトりを読み込むためのライブラリ

path = Path.home()/"csv"/"sample.csv"

#--------------------------------------------------------------------
#CSVファイルの文字列を取得
#--------------------------------------------------------------------
def get_csv():
    with open(path) as f:
        i = 0
        hozon = []                  #1文字づつ保存
        one_D_list = []             #1次元の文字列をリストとして保存
        two_D_list = []             #2次元リストとして文字列を保存
        field_flag = 0              #フィールド内にカンマの存在を判定
        double_quotation_flag = 0   #ダブルクォーテーションが2回連続で記述されているかを確かめるフラグ
        line_break_flag = 0         #改行が2回連続で記述されているかを確かめるフラグ
        double_quotation_count = 0  #フィールド内にあるダブルクォーテーションを数えます

        while True:
            f.seek(i)
            c = f.read(1)

            if not c:               #c == EOFの時break
                if hozon:
                    one_D_list.append("".join(hozon))
                    two_D_list.append(one_D_list)
                break

            if c == '"':
                double_quotation_count += 1
                line_break_flag = 0
                if field_flag == 0:
                    field_flag = 1
                else:
                    field_flag = 0

                if double_quotation_flag == 0:
                    double_quotation_flag = 1
                else:
                    hozon.append(c)
                    double_quotation_flag = 0
            else:
                double_quotation_flag = 0
                if c == ",":
                    line_break_flag = 0
                    if field_flag == 0:
                        one_D_list.append("".join(hozon))
                        hozon =[]
                        if double_quotation_count % 2 == 1:
                            print("フィールド内にダブルクォーテーションが奇数個あります。")
                            print("参照ファイルを確認してください。")
                            exit(1)
                        double_quotation_count = 0
                    else:
                        hozon.append(c)
                elif c == "\n":
                    if line_break_flag == 0:
                        line_break_flag = 1
                        one_D_list.append("".join(hozon))
                        two_D_list.append(one_D_list)
                        hozon = []
                        one_D_list = []
                        if double_quotation_count % 2 == 1:
                            print("フィールド内にダブルクォーテーションが奇数個あります。")
                            print("参照ファイルを確認してください。")
                            exit(1)
                        double_quotation_count = 0
                    else:
                        break
                else:
                    hozon.append(c)
            i += 1
        return two_D_list

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

#--------------------------------------------------------------------
#3：編集
#--------------------------------------------------------------------
def edit_csv(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    while True:
        r = input("レコード番号を入力してください。\n編集を中止する場合はxを入力してください。 : ")
        if r == "x":
            return main_manu(two_D_list)
        elif int(r) > row_len:
            print("存在しないレコードです。")
            print("もう一度入力してください。")
        else:
            r = int(r)
            break
    while True:
        f = input("フィールド番号を入力してください：\n編集を中止する場合はxを入力してください。 : ")
        if f == "x":
            return main_manu(two_D_list)
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

#--------------------------------------------------------------------
#4：保存
#--------------------------------------------------------------------
def store_csv(two_D_list):
    arr_2d = np.array(two_D_list)
    row_len, col_len = arr_2d.shape
    with open(path, mode="w") as f:
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
#--------------------------------------------------------------------
#メインメニュー
#--------------------------------------------------------------------
def main_manu(two_D_list):
    while True:
        print("-------------------------------------------")
        print("1 : レコードごとに表示")
        print("2 : フィールドごとに表示")
        print("3 : 編集")
        print("4 : 保存")
        print("0 : 終了")
        print("-------------------------------------------")
        x = int(input("番号を入力してください : "))

        if x == 0:
            print("編集を終了しました。")
            sys.exit(0)
        elif x == 1:
            show_record(two_D_list)
        elif x == 2:
            show_field(two_D_list)
        elif x == 3:
            edit_csv(two_D_list)
        elif x == 4:
            store_csv(two_D_list)
        else:
            print("入力番号が認識されません。")
            print("もう一度入力してください")

main_manu(two_D_list = get_csv())