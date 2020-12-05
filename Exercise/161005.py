import pandas as pd
import datetime as dt
import numpy as np

def input_path():
    while True:
        try:
            csv_path = input('The path of the historical data is:\n')
            data = pd.read_csv(csv_path)
            break
        except:
            print('Invalid path, try again')
    print('Valid path, the head of file is shown as below')
    return data

def check_series():
    error = 0
    if '日期' in data:
        error += 1
    else:
        while True:
            date_series = input('The date series is named:\n')
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
            price_series = input('The price series is named:\n')
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
            open_series = input('The open series is named:\n')
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
            high_series = input('The high series is named:\n')
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
            low_series = input('The low series is named:\n')
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
            change_series = input('The change series is named:\n')
            if change_series in data:
                data.rename(columns={change_series:'涨跌幅'},inplace=True)
                print("Match successfully, renamed to '涨跌幅'")
                break
            else:
                print('Match failed, re-enter')
    if error != 6:
        print(data)

def add_series():
    if '星期' in data:
        del data['星期']
    if '日' in data:
        del data['日']
    wd_list = []
    day_list = []
    for each in range(len(data['日期'])):
        test = data['日期'][each].replace('年','').replace('月','').replace('日','')
        item = dt.datetime.strptime(test, "%Y%m%d").weekday() + 1
        wd_list.append(item)
        day_list.append(dt.datetime.strptime(test, "%Y%m%d").day)
    data.insert(0,'星期',wd_list)
    data.insert(1,'日',day_list)
    if '估计' in data:
        del data['估计']
    es_list = []
    for each in range(len(data['日期'])):
        es_value=(data['收盘'][each]+data['开盘'][each]+data['高'][each]+data['低'][each])/4
        es_list.append(es_value)
    data.insert(2,'估计',es_list)

def check_date_item():
    for each in data['日期']:
        each = str(each)
        if len(each) < 9 or len(each) > 11:
            return False
        elif each.count('年') != 1 or each.count('月') != 1 or each.count('日') != 1:
            return False
    return True

def check_pohl():
    for each in range(len(data['日期'])):
        if not str(data['收盘'][each]).replace('.','').isdigit() or not str(data['开盘'][each]).replace('.','').isdigit() or not str(data['高'][each]).replace('.','').isdigit() or not str(data['低'][each]).replace('.','').isdigit():
            return False
    return True

while True:
    try:
        data = input_path()
        print(data)
        check_series()
        check_date_item()
        check_pohl()
        add_series()
        print(data)
        break
    except:
        print('The preparation failed, try again\n')

print('\nThe preparation work is completed and ready to calculate.\n')

def es_range():
    while True:
        try:
            es = int(input('How many trading days(1~' + str(len(data['日期'])) +') need to be calculated until now?\n'))
            if es > len(data['日期']):
                print('Out of range, re-enter\n')
                continue
            print('\nThe time is set to the previous '+str(es)+' trading days in dataset\n')
            return es
        except:
            print('Invalid input, re-enter\n')

## Invest once a week
def week1():
    week1 = [[],[],[],[],[]] ## [mon,tue,wed,thur,fri]
    for each in range(rng):
        if   data['星期'][each] == 1:
            week1[0].append(data['估计'][each])
        elif data['星期'][each] == 2:
            week1[1].append(data['估计'][each])
        elif data['星期'][each] == 3:
            week1[2].append(data['估计'][each])
        elif data['星期'][each] == 4:
            week1[3].append(data['估计'][each])
        elif data['星期'][each] == 5:
            week1[4].append(data['估计'][each])
    print('Invest once a week')
    print('\tMonday    average price:   ' + str(np.mean(week1[0])))
    print('\tTuesday   average price:   ' + str(np.mean(week1[1])))
    print('\tWednesday average price:   ' + str(np.mean(week1[2])))
    print('\tThursday  average price:   ' + str(np.mean(week1[3])))
    print('\tFriday    average price:   ' + str(np.mean(week1[4])))

## Invest every two weeks
def week2():
    week2 = [[],[],[],[],[],[0,0,0,0,0]] ## [mon,tue,wed,thur,fri,MARK] 
    for each in range(rng):
        if   data['星期'][each] == 1 and week2[-1][0]%2 == 0:
            week2[0].append(data['估计'][each])
            week2[-1][0] += 1
        elif data['星期'][each] == 2 and week2[-1][1]%2 == 0:
            week2[1].append(data['估计'][each])
            week2[-1][1] += 1
        elif data['星期'][each] == 3 and week2[-1][2]%2 == 0:
            week2[2].append(data['收盘'][each])
            week2[-1][2] += 1
        elif data['星期'][each] == 4 and week2[-1][3]%2 == 0:
            week2[3].append(data['估计'][each])
            week2[-1][3] += 1
        elif data['星期'][each] == 5 and week2[-1][4]%2 == 0:
            week2[4].append(data['估计'][each])
            week2[-1][4] += 1
    print('Invest every two weeks')
    print('\tMonday    average price:   ' + str(np.mean(week2[0])))
    print('\tTuesday   average price:   ' + str(np.mean(week2[1])))
    print('\tWednesday average price:   ' + str(np.mean(week2[2])))
    print('\tThursday  average price:   ' + str(np.mean(week2[3])))
    print('\tFriday    average price:   ' + str(np.mean(week2[4])))

## Invest once a month
def month1():
    month1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for each in range(rng):
        if   data['日'][each] == 1:
            month1[0].append(data['估计'][each])
        elif data['日'][each] == 2:
            month1[1].append(data['估计'][each])
        elif data['日'][each] == 3:
            month1[2].append(data['估计'][each])
        elif data['日'][each] == 4:
            month1[3].append(data['估计'][each])
        elif data['日'][each] == 5:
            month1[4].append(data['估计'][each])
        elif data['日'][each] == 6:
            month1[5].append(data['估计'][each])
        elif data['日'][each] == 7:
            month1[6].append(data['估计'][each])
        elif data['日'][each] == 8:
            month1[7].append(data['估计'][each])
        elif data['日'][each] == 9:
            month1[8].append(data['估计'][each])
        elif data['日'][each] == 10:
            month1[9].append(data['估计'][each])
        elif data['日'][each] == 11:
            month1[10].append(data['估计'][each])
        elif data['日'][each] == 12:
            month1[11].append(data['估计'][each])
        elif data['日'][each] == 13:
            month1[12].append(data['估计'][each])
        elif data['日'][each] == 14:
            month1[13].append(data['估计'][each])
        elif data['日'][each] == 15:
            month1[14].append(data['估计'][each])
        elif data['日'][each] == 16:
            month1[15].append(data['估计'][each])
        elif data['日'][each] == 17:
            month1[16].append(data['估计'][each])
        elif data['日'][each] == 18:
            month1[17].append(data['估计'][each])
        elif data['日'][each] == 19:
            month1[18].append(data['估计'][each])
        elif data['日'][each] == 20:
            month1[19].append(data['估计'][each])
        elif data['日'][each] == 21:
            month1[20].append(data['估计'][each])
        elif data['日'][each] == 22:
            month1[21].append(data['估计'][each])
        elif data['日'][each] == 23:
            month1[22].append(data['估计'][each])
        elif data['日'][each] == 24:
            month1[23].append(data['估计'][each])
        elif data['日'][each] == 25:
            month1[24].append(data['估计'][each])
        elif data['日'][each] == 26:
            month1[25].append(data['估计'][each])
        elif data['日'][each] == 27:
            month1[26].append(data['估计'][each])
        elif data['日'][each] == 28:
            month1[27].append(data['估计'][each])
    print('Invest once a month')
    print('\t1st  average price:   ' + str(np.mean(month1[0])))
    print('\t2nd  average price:   ' + str(np.mean(month1[1])))
    print('\t3rd  average price:   ' + str(np.mean(month1[2])))
    print('\t4th  average price:   ' + str(np.mean(month1[3])))
    print('\t5th  average price:   ' + str(np.mean(month1[4])))
    print('\t6th  average price:   ' + str(np.mean(month1[5])))
    print('\t7th  average price:   ' + str(np.mean(month1[6])))
    print('\t8th  average price:   ' + str(np.mean(month1[7])))
    print('\t9th  average price:   ' + str(np.mean(month1[8])))
    print('\t10th average price:   ' + str(np.mean(month1[9])))
    print('\t11st average price:   ' + str(np.mean(month1[10])))
    print('\t12nd average price:   ' + str(np.mean(month1[11])))
    print('\t13rd average price:   ' + str(np.mean(month1[12])))
    print('\t14th average price:   ' + str(np.mean(month1[13])))
    print('\t15th average price:   ' + str(np.mean(month1[14])))
    print('\t16th average price:   ' + str(np.mean(month1[15])))
    print('\t17th average price:   ' + str(np.mean(month1[16])))
    print('\t18th average price:   ' + str(np.mean(month1[17])))
    print('\t19th average price:   ' + str(np.mean(month1[18])))
    print('\t20th average price:   ' + str(np.mean(month1[19])))
    print('\t21st average price:   ' + str(np.mean(month1[20])))
    print('\t22nd average price:   ' + str(np.mean(month1[21])))
    print('\t23rd average price:   ' + str(np.mean(month1[22])))
    print('\t24th average price:   ' + str(np.mean(month1[23])))
    print('\t25th average price:   ' + str(np.mean(month1[24])))
    print('\t26th average price:   ' + str(np.mean(month1[25])))
    print('\t27th average price:   ' + str(np.mean(month1[26])))
    print('\t28th average price:   ' + str(np.mean(month1[27])))

## Invest once a day
def day1():
    day1 = []
    for each in range(rng):
        day1.append(data['估计'][each])
    print('Invest once a day')
    print('\tDaily average price:   ' + str(np.mean(day1)))

while True:
    rng = es_range()
    while True:
        choice = input('\n0: Reselect time span\n1: Invest once a week\n2: Invest every two weeks\n3: Invest once a month\n4: Invest once a day\nSelect one of the above functions to input the corresponding number (0~4), and click Enter:')
        print()
        if choice == '0':
            break
        elif choice == '1':
            week1()
            continue
        elif choice == '2':
            week2()
            continue
        elif choice == '3':
            month1()
            continue
        elif choice == '4':
            day1()
            continue
        else:
            print('\nInput error, please select again\n')