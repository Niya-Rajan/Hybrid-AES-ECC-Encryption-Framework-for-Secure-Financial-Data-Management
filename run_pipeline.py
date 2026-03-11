import subprocess
import sys

python_exec = sys.executable

print("\n===== HYBRID AES + ECC PIPELINE STARTED =====\n")

print("Step 1: Generating ECC Keys...")
subprocess.run([python_exec, "encryption/ecc_keys.py"])

print("\nStep 2: Encrypting File with AES...")
subprocess.run([python_exec, "encryption/aes_encrypt.py"])

print("\nStep 3: Protecting AES Key using ECC...")
subprocess.run([python_exec, "encryption/ecc_encrypt_key.py"])

print("\nStep 4: Recovering AES Key using ECC...")
subprocess.run([python_exec, "encryption/ecc_decrypt_key.py"])

print("\nStep 5: Decrypting File with AES...")
subprocess.run([python_exec, "encryption/aes_decrypt.py"])

print("\n===== PIPELINE COMPLETED SUCCESSFULLY =====")