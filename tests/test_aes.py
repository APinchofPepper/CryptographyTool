import pytest
from app.utils.aes import aes_encrypt, aes_decrypt

def test_aes_encrypt_decrypt():
    key = "securekey12345678"  # Use exactly 16 characters
    text = "HELLO AES ENCRYPTION"
    encrypted_text = aes_encrypt(text, key)
    decrypted_text = aes_decrypt(encrypted_text, key)
    assert decrypted_text == text

def test_aes_invalid_key_length():
    key = "shortkey"
    text = "HELLO AES"
    with pytest.raises(ValueError):
        aes_encrypt(text, key)
