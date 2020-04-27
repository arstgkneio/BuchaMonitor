

import pandas as pd
from datetime import timedelta

df1=pd.read_csv('C:/Users/andre/OneDrive - Newcastle University/Computing/GitHub/BuchaMonitor/bucha_logs/bucha_log_20200426.csv')


#FINDING MAX AND MIN
# p=df1[' temperature'].max()
# q=df1[' temperature'].min()

# #FINDING TIMESTAMP OF MAX AND MIN
# min_ts = pd.timestamp.min()
# max_ts = pd.timestamp.max()

# print("the minimum happened at:", min_ts)
# print("the maximum happened at:", max_ts)


df2 = pd.read_csv('C:/Users/andre/OneDrive - Newcastle University/Computing/GitHub/BuchaMonitor/bucha_logs/bucha_log_20200427.csv')

# combine two csv files into one data frame
result = df1.append(df2)
#result = result.reset_index(drop=True)
#result = result.set_index('date_time')
arst = result['temperature'].max()

#pd.DataFrame.between_time

print("df1 = ", df1)
print("df2 = ", df2)
print("indexed dataframe = ", result)
print("max temperature = ", arst)


#print("the minimum temperature is:", q)
#print("the maximum temperature is:", p)

# FINDING MAX AND MIN WITHIN 24 HOUR RANGE

# def daymax(row):         
#     ser = result.temperature[(result.date_time <= row + timedelta(hours=24))]
#     return ser.max()

# result['maxTemp'] = result.date_time.apply(daymax)

# print(result)


# result = result.set_index('date_time'):

# >>> df2 = result.resample('1min').sort_index(ascending=False).fillna(np.nan)
# >>> df2 = df2.rolling(48,min_periods=1).max()
# >>> result.join(df2,rsuffix='2')

# print(result)

#                      Y   Y2
# timestamp                  
# 2016-03-29 12:00:00  1  3.0
# 2016-03-29 13:00:00  2  4.0
# 2016-03-30 11:00:00  3  4.0
# 2016-03-30 12:30:00  4  4.0
# 2016-03-30 13:30:00  3  3.0
# 2016-03-30 14:00:00  2  2.0

