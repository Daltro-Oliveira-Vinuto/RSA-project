import auxiliar
from auxiliar import *

number: int = 25
is_prime: bool = test_primality_fast(number)

print(f"result for {number} is {is_prime}")