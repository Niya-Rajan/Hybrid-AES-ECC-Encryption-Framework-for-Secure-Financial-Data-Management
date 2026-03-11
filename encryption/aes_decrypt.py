from Crypto.Cipher import AES

# Load AES key
with open("recovered_aes_key.bin", "rb") as f:
    key = f.read()

# Read encrypted file
with open("test_files/encrypted.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

# Create cipher
cipher = AES.new(key, AES.MODE_EAX, nonce)

# Decrypt
data = cipher.decrypt_and_verify(ciphertext, tag)

# Save decrypted file
with open("test_files/decrypted.txt", "wb") as f:
    f.write(data)

print("File decrypted successfully.")