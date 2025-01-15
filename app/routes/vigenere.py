from fastapi import APIRouter
from app.utils.vigenere_cipher import vigenere_encrypt, vigenere_decrypt

router = APIRouter()

@router.post("/encrypt")
def encrypt_vigenere(text: str, keyword: str):
    """
    Encrypt text using Vigenère Cipher.
    """
    return {"encrypted_text": vigenere_encrypt(text, keyword)}

@router.post("/decrypt")
def decrypt_vigenere(text: str, keyword: str):
    """
    Decrypt text using Vigenère Cipher.
    """
    return {"decrypted_text": vigenere_decrypt(text, keyword)}
