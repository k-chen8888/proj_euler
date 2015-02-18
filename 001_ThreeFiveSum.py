def three_five_sum(ceiling):
	sum = 0
	
	# Loop through the range
	for i in range(0, 1000):
		# Add if either a multiple of 3 or a multiple of 5
		sum = sum + i if i % 3 == 0 or i % 5 == 0 else sum
	
	return sum

if __name__ == '__main__':
	print three_five_sum(1000)
