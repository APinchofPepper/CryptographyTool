from fastapi import APIRouter
from app.utils.rot13 import rot13_encrypt

router = APIRouter()

@router.post("/encrypt")
def encrypt_rot13(text: str):
    """
    Encrypt text using ROT13 (symmetric cipher).
    """
    return {"encrypted_text": rot13_encrypt(text)}

@router.post("/decrypt")
def decrypt_rot13(text: str):
    """
    Decrypt text using ROT13 (symmetric cipher, same as encryption).
    """
    return {"decrypted_text": rot13_encrypt(text)}
