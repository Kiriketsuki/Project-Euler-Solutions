global dict_of_fib
dict_of_fib = {}

def fib_rec(n):
	if n == 1 :
		return 0
	elif n == 2:
		return 1
	elif n in dict_of_fib:
		return dict_of_fib[n]
	else:
		dict_of_fib[n] = (fib_rec(n-1) + fib_rec(n-2))
		return fib_rec(n-1) + fib_rec(n-2)
		
def fib_ite(n):
	a,b = 0,1
	for i in range(0,n):
		a,b = b, a+b
	return a
	
def first_n_fib_term(n):
	""" 
		n is the maximum value returned by Fibonacci series
		returns the term of the value before n in the series
	"""
	high = 50
	low = 0
	guess = (high+low)//2
	found = False
	
	while not found:
		counter = 0
		if abs(fib_ite(guess) - n) > (n*0.1) and fib_ite(guess) < n:
			low = guess
			guess = (high+low)//2
			counter += 1
		elif abs(fib_ite(guess) - n) > (n*0.1) and fib_ite(guess) >n:
			high = guess
			guess = (high+low)//2
			counter += 1
		elif counter == 1000:
			found = True
		else:
			found = True
	return guess
			
		
		
		
def sum_of_even_fib(n):
	sum = 0
	for i in range(n):
		if fib_ite(i) %2 == 0:
			sum += fib_ite(i)
	return sum