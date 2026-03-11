from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Load private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Generate shared key using ECDH
shared_key = private_key.exchange(ec.ECDH(), public_key)

# Derive a usable key from shared key
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data'
).derive(shared_key)

# Load AES key
with open("aes_key.bin", "rb") as f:
    aes_key = f.read()

# Simple protection: XOR AES key with derived key
encrypted_key = bytes(a ^ b for a, b in zip(aes_key, derived_key))

# Save encrypted AES key
with open("encrypted_aes_key.bin", "wb") as f:
    f.write(encrypted_key)

print("AES key secured using ECC shared key.")