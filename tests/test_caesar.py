import pytest
from app.utils.caesar_cipher import caesar_encrypt, caesar_decrypt

def test_caesar_encrypt():
    assert caesar_encrypt("HELLO", 3) == "KHOOR"
    assert caesar_encrypt("hello", 3) == "khoor"
    assert caesar_encrypt("123", 3) == "123"

def test_caesar_decrypt():
    assert caesar_decrypt("KHOOR", 3) == "HELLO"
    assert caesar_decrypt("khoor", 3) == "hello"
    assert caesar_decrypt("123", 3) == "123"
