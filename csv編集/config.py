from pathlib import Path    #/Users/yourname/下のcsvディレクトりを読み込むためのライブラリ

BASE_DIR = Path.home()          #windowsの場合はC:に変更
CSV_DIR = BASE_DIR/"csv"/"sample.csv"
UI_DIR = BASE_DIR/"Learning"/"csv編集"/"ui"