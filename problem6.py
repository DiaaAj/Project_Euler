def SquareSum(number):
	square, sum = 0, 0
	for i in range(number+1):
		square+=i**2
		sum+=i
	return sum**2-square

print(SquareSum(100))
