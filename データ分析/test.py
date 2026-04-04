import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import rcParams
import platform


# フォント設定
def set_font():
    os_name = platform.system()

    if os_name == "Darwin":  # Mac
        rcParams['font.family'] = 'Hiragino Sans'
    elif os_name == "Windows":
        rcParams['font.family'] = 'Yu Gothic'
    else:
        rcParams['font.family'] = 'DejaVu Sans'

# 情報入力
def get_user_input():
    # 銘柄コード入力
    code = input("銘柄コードを入力してください（例：4755.T）: ")

    # 期間入力
    start = input("開始日を入力してください（例：2023-01-01）: ")
    end = input("終了日を入力してください（例：2024-01-01）: ")

    return code, start, end

# データ取得
def get_stock_data(code, start, end):
    return yf.download(code, start=start, end=end)

# 企業名取得
def get_company_name(code):
    ticker = yf.Ticker(code)
    try:
        name = ticker.info.get("longName", code)
        if isinstance(name, list):
            company_name = name[0]
        else:
            company_name = name
    except:
        company_name = code

# 移動平均計算
def calculate_moving_averages(df):
    df["MA5"] = df["Close"].rolling(window=5).mean()
    df["MA25"] = df["Close"].rolling(window=25).mean()
    return df

# RSI計算
def clculate_rsi(df):
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

# ゴールデン・デッドクロス検出
def generate_cross_signals(df):
    df["Signal"] = 0
    df.loc[df["MA5"] > df["MA25"], "Signal"] = 1
    df["Cross"] = df["Signal"].diff()
    return df

# グラフ描画
def plot_stock_chart(df, company_name, start, end):
    # グラフ設定
    fig, (ax1, ax3) = plt.subplots(
        2, 1, figsize=(12, 8),
        sharex=True,
        gridspec_kw={'height_ratios': [3, 1]}
    )

    # 株価
    ax1.plot(df.index, df["Close"], label="株価", linewidth=2)
    ax1.plot(df.index, df["MA5"], label="5日平均", linestyle="--")
    ax1.plot(df.index, df["MA25"], label="25日平均", linestyle="--")

    # ゴールデンクロス（買いシグナル）
    buy = df[df["Cross"] == 1]
    ax1.scatter(buy.index, buy["Close"], marker="^", s=100, color="red", label="Buy Signal")

    # デッドクロス（売りシグナル）
    sell = df[df["Cross"] == -1]
    ax1.scatter(sell.index, sell["Close"], marker="v", s=100, color="blue", label="Sell Signal")

    ax1.set_xlabel("日付")
    ax1.set_ylabel("株価（円）")
    ax1.grid(True)

    # 出来高（別軸）
    ax2 = ax1.twinx()
    ax2.bar(df.index, df["Volume"].squeeze(), alpha=0.3)
    ax2.set_ylabel("出来高")

    # RSIグラフ
    ax3.plot(df.index, df["RSI"], label="RSI", linestyle="-")
    ax3.axhline(70, linestyle="--")  # 買われすぎ
    ax3.axhline(30, linestyle="--")  # 売られすぎ

    ax3.set_ylabel("RSI")
    ax3.set_xlabel("日付")
    ax3.grid(True)
    ax3.legend(loc="upper left")

    # タイトル
    ax1.set_title(f"{company_name} の株価推移（{start}〜{end}）")

    # 凡例
    ax1.legend(loc="upper left")

    plt.tight_layout()
    plt.show()

def main():
    set_font()
    code, start, end = get_user_input()
    df = get_stock_data(code, start, end)
    company_name = get_company_name(code)
    df = calculate_moving_averages(df)
    df = clculate_rsi(df)
    df = generate_cross_signals(df)
    plot_stock_chart(df, company_name, start, end)

if __name__ == "__main__":
    main()