
import auxiliar
from auxiliar import choose_coprime, generate_prime

import math

def generate_e(p: int, q: int) -> int:
    n: int = p*q;

    fi: int = (p-1)*(q-1)

    e: int = choose_coprime(fi)  

    return e


def inverse_of_modulo(a: int, b: int ) -> int:
    x1: int; x2: int; x3: int;
    y1: int; y2: int; y3: int;
    q:int  

    if (b == 0):
        return 1

    x1, x2, x3 = 0, 1, b
    y1, y2, y3 = 1, 0, a
    while x3 != 0:
     q = y3 // x3
     x1, x2, x3, y1, y2, y3 = (y1 - q * x1), (y2 - q * x2), (y3 - q * x3), x1, x2, x3
    return y1 % b

def choose_d(p:int, q:int, e:int) -> int:

    fi: int = (p-1)*(q-1)
    n: int = p*q

    d: int = 1
    finded_d: bool = False

    """
    while not finded_d:
        if (d*e % fi == 1):
            finded_d = True 
        else:
            d+= 1
        #print(f"d: {d}")
    """

    d = inverse_of_modulo(e, fi)

    print(f"new value of d: {d}")

    return d


def rsa_encode(message: str, n: int, e: int) -> list[bytes]:
    values_list_message: list[int] = []
    values_list_encrypted: list[int] = []

    for char in message:
        value:int = ord(char)
        values_list_message.append(value)


    for char_code in values_list_message:
        char_encrypted:int = pow(char_code, e, n) # same as (message_int**e) % n 
        values_list_encrypted.append(char_encrypted)

    encrypted_message: list[bytes] = []

    for char_code in values_list_encrypted:
        encrypted_message.append( char_code.to_bytes(128,"big") )

    return encrypted_message


def rsa_decode(encrypted_message: list[bytes], n: int, d: int) -> str:
    values_list_encrypted: list[int] = []
    values_list_decrypted: list[int] = []


    for value_byte in encrypted_message:
        value:int = int.from_bytes(value_byte, "big")
        values_list_encrypted.append(value)

    for char_code in values_list_encrypted:
        char_decrypted:int = pow(char_code, d, n) # same as (message_int**d) % n; 
        values_list_decrypted.append(char_decrypted)

    decrypted_message: str = ""

    for char_code in values_list_decrypted:
        decrypted_message += chr(char_code)

    return str(decrypted_message) 


def generate_keys() -> tuple[dict[str,int], dict[str,int]]:
    private_key: dict[str,int] = dict()
    public_key: dict[str,int]  = dict()

    p: int = generate_prime(2**50)
    q: int = generate_prime(2**50)

    print(f"(generated p,q = {p,q})")

    n: int = p*q

    e:int  = generate_e(p, q)
    d: int = choose_d(p, q, e)

    print(f"e choosed: {e}")
    print(f"d finded: {d}")

    public_key["n"] = n  
    public_key["e"] = e  
    private_key["n"] = n 
    private_key["d"] = d

    return (public_key, private_key)