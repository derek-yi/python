# -*- coding: utf-8 -*-

# ����datetimeģ��
import datetime  

#��������ʱ��
today = datetime.date.today()

# ���������ʱ��  
yesterday = today - datetime.timedelta(days = 1)

# ���������ʱ�� 
tomorrow = today + datetime.timedelta(days = 1)  

# ��ӡ������ʱ��
print(yesterday, today, tomorrow)

