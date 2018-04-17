# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('モジュールのロード')

def test():
    print('関数：testを呼び出しました')

if __name__ == '__main__':

    print('python-izm')
#   print('パイソンイズム')
    test()
