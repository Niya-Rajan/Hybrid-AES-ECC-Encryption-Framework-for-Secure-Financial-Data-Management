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

# Generate shared key
shared_key = private_key.exchange(ec.ECDH(), public_key)

# Derive the same key
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data'
).derive(shared_key)

# Load encrypted AES key
with open("encrypted_aes_key.bin", "rb") as f:
    encrypted_key = f.read()

# Recover AES key using XOR
recovered_aes_key = bytes(a ^ b for a, b in zip(encrypted_key, derived_key))

# Save recovered AES key
with open("recovered_aes_key.bin", "wb") as f:
    f.write(recovered_aes_key)

print("AES key recovered successfully.")