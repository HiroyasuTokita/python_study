# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

test_integer = 100
print(test_integer + 10)
print(test_integer - 10)
print(test_integer * 10)
print(int(test_integer / 10))

test_str = '100'
print(int(test_str) + 100)

test_str = '100.5'
print(float(test_str) + 100)

test_str = '.5'
print((test_str))
print(float(test_str))

test_complex = 100 + 5j

print(test_complex)
print(test_complex.real)
print(test_complex.imag)
