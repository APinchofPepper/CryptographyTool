from fastapi import APIRouter
from app.utils.caesar_cipher import caesar_encrypt, caesar_decrypt

router = APIRouter()

@router.post("/encrypt")
def encrypt_caesar(text: str, shift: int):
    """
    Encrypt text using Caesar Cipher.
    """
    return {"encrypted_text": caesar_encrypt(text, shift)}

@router.post("/decrypt")
def decrypt_caesar(text: str, shift: int):
    """
    Decrypt text using Caesar Cipher.
    """
    return {"decrypted_text": caesar_decrypt(text, shift)}
