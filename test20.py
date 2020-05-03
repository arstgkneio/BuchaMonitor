import pandas

df1 = pandas.read_csv("bucha_logs/bucha_log_20200428.csv")
df2 = pandas.read_csv("bucha_logs/bucha_log_20200429.csv")

df3 = df1.append(df2, ignore_index=True)
print(df1, df2, df3)
