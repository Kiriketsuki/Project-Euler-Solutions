def is_palindrome_int(n):
	"""
		takes in an integer n
		returns True if palindrome, False if not
	"""
	
	str_n = str(n)
	length_str = len(str_n)
	if length_str == 1:
		return True
	elif length_str == 2:
		if str_n[0] == str_n[1]:
			return True
		else:
			return False
	elif length_str % 2 == 0:
		if str_n[:(length_str//2)] == str_n[(length_str//2):][::-1]:
			return True
		else:
			return False
	else:
		if str_n[:(length_str//2)] == str_n[(length_str//2)+1:][::-1]:
			return True
		else:
			return False
			
list_of_products =[]
for i in range(100,1000):
	for j in range(100,1000):
		if is_palindrome_int(i*j):
			list_of_products.append(i*j)

print(max(list_of_products))

