# -*- coding: utf-8 -*-
import sys
import io
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 今日の日付をYYYYMMDD形式で返す。
def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day) # 配列の初期宣言設定

    return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
