def rot13_encrypt(text: str) -> str:
    """
    Encrypt text using ROT13 (same function for decryption).
    """
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + 13) % 26 + shift_base)
        else:
            result += char
    return result
