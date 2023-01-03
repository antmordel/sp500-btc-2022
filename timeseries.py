import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


def main():
    # "^GSPC" is the ticker for the S&P 500 index
    sp500_df = yf.download(tickers="^GSPC", start="2022-01-01", end="2023-01-01", interval="1d")

    # Normalize the data
    spread = sp500_df["Close"].max() - sp500_df["Close"].min()
    sp500_df["Normalized"] = (sp500_df["Close"] - sp500_df["Close"].min()) / spread

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ln1 = sp500_df.plot(ax=ax1, use_index=True, y="Close", kind="line", color="blue",
                        title="S&P 500 Index VS Bitcoin", legend=False, label="S&P 500 Index")

    # BTC prices
    btc_df = pd.read_json('./btc_value.json')
    btc_df.rename(columns={0: 'Date', 1: 'Price'}, inplace=True)
    btc_df.set_index("Date")
    btc_df["Date"] = pd.to_datetime(btc_df["Date"], unit="ms")
    btc_df = btc_df[btc_df['Date'].dt.year == 2022]

    # Normalize the data
    spread_btc = btc_df["Price"].max() - btc_df["Price"].min()
    btc_df["Normalized"] = (btc_df["Price"] - btc_df["Price"].min()) / spread_btc
    ln2 = btc_df.plot(ax=ax2, x="Date", y="Price", kind="line",
                      color="green", legend=False, label="BTC Price")

    ln1.set_ylabel("S&P 500 Index")
    ln2.set_ylabel("BTC Price")
    plt.show()


if __name__ == "__main__":
    main()
