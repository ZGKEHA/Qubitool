import pandas as pd
import datetime as dt
import numpy as np
from pandas.core.base import DataError

def input_path():
    while True:
        try:
            csv_path = input('The path of the historical data is:\t')
            data = pd.read_csv(csv_path)
            break
        except:
            print('Invalid path, try again')
    print('Valid path, the head of file is shown as below')
    print(data + '\t')
    return data
data = input_path()

def check_series():
    error = 0
    if '日期' in data:
        error += 1
    else:
        while True:
            date_series = input('The date series is named:\t')
            if date_series in data:
                data.rename(columns={date_series:'日期'},inplace=True)
                print("Match successfully, renamed to '日期'")
                break
            else:
                print('Match failed, re-enter')
    if '收盘' in data:
        error += 1
    else:
        while True:
            price_series = input('The price series is named:\t')
            if price_series in data:
                data.rename(columns={price_series:'收盘'},inplace=True)
                print("Match successfully, renamed to '收盘'")
                break
            else:
                print('Match failed, re-enter')
    if '开盘' in data:
        error += 1
    else:
        while True:
            open_series = input('The open series is named:\t')
            if open_series in data:
                data.rename(columns={open_series:'开盘'},inplace=True)
                print("Match successfully, renamed to '开盘'")
                break
            else:
                print('Match failed, re-enter')
    if '高' in data:
        error += 1
    else:
        while True:
            high_series = input('The high series is named:\t')
            if high_series in data:
                data.rename(columns={high_series:'高'},inplace=True)
                print("Match successfully, renamed to '高'")
                break
            else:
                print('Match failed, re-enter')
    if '低' in data:
        error += 1
    else:
        while True:
            low_series = input('The low series is named:\t')
            if low_series in data:
                data.rename(columns={low_series:'低'},inplace=True)
                print("Match successfully, renamed to '低'")
                break
            else:
                print('Match failed, re-enter')
    if '涨跌幅' in data:
        error += 1
    else:
        while True:
            change_series = input('The change series is named:\t')
            if change_series in data:
                data.rename(columns={change_series:'涨跌幅'},inplace=True)
                print("Match successfully, renamed to '涨跌幅'")
                break
            else:
                print('Match failed, re-enter')
    if error != 0:
        print(data)
check_series()