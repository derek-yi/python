# -*- coding: utf-8 -*-

# bbb
import datetime  

# aaa
today = datetime.date.today()


# test
yesterday = today - datetime.timedelta(days = 1)

# test
tomorrow = today + datetime.timedelta(days = 1)  


# 打印这三个时间
print(yesterday, today, tomorrow)

