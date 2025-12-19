from config import CSV_DIR

#--------------------------------------------------------------------
#CSVファイルの文字列を取得
#--------------------------------------------------------------------
def get_csv():
    with open(CSV_DIR) as f:
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
