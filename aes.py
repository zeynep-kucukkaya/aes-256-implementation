from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_data(data):
    key = get_random_bytes(32)  # 256-bit key
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return key, ciphertext, tag, cipher.nonce

if __name__ == "__main__":
    message = b"Hello, AES-256"
    key, ciphertext, tag, nonce = encrypt_data(message)

    print("Ciphertext:", ciphertext)
