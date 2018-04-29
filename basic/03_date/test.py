# -*- coding: utf-8 -*-
import sys
import io
import datetime
import calendar

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

today = datetime.date.today()
todaydetail = datetime.datetime.today()

print('----------------------------------')
print(today)
print(todaydetail) #特に指定しなくても日付時刻形式で出る。
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond) #ミリ秒の変数は持たない様子。datetime

print('----------------------------------')

print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))
print(calendar.isleap(2018))
print(calendar.isleap(2019))
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2020))
