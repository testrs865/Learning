## Overview
- Pythonで実装した、CSVファイルを表示・編集・保存できるコマンドラインツールです
- 標準ライブラリを中心に使用し、CSVの構造（カンマ・改行・ダブルクォーテーション）を自前で解析・処理しています

---

## 制作目的

- Pythonの基礎文法（条件分岐・ループ・関数）の理解を深めるため
- CSVファイルの仕様を理解するため
- 入力ミスや不正データに対するエラーハンドリングを学ぶため
- CUI形式の業務ツールを想定したプログラム構成を意識するため

※ 学習目的で作成したコードです。  
可読性と処理の流れが分かりやすいことを重視しています。

---

## 実行方法
1. 本リポジトリをクローンします
2. config.pyにて**BASE_DIR**をmacOSなら**Path.home()** に、windowsなら**C:** にしてください
3. 上記のディレクトリ下に **/"csv"/"sample.csv"**　を配置してください
4. main.pyを実行してください

---

## 工夫した点
- csv モジュールを使わず、ファイルを1文字ずつ読み込んで解析
- フィールド内のダブルクォーテーション数をカウントし、不正なCSVを検出
- 入力ミス時にプログラムが異常終了しないようループ制御を実装
- データ構造を2次元リストで統一し、処理を分かりやすく整理

---
## 使用例

<img width="642" height="492" alt="Image" src="https://github.com/user-attachments/assets/647b6dae-9dae-4fe9-b2b8-d3c047fa31fc" />

<img width="670" height="320" alt="Image" src="https://github.com/user-attachments/assets/82b8b9a6-6d89-4fd5-a3cd-ba1e21d27554" />

<img width="614" height="658" alt="Image" src="https://github.com/user-attachments/assets/eb5b3134-03cb-48c2-b38c-efb15b17c200" />

<img width="620" height="230" alt="Image" src="https://github.com/user-attachments/assets/353b6a16-2899-4227-aded-cb663b09e4b6" />

<img width="674" height="252" alt="Image" src="https://github.com/user-attachments/assets/34976c6b-a3c7-4c7b-b600-066a02f6ad14" />

<img width="310" height="120" alt="Image" src="https://github.com/user-attachments/assets/14d15a86-f16a-4524-be09-0579b0b2cd17" />