#变量名设置
name_company="js"
stock_price=19.99
stock_code="003032"
stock_price_daily_grown=1.2
growth_day="7"
finally_7=19.99*1.2**7
finally_7_1="%.2f" % finally_7
#输出
print(finally_7_1)
#用f占位
print(f"公司名:{name_company},股票代码:{stock_code},当前股价:{stock_price}")
#用%s占位
print("股票每日增长系数%s,经过%s天后,股价为：%s" % (stock_price_daily_grown,growth_day,finally_7_1))








