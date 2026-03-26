import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from config import CSV_DIR

# データ読み込み
df = pd.read_csv(CSV_DIR)

# 商品カテゴリごとの平均売上
category_avg = df.groupby("商品カテゴリ")["売上"].mean()

# 日本語フォント指定（Windowsの場合）
#rcParams['font.family'] = 'Yu Gothic'
rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

# 横並びのグラフ（1行2列）
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # figsizeでサイズ調整

# ① 日別売上
axes[0].bar(df.index, df["売上"])
axes[0].set_xticks(df.index)
axes[0].set_xticklabels(df["日付"], rotation=45)
axes[0].set_xlabel("日付")
axes[0].set_ylabel("売上")
axes[0].set_title("日別売上")

# ② カテゴリ別平均売上
axes[1].bar(category_avg.index, category_avg.values, color="skyblue")
axes[1].set_xlabel("商品カテゴリ")
axes[1].set_ylabel("平均売上")
axes[1].set_title("カテゴリ別平均売上")

plt.tight_layout()  # グラフが重ならないように調整
plt.show()