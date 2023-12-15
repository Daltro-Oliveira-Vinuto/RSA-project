
import rsa 
from rsa import generate_keys, rsa_encode, rsa_decode

def main() -> None:
	A_public_key: dict[str,int]; A_private_key: dict[str,int];
	B_public_key: dict[str,int]; B_private_key: dict[str,int];

	A_public_key, A_private_key = generate_keys()
	B_public_key, B_private_key = generate_keys()

	print(f"A public key pair: {A_public_key}, private key pair: {A_private_key}")
	print(f"B public key pair: {B_public_key}, private key pair: {B_private_key}")

	message: str = input("Digite a mensagem a ser criptografada em RSA por A:")

	print(f"Message to be send from A to B: {message}")

	encrypted_message: list[bytes] = rsa_encode(message, A_public_key["n"], A_public_key["e"])

	print(f"encrypted message receive by B: {encrypted_message}")

	decrypted_message: str = rsa_decode(encrypted_message, A_public_key["n"], A_private_key["d"])

	print(f"decrypted message by B: {decrypted_message}")
	

if __name__ == "__main__":
	main()