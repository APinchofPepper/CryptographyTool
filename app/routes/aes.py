from fastapi import APIRouter
from app.utils.aes import aes_encrypt, aes_decrypt
import urllib.parse

router = APIRouter()

@router.post("/encrypt")
def encrypt_aes(text: str, key: str):
    """
    Encrypt text using AES.
    """
    return {"encrypted_text": aes_encrypt(text, key)}

@router.post("/decrypt")
def decrypt_aes(text: str, key: str):
    """
    Decrypt text using AES.
    Handles URL-encoded ciphertexts.
    """
    # Decode URL-encoded ciphertext
    decoded_text = urllib.parse.unquote(text)
    return {"decrypted_text": aes_decrypt(decoded_text, key)}