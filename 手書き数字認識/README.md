## Overview
- Pytorchを用いて手書き数字の10~15を識別するCNNモデルを実装しました
- AI技術の理解を深めるため、ChatGPTを活用しながらプロジェクトを作成しました

---

## 制作目的
- AI技術の理解を深めるため
- 畳み込みニューラルネットワークの理解を深めるため

---

## 実行方法
1. 本リポジトリをクローンします
2. お使いのOSに合わせてconfig.pyの**BASE_DIR**を変更してください

windowの場合は"C:"に変更してください。

macの場合は変更する必要はありません。

3. 環境の準備

Python 3.8 以上が必要です。

依存ライブラリは以下の通りです:

- torch
- torchvision
- matplotlib
- pillow
- numpy
- pygame

インストールはpipでまとめて可能です。
```
pip install torch torchvision matplotlib pillow numpy pygame
```

4. main.pyを実行します

---

## 工夫した点
- 簡単な絵描きアプリを作成し、ユーザーが描いた数字を直接CNNモデルで推論して分類結果を表示できるようにしました。
- 描画した画像は自動で前処理（リサイズ・グレースケール化・正規化）されるため、学習済みモデルにそのまま入力可能です。
- MNISTの数字をつなげて作成したデータセットで推論精度が低かったため、数字間の幅を10ピクセル縮める前処理を行い、識別精度を改善しました。

---

## Dataset
datasetの10\~15はMNISTの0\~5を組み合わせて作成しました。

---

## 学習曲線
<img width="1200" height="500" alt="Image" src="https://github.com/user-attachments/assets/d6466376-e740-4277-8070-be627cc8937f" />

---

## 使用例
<img width="555" height="305" alt="Image" src="https://github.com/user-attachments/assets/476009ee-306f-4e7e-81ad-d060d27daf82" />

<img width="560" height="306" alt="Image" src="https://github.com/user-attachments/assets/2e1e5876-d4c4-4648-961a-9b9b0c246e81" />

<img width="554" height="305" alt="Image" src="https://github.com/user-attachments/assets/a773ddc3-3cf1-4e83-87e4-caef4fea0250" />

<img width="552" height="302" alt="Image" src="https://github.com/user-attachments/assets/66ed691b-fcd3-4501-92ca-1dae0d952826" />

<img width="557" height="300" alt="Image" src="https://github.com/user-attachments/assets/c732d217-834a-40e6-b354-62bcc6d2f677" />

<img width="554" height="305" alt="Image" src="https://github.com/user-attachments/assets/0e76f011-5ff8-47f6-8a92-6a8fa7465ae4" />