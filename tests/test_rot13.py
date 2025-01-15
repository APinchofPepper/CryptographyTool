import pytest
from app.utils.rot13 import rot13_encrypt

def test_rot13_encrypt_decrypt():
    text = "HELLO ROT13"
    encrypted_text = rot13_encrypt(text)
    decrypted_text = rot13_encrypt(encrypted_text)  # ROT13 is symmetric
    assert decrypted_text == text

def test_rot13_non_alpha():
    text = "12345"
    encrypted_text = rot13_encrypt(text)
    assert encrypted_text == text  # Non-alphabet characters remain unchanged
