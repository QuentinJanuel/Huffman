from math import *

phi = (1+sqrt(5))/2

def fibo(n):
	return round((phi**(n))/sqrt(5))


def val1(n):
	sum1 = 0
	sum2 = 0
	for i in range(1, n):
		sum1 += fibo(i-1)
		sum2 += fibo(i-2)
	return sum1+sum2

def val2(n):
	sum = 1
	for i in range(1, n):
		sum += fibo(i-2)
	return ceil(log(n)/log(2))*sum

digits = 1000

for i in range(2, 100):
	a = val1(i)
	b = val2(i)
	# print(int(digits*a/b)/digits, a <= b)
	print(i, a, b, a <= b)



print (fibo(3))
