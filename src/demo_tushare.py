import tushare as ts
ts.set_token('9edfe7066698c6393d462401672933adfcdc322e96d10bfa69f1089a')
print(ts.__version__)

pro = ts.pro_api()

# df = pro.query('trade_cal', exchange='', start_date='20220601', end_date='20220810', fields='exchange,cal_date,is_open, pretrade_date', isopen='0')

# print(df)

new_share = pro.new_share(start_date='20210101', end_date='20221231')
print(new_share)