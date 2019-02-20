def smallest_multiple(n):
	"""
		n is the largest factor of said number
		returns the smallest number that can be divided by all the numbers from 1 to n
	"""
	found = False
	i = (n-1)*n
	while not found:
		counter = 0
		for j in range(1,n+1):
			if i%j == 0:
				counter += 1
		if counter >= n:
			found = True
		else:
			i +=1
	return i