from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_data(data, key):
    iv = get_random_bytes(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = data + b"\0" * (AES.block_size - len(data) % AES.block_size)
    encrypted_data = iv + cipher.encrypt(padded_data)
    encrypted_base64 = base64.b64encode(encrypted_data).decode()
    return encrypted_base64

key = b"testtest"

phrase = input("Entrez la phrase à chiffrer : ")
encrypted_phrase = encrypt_data(phrase.encode(), key)
print("Phrase chiffrée :", encrypted_phrase)
