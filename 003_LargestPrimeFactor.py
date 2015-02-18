import math

def find_prime(target):
	# Only check up to the square root
	ceiling = int(math.ceil(math.sqrt(target)))

	# Make a sieve that assumes all numbers to be checked are initially prime
	sieve = ['p'] * (ceiling + 1)

	for i in range(2, ceiling + 1):
	 	# Check if target is divisible
		if target % i == 0:
			# Recurse, using the result as the new target
			return find_prime(target / i)
		
		# Target is not divisible, find next prime
		if sieve[i] == 'p':
			j = 0
		
			while 2 * j < ceiling + 1:
				sieve[2 * j] = 'c'
				j += 1
	
	# If the target is prime, then we are done
	return target

if __name__ == '__main__':
	print find_prime(600851475143)
