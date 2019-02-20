def largest_prime_factors(n):
	""" 
		n is the product
		returns largest prime factor
	"""
	list_of_factors = []
	list_of_prime_factors = []
	for i in range(1,n):
		if n % i == 0:
			list_of_factors.append(i)
	
	for i in list_of_factors:
		j = 1
		counter = 0
		while j <= i:
			if i%j == 0:
				counter += 1
				if counter > 2:
					break
			j += 1
		if counter == 2:
			list_of_prime_factors.append(i)
	return max(list_of_prime_factors)