from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Generate AES key
key = get_random_bytes(32)  # 256-bit key

# Save the key for later use
with open("aes_key.bin", "wb") as f:
    f.write(key)

print("AES key generated and saved.")

# Read the file
with open("test_files/test.txt", "rb") as f:
    data = f.read()

# Create AES cipher
cipher = AES.new(key, AES.MODE_EAX)

ciphertext, tag = cipher.encrypt_and_digest(data)

# Save encrypted file
with open("test_files/encrypted.bin", "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(ciphertext)

print("File encrypted successfully.")