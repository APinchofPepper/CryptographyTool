from Crypto.Cipher import AES
import base64

def pad_key(key: str) -> bytes:
    """
    Pad or truncate the key to 16, 24, or 32 bytes.
    
    Args:
    - key (str): Input key
    
    Returns:
    - bytes: Padded key bytes
    """
    key_bytes = key.encode('utf-8')
    if len(key_bytes) < 16:
        key_bytes = key_bytes.ljust(16, b'\0')
    elif len(key_bytes) < 24:
        key_bytes = key_bytes.ljust(24, b'\0')
    elif len(key_bytes) < 32:
        key_bytes = key_bytes.ljust(32, b'\0')
    else:
        key_bytes = key_bytes[:32]
    
    return key_bytes

def aes_encrypt(text: str, key: str) -> str:
    """
    Encrypt text using AES.
    
    Args:
    - text (str): Text to encrypt
    - key (str): Encryption key
    
    Returns:
    - str: Base64 encoded encrypted text
    """
    # Prepare key
    key_bytes = pad_key(key)
    
    # Create cipher
    cipher = AES.new(key_bytes, AES.MODE_EAX)
    nonce = cipher.nonce
    
    # Encrypt
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    
    # Combine nonce, ciphertext, and tag, then base64 encode
    return base64.b64encode(nonce + ciphertext + tag).decode('utf-8')

def aes_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt text using AES.
    
    Args:
    - ciphertext (str): Base64 encoded encrypted text
    - key (str): Decryption key
    
    Returns:
    - str: Decrypted text
    """
    try:
        # Prepare key
        key_bytes = pad_key(key)
        
        # Decode base64 ciphertext
        decoded_data = base64.b64decode(ciphertext)
        
        # Extract nonce, ciphertext, and tag
        nonce = decoded_data[:16]
        encrypted_data = decoded_data[16:-16]
        tag = decoded_data[-16:]
        
        # Create cipher and decrypt
        cipher = AES.new(key_bytes, AES.MODE_EAX, nonce=nonce)
        decrypted_text = cipher.decrypt_and_verify(encrypted_data, tag)
        
        return decrypted_text.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")