import sys
import show_record as sr
import show_field as sf
import edit_csv as ec
import store_csv as sc
import get_csv as gc

two_D_list = gc.get_csv()

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

        num = input("番号を入力してください : ")

        try:
            x = int(num)
            if x == 0:
                print("編集を終了しました。")
                sys.exit(0)
            elif x == 1:
                sr.show_record(two_D_list)
            elif x == 2:
                sf.show_field(two_D_list)
            elif x == 3:
                ec.edit_csv(two_D_list)
            elif x == 4:
                sc.store_csv(two_D_list)
            else:
                print("入力番号が認識されません。")
                print("もう一度入力してください")
        except ValueError: 
            print("数字以外の文字が入力されています。")
            print("もう一度入力してください")

if __name__ == "__main__":
    main_manu(two_D_list)