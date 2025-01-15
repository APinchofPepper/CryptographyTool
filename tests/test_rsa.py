import pytest
from app.utils.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt

def test_rsa_encrypt_decrypt():
    private_key, public_key = generate_rsa_keys()
    text = "HELLO RSA"
    encrypted_text = rsa_encrypt(text, public_key)
    decrypted_text = rsa_decrypt(encrypted_text, private_key)
    assert decrypted_text == text

def test_rsa_invalid_key():
    _, public_key = generate_rsa_keys()
    invalid_private_key = "invalid_key"
    text = "HELLO RSA"
    encrypted_text = rsa_encrypt(text, public_key)
    with pytest.raises(ValueError):
        rsa_decrypt(encrypted_text, invalid_private_key)
