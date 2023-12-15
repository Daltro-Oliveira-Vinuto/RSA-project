
import rsa 
from rsa import *

from auxiliar import generate_prime


def main() -> None:

	p: int = generate_prime(2**50)
	q: int = generate_prime(2**50)

	print(f"(generated p,q = {p,q})")

	n: int = p*q

	e:int  = generate_e(p, q)
	d: int = choose_d(p, q, e)


	print(f"e choosed: {e}")
	print(f"d finded: {d}")

	message: str = input("Digite a mensagem a ser criptografada em RSA: ")

	print(f"Message to be send: {message}")

	encrypted_message: list[bytes] = rsa_encode(message, n, e)

	print(f"encrypted message: {encrypted_message}")

	decrypted_message: str = rsa_decode(encrypted_message, n, d)

	print(f"decrypted message: {decrypted_message}")
	

if __name__ == "__main__":
	main()