def fib(n):
	
	result = []
	a,b = 0,1

	while a < n:
		#print(a)
		result.append(a)
		a,b = b, (a + b)

	return result


fibres = fib(10)
print fibres
