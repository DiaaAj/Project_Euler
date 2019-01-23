import logging
import timeit
logging.basicConfig(level = logging.DEBUG)

def isPlaindrome(x):
	return str(x) == str(x)[::-1]

plaindromes = []
for i in range(100,1000):
	for j in range(100,1000):
		if(isPlaindrome(i*j)): plaindromes.append(i*j)

print(max(plaindromes))
