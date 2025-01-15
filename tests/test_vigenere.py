import pytest
from app.utils.vigenere_cipher import vigenere_encrypt, vigenere_decrypt

def test_vigenere_encrypt():
    """
    Test encryption with the Vigenère cipher.
    """
    # Standard encryption
    assert vigenere_encrypt("HELLO", "KEY") == "RIJVS"
    assert vigenere_encrypt("hello", "key") == "rijvs"
    assert vigenere_encrypt("HELLO WORLD", "KEY") == "RIJVS UYVJN"

    # Case insensitivity in the keyword
    assert vigenere_encrypt("HELLO", "key") == "RIJVS"

    # Non-alphabetic characters should remain unchanged
    assert vigenere_encrypt("HELLO, WORLD!", "KEY") == "RIJVS, UYVJN!"

    # Empty string
    assert vigenere_encrypt("", "KEY") == ""

def test_vigenere_decrypt():
    """
    Test decryption with the Vigenère cipher.
    """
    # Standard decryption
    assert vigenere_decrypt("RIJVS", "KEY") == "HELLO"
    assert vigenere_decrypt("rijvs", "key") == "hello"
    assert vigenere_decrypt("RIJVS UYVJN", "KEY") == "HELLO WORLD"

    # Case insensitivity in the keyword
    assert vigenere_decrypt("RIJVS", "key") == "HELLO"

    # Non-alphabetic characters should remain unchanged
    assert vigenere_decrypt("RIJVS, UYVJN!", "KEY") == "HELLO, WORLD!"

    # Empty string
    assert vigenere_decrypt("", "KEY") == ""

def test_vigenere_edge_cases():
    """
    Test edge cases for the Vigenère cipher.
    """
    # Keyword is longer than the text
    assert vigenere_encrypt("HI", "LONGKEYWORD") == "SI"
    assert vigenere_decrypt("SI", "LONGKEYWORD") == "HI"

    # Keyword is empty (should raise an error)
    with pytest.raises(IndexError):
        vigenere_encrypt("HELLO", "")
    with pytest.raises(IndexError):
        vigenere_decrypt("RIJVS", "")
