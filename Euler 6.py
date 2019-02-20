def sum_of_squares(n):
	"""
		n is the last term
		returns the sum of squares from 1 to n
	"""
	sum = 0
	for i in range(0,n+1):
		sum += i**2
	
	return sum
	
def square_of_sums(n):
	sum = 0
	for i in range(0,n+1):
		sum += i
	return sum**2
	
