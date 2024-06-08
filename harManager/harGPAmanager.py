import re
import pandas as pd
from json import loads, dumps


with open('GPA.har', 'r', encoding='utf-8') as f:
    har_data = f.read()

Collum_id = [
    'kch_id',#课程id
    'kcmc',#课程名称
    'kcxzmc',#课程性质名称
    'njmc',#年级名称
    'bfzcj',# 百分制成绩
    'jd',#绩点 GPA4.0
    'jgmc',#学院
    'kcbj',#主修
    'xf',#学分
    'xfjd',#学分绩点
    'xnmmc',#学年
    'tjrxm',#老师
    'kclbmc',#课程类别名称
]

# const
COL_NUM = 12

Patterns = [
    r'\\\"kch_id\\\":\\\"(.*?)\\\"',#课程id
    r'\\\"kcmc\\\":\\\"(.*?)\\\"',#课程名称
    r'\\\"kcxzmc\\\":\\\"(.*?)\\\"',#课程性质名称
    r'\\\"njmc\\\":\\\"(.*?)\\\"',#年级名称
    r'\\\"bfzcj\\\":\\\"(.*?)\\\",',  # 百分制成绩
    r'\\\"jd\\\":\\\"(.*?)\\\"',#绩点 GPA4.0
    r'\\\"jgmc\\\":\\\"(.*?)\\\"',#学院
    r'\\\"kcbj\\\":\\\"(.*?)\\\"',#主修
    r'\\\"xf\\\":\\\"(.*?)\\\"',#学分
    r'\\\"xfjd\\\":\\\"(.*?)\\\"',#学分绩点
    r'\\\"xnmmc\\\":\\\"(.*?)\\\"',#学年
    r'\\\"tjrxm\\\":\\\"(.*?)\\\"',#老师
    r'\\\"kclbmc\\\":\\\"(.*?)\\\"',#课程类别名称
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
print(NUM, end = ' c')
print('\n')

for j in range(NUM):
    df.append({}, ignore_index=True)


for i in range(COL_NUM):
    pattern = re.compile(Patterns[i])
    result = re.findall(pattern, (har_data))
    # print(result)
    # if len(result) != NUM:
    #     print("wtf\n")
    for j in range(NUM):
        # print(result[j])
        df.at[j,Collum_id[i]] = result[j]


# 如何获取课程类别名称？
pattern = re.compile(r'\\\"kch_id\\\":\\\"(.*?)kcmc')
result = re.findall(pattern, (har_data))
for j in range(NUM):
    match = re.findall(Patterns[12],result[j])
    if match : df.at[j, Collum_id[12]] = match[0]
    else: df.at[j, Collum_id[12]] = '无'
# print(result)

df_unique = df.drop_duplicates(subset='kcmc', keep='first')
print(df_unique)
# df = pd.DataFrame(result)
# print(df)

# for i in range(0,LEN):
#     for j in (0,3):
#         print(data[i][j] + ' ')
#     print('\n')

# print(len(result))

# with open('harmanager.txt', 'w', encoding='utf-8') as f:
#     for item in result:
#         f.write(item + '\n')
#
json_data = df.to_json(orient='records', force_ascii=False)

# 将 JSON 数据写入文件
with open('myGPA.json', 'w', encoding="utf8") as jsonfile:
    jsonfile.write(json_data)


