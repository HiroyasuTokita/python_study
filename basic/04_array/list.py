import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

test_list_1 = ['python','-','izm','.','com'] # 連想配列は[]
print(test_list_1)

print('--------------------------------')

for i in test_list_1:
    print(i)

test_list_1 = []
print(test_list_1)

print('--------------------------------')

test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')

for i in test_list_1: # 普通に拡張ループされる。
    print(i)


test_list_1 = ['python', 'izm', 'com']
print(test_list_1)

print('--------------------------------')

test_list_1.insert(1, '-')
test_list_1.insert(3, '.')

print(test_list_1)

test_list_1.insert(0, 'http://www.')
print(test_list_1)
test_list_1.insert(0, 'http://www.') # 挿入され、番号は再度ずれる。
print(test_list_1)


print('--------------------------------')

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

test_list_1.remove('2')
print(test_list_1) # 最初に見つかったものが削除される。

print('--------------------------------')

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

print(test_list_1.pop(1))
print(test_list_1)

print(test_list_1.pop())
print(test_list_1)

print('--------------------------------')

test_list_1 = ['100', '200', '300', '200', '100','200','200']
print(test_list_1.index('300'))

print('--------------------------------')
print(test_list_1.count('200'))
