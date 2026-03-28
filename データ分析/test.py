import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import rcParams
import platform

# ===== フォント設定（安全版）=====
os_name = platform.system()

if os_name == "Darwin":  # Mac
    rcParams['font.family'] = 'Hiragino Sans'
elif os_name == "Windows":
    rcParams['font.family'] = 'Yu Gothic'
else:
    rcParams['font.family'] = 'DejaVu Sans'

# ===== ① 銘柄コード入力 =====
code = input("銘柄コードを入力してください（例：4755.T）: ")

# ===== ② 期間入力 =====
start_date = input("開始日を入力してください（例：2023-01-01）: ")
end_date = input("終了日を入力してください（例：2024-01-01）: ")

# ===== ③ 企業名取得（安全化）=====
ticker = yf.Ticker(code)
try:
    name = ticker.info.get("longName", code)
    if isinstance(name, list):
        company_name = name[0]
    else:
        company_name = name
except:
    company_name = code

# ===== ④ データ取得 =====
df = yf.download(code, start=start_date, end=end_date)

# データ取得チェック
if df.empty:
    print("データ取得失敗：銘柄コードや日付を確認してください")
    exit()

# ===== ⑤ 移動平均 =====
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA25"] = df["Close"].rolling(window=25).mean()

# ===== ⑥ グラフ（改善版）=====
fig, ax1 = plt.subplots(figsize=(12, 6))

# 株価
ax1.plot(df.index, df["Close"], label="株価", linewidth=2)
ax1.plot(df.index, df["MA5"], label="5日平均", linestyle="--")
ax1.plot(df.index, df["MA25"], label="25日平均", linestyle="--")

ax1.set_xlabel("日付")
ax1.set_ylabel("株価（円）")
ax1.grid(True)

# 出来高（別軸）
ax2 = ax1.twinx()
ax2.bar(df.index, df["Volume"].squeeze(), alpha=0.3)
ax2.set_ylabel("出来高")

# タイトル
ax1.set_title(f"{company_name} の株価推移（{start_date}〜{end_date}）")

# 凡例
ax1.legend(loc="upper left")

plt.tight_layout()
plt.show()