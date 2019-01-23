def isDivisible(number):
	for i in range(1,21):
		if(number%i != 0): return 0
	return 1

for i in range(20, 999999999, 20):
	if(isDivisible(i)): print(i)

