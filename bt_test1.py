import pandas as pd
from datetime import datetime
import backtrader as bt
import matplotlib.pyplot as plt
from dataops import *

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#数据加载
start_date = "2020-01-01"
end_date = "2023-01-01"
def getdata(code = "sh.600519", start_date = start_date, end_date = end_date):
    df = get_stock_data_from_baostock(code = code, start_date = start_date, end_date = end_date, login=False)
    print(df)
    print(df["date"].dtype)
    df["date"] = pd.to_datetime(df["date"])
    print(df["date"].dtype)
    df.index = pd.to_datetime(df["date"])
    print(df)
    print("11111111111")

getdata()