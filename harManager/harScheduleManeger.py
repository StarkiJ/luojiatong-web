import re
import sys
import json
from datetime import datetime, timedelta

import pandas as pd

file_path = 'kebiao.har'

start_date_str = '2024-2-25'
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

Time_table_start = [
    'Placeholder',
    '8:00',
    '8:50',
    '9:50',
    '10:40',
    '11:30',
    '14:05',
    '14:55',
    '15:45',
    '16:40',
    '17:30',
    '18:30',
    '19:20',
    '20:10',
]

Time_table_end = [
    'Placeholder',
    '8:45',
    '9:35',
    '10:35',
    '11:25',
    '12:15',
    '14:50',
    '15:40',
    '16:30',
    '17:25',
    '18:15',
    '19:15',
    '20:05',
    '20:45'
]


def get_start_time(weeksno,daysno,beginclassno):
    time_ster = Time_table_start[beginclassno]
    if daysno == 7:
        daysno = 0
    hours, minutes = map(int, time_ster.split(':'))
    futuredate = start_date + timedelta(weeks=weeksno-1,days=daysno,hours=hours,minutes=minutes)

    return futuredate.strftime("%Y-%m-%d %H:%M:%S")

def get_end_time(weeksno,daysno,beginclassno):
    time_ster = Time_table_end[beginclassno]
    if daysno == 7:
        daysno = 0
    hours, minutes = map(int, time_ster.split(':'))
    futuredate = start_date + timedelta(weeks=weeksno-1,days=daysno,hours=hours,minutes=minutes)

    return futuredate.strftime("%Y-%m-%d %H:%M:%S")

# Del_NUM = 1
# Del_patterns = [
#     r'\\\"sjkList\\\":\[(.*?)\],\\\"xqjmcMap',#删除附加项目,such as keyanxunlian
#     r'\\\"jxbmc\\\":\\\"(.*?)\\\"'
# ]
#
# Del_list = []

with open(file_path , 'r', encoding='utf-8') as f:
    har_data_raw = f.read()

# for i in range(Del_NUM):
#     result = re.findall(Del_patterns[i], har_data_raw)
#     for ele in result:
#         Del_list.append(ele)



result = re.findall(r'\\\"kbList\\\":\[(.*?)\],\\\"xsbjList', har_data_raw)
har_data = result[0]


# print(har_data)
# sys.exit()
# const
COL_NUM = 9


# cdmc
# xkbz


Collum_id = [
    'jxbmc',#教学班名称
    'kcmc',#课程名称
    'zcd',#那些周
    'xqj',#星期几
    'jc',#哪几节
    'cdmc',#楼号其一
    'xkbz',#楼号其二
    'xm',#老师姓名
    'kcxszc',#课程形式组成
]

Patterns = [
    r'\\\"jxbmc\\\":\\\"(.*?)\\\"',
    r'\\\"kcmc\\\":\\\"(.*?)\\\"',
    r'\\\"zcd\\\":\\\"(.*?)\\\"',
    r'\\\"xqj\\\":\\\"(.*?)\\\"',
    r'\\\"jc\\\":\\\"(.*?)\\\"',
    r'\\\"cdmc\\\":\\\"(.*?)\\\"',
    r'\\\"xkbz\\\":\\\"(.*?)\\\"',
    r'\\\"xm\\\":\\\"(.*?)\\\"',
    r'\\\"kcxszc\\\":\\\"(.*?)\\\",',
]

# pattern = re.compile(Patterns[0])
#
# result = re.findall(pattern, (har_data))

df = pd.DataFrame(columns=Collum_id)

#测试有多少行数据
pattern = re.compile(Patterns[0])
result = re.findall(pattern, (har_data))
NUM = len(result)

print('raw data : ',end = '')
print(NUM, end = '')
print('\n')

for j in range(NUM):
    df.append({}, ignore_index=True)


for i in range(COL_NUM):
    pattern = re.compile(Patterns[i])
    result = re.findall(pattern, (har_data))
    # print(len(result))
    # if len(result) != NUM:
    #     print("wtf\n")
    for j in range(len(result)):
        df.at[j,Collum_id[i]] = result[j]

for j in range(NUM):
    for i in range(COL_NUM):
        print(df.iloc[j][Collum_id[i]], end=',')
    print('\n')


json_list = []

Day_patterns = [
    r'(\d+)-(\d+)周',  # 匹配范围，如 "6-9周"
    r'(\d+)周'  # 匹配单独的周，如 "12周"
]

for j in range(NUM):
    teacher_name = df.iloc[j]['xm']
    component = df.iloc[j]['kcxszc']


    week_set = set()

    ranges = re.findall(r'(\d+)-(\d+)', df.iloc[j]['zcd'])
    for start, end in ranges:
        week_set.update(range(int(start), int(end) + 1))

    singles = re.findall(r'(?<!-)(?<!\d)(\d+)(?!\d)(?!-)', df.iloc[j]['zcd'])
    for single in singles:
        week_set.add(int(single))

    int_week = sorted((week_set))

    int_day = int(df.iloc[j]['xqj'])
    matches = re.findall(r'(\d+)', df.iloc[j]['jc'])
    int_class = [int(num) for num in matches]

    if df.iloc[j]['xkbz'] != '无':
        place = df.iloc[j]['xkbz']
    else:
        place = df.iloc[j]['cdmc']

    len_week = len(int_week)

    for week in int_week:
            data_item = {'type': 1,'name': df.iloc[j]['kcmc'],'place': place, 'content' : f'{teacher_name},{component}',
                     'startTime': get_start_time(week,int_day,int_class[0]), 'endTime': get_end_time(week,int_day,int_class[1])}
            json_list.append(data_item)


with open('schedule.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_list, json_file,ensure_ascii=False, indent=4)
