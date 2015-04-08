import sys, math

# Naive way to check if a number is a prime
def is_prime(n):
	return True if all( n % i != 0 for i in range( 2, int( math.sqrt(n) + 1 ) ) ) else False

# Generator that keeps making primes
def primes():
	yield 2
	curr_prime = 3
	
	while True:
		while not is_prime(curr_prime):
			curr_prime = curr_prime + 2
		
		yield curr_prime
		curr_prime = curr_prime + 2

# Find the kth prime by using the generator k times
def kth_prime(k):
	prime = primes()
	
	try:
		for i in range(1, k):
			prime.next()
	
	except StopIteration:
		pass
	
	return prime.next()

if __name__ == "__main__":
	print kth_prime( int(sys.argv[1]) )
