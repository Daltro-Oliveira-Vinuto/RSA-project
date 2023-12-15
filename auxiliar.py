import random
import math

def test_primality_slow(number:int) -> bool:
	is_prime: bool = True

	i: int = 2  
	while is_prime and i < number:
		if (number%i == 0 and number != 0):
			is_prime = False

		i+=1

	return is_prime

def test_primality_fast(number: int) -> bool:
	is_prime: bool = True

	if (number % 2 == 0):
		is_prime = False
		return is_prime
	else:
		if (number < 5):
			is_prime = False
			return is_prime

		n_1: int = number-1

		s:int 
		try_s: int = 1
		finded_s: bool = False
		while not finded_s:

			if (n_1 % (2**try_s) != 0):
				finded_s = True 
			else:
				s = try_s
				m: int  = n_1 / (2**try_s)
				try_s+= 1

		d:int = int(m) 
		a: int = (random.randrange(2, number-2))

		#print(f"values of a: {a}, s: {s}, d: {d}")

		finded_primality: bool = False	

		x: int = pow(a, d, number) # same as a**d % number
		y: int = 0	
		i: int = 0
		while not finded_primality and i < s:
			#print(f"y: {y}")

			y = pow(x, int(2), number) # same as (x**2) % number

			if (y == 1 and x != 1 and x != number-1):
				finded_primality = True
				is_prime = False
				return is_prime
			else:
				x = y
			i+= 1

		if (y != 1):
			is_prime = False
			return is_prime

	is_prime = True
	return is_prime

def generate_prime(upper_bound) -> int:
	prime_number:int 

	is_prime: bool = False
	while not is_prime:
		random_n = int(random.random()*upper_bound)

		if test_primality_fast(random_n):
			prime_number = random_n
			is_prime = True


	return prime_number

def choose_coprime(fi: int) -> int:
	e:int  
	finded_coprime: bool = False 

	list_primes: list[int] = [65537, 257, 17, 5]

	for value in list_primes:
		if (math.gcd(fi, value) == 1):
			finded_coprime = True
			e = value

	i: int = 5
	while not finded_coprime:
		if (math.gcd(fi, i) == 1):
			finded_coprime = True  
			e = i  
		i+= 2
		print(f"i: {i}")

	print(f"new value of e: {e}")
	return e



