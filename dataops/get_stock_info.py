import pandas as pd
import baostock as bs




def get_stock_list(exchange = "SH", data_file = "./data/stock_list/SH_stock.csv"):
    if exchange == "SH":
        name = "证券代码"
    elif exchange == "SZ":
        name = "A股代码"
    data = pd.read_csv(data_file, dtype={name: str})
    stock_list = data[name].tolist()
    return stock_list
    
def get_stock_info(exchange = "SH", data_file = "./data/stock_list/SH_stock.csv"):
    if exchange == "SH":
        name = "证券代码"
    elif exchange == "SZ":
        name = "A股代码"
    data = pd.read_csv(data_file, dtype={name: str})
    if exchange == "SZ":
        print(data)
        # stock_list = data["A股代码"].tolist()
        print(data['A股简称'].dtype)
        print(data['A股代码'].dtype)
    return data


def get_stock_data_from_baostock(code="sh.600000", start_date="2024-07-01", end_date="2024-12-31", frequency="d", adjustflag="3", login = True):
    if not login:
        lg = bs.login()
        assert lg.error_code == "0"
        assert lg.error_msg == "success"
    # 获取dataframe格式的股票数据
    rs = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        start_date=start_date, end_date=end_date, frequency=frequency, adjustflag=adjustflag)
    assert rs.error_code == "0"
    assert rs.error_msg == "success"

    data_list = []
    while (rs.error_code == "0") & rs.next():
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    return result



def download_stock_data(code_list=[], save_place = "./data/stock_data/{}.csv",start_date="2024-07-01", end_date="2024-12-31", frequency="d", adjustflag="3"):
    lg = bs.login()
    assert lg.error_code == "0"
    assert lg.error_msg == "success"
    for i, code in enumerate(code_list):
        data_df = get_stock_data_from_baostock(code=code, start_date=start_date, end_date=end_date, frequency=frequency, adjustflag=adjustflag)
        data_df.to_csv(save_place.format(code), index=False)
        print(f"下载完成：{code}.csv, 进度：{i}/{len(code_list)}")


