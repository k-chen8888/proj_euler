def fibonacci_even_sum(fprev, fcurr, ceiling, curr_sum):
	# Continue recursion if below ceiling; otherwise, output sum
	# Inside recursion, pass along current sum if not even, otherwise add
	return fibonacci_even_sum(fcurr, fprev + fcurr, ceiling, curr_sum + fcurr if fcurr % 2 == 0 else curr_sum) if fcurr < ceiling else curr_sum

if __name__ == '__main__':
	print fibonacci_even_sum(1, 2, 4000000, 0)
