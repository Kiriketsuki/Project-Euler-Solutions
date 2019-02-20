def multiples_of_3_and_5(n):
	"""
		n is upper limit of range
		Return the sum of numbers that are multiples of 3 and 5 below number n
	"""
	answer = 0
	for i in range(n):
		if i % 5 == 0:
			answer += i
		elif i % 3 == 0:
			answer += i
			
	return answer
		