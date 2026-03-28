import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import rcParams
import platform

os_name = platform.system()

if os_name == "Darwin":  # Mac
    rcParams['font.family'] = 'Hiragino Sans'
elif os_name == "Windows":
    rcParams['font.family'] = 'Yu Gothic'
else:
    rcParams['font.family'] = 'DejaVu Sans'  # Linuxなど

# ① 銘柄コード入力
code = input("銘柄コードを入力してください（例：4755.T）: ")

# ② 期間入力
start_date = input("開始日を入力してください（例：2023-01-01）: ")
end_date = input("終了日を入力してください（例：2024-01-01）: ")

# ③ 企業名取得
ticker = yf.Ticker(code)
company_name = ticker.info.get("longName", code)

# ④ データ取得
df = yf.download(code, start=start_date, end=end_date)

# ⑤ 移動平均
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA25"] = df["Close"].rolling(window=25).mean()

# ⑥ グラフ
plt.figure(figsize=(12,5))
plt.plot(df["Close"], label="株価")
plt.plot(df["MA5"], label="5日平均")
plt.plot(df["MA25"], label="25日平均")

plt.title(f"{company_name} の株価推移（{start_date}〜{end_date}）")
plt.xlabel("日付")
plt.ylabel("株価（円）")

#plt.bar(df.index, df["Volume"].values)

plt.legend()
plt.grid(True)
plt.show()