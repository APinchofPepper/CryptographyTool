def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using the Caesar cipher.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypt text using the Caesar cipher.
    """
    return caesar_encrypt(text, -shift)
