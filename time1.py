# -*- coding: utf-8 -*-

# ����datetimeģ��
import datetime  

#��������ʱ��
today = datetime.date.today()

# test
tomorrow = today + datetime.timedelta(days = 1)  

# test
yesterday = today - datetime.timedelta(days = 1)

# ��ӡ������ʱ��
print(yesterday, today, tomorrow)

