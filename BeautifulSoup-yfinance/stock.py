import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


apple = yf.Ticker("AAPL")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"

apple_info = pd.read_json(url)
file_path =  r"D:\data_project\apple.json"
apple_info = pd.read_json(file_path)


apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)

apple_share_price_data.plot(x="Date", y="Open", title="Apple Share Price Data")
# plt.xlabel("Date")
plt.ylabel("Opening Price ($)")
plt.show()

apple.dividends.plot(title="Apple Dividends")
plt.xlabel("Date")
plt.ylabel("Dividends ($)")
plt.show()