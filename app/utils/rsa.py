from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_rsa_key_pair():
    """
    Generate a new RSA key pair.
    
    Returns:
    - public_key (str): Base64 encoded public key
    - private_key (str): Base64 encoded private key
    """
    # Generate a 2048-bit RSA key pair
    key = RSA.generate(2048)
    
    # Export public key in PEM format and base64 encode
    public_key = base64.b64encode(key.publickey().export_key()).decode('utf-8')
    
    # Export private key in PEM format and base64 encode
    private_key = base64.b64encode(key.export_key()).decode('utf-8')
    
    return public_key, private_key

def rsa_encrypt(text: str, public_key: str) -> str:
    """
    Encrypt text using RSA public key.
    
    Args:
    - text (str): Text to encrypt
    - public_key (str): Base64 encoded public key
    
    Returns:
    - str: Base64 encoded encrypted text
    """
    try:
        # Ensure public key is properly base64 padded
        padded_key = _pad_base64(public_key)
        
        # Decode base64 public key
        key_bytes = base64.b64decode(padded_key.encode('utf-8'))
        
        # Import the public key
        key = RSA.import_key(key_bytes)
        
        # Create cipher
        cipher = PKCS1_OAEP.new(key)
        
        # Encrypt the text
        encrypted_text = cipher.encrypt(text.encode('utf-8'))
        
        # Base64 encode the encrypted text
        return base64.b64encode(encrypted_text).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Encryption failed: {str(e)}")

def rsa_decrypt(ciphertext: str, private_key: str) -> str:
    """
    Decrypt text using RSA private key.
    
    Args:
    - ciphertext (str): Base64 encoded encrypted text
    - private_key (str): Base64 encoded private key
    
    Returns:
    - str: Decrypted text
    """
    try:
        # Ensure private key and ciphertext are properly base64 padded
        padded_key = _pad_base64(private_key)
        padded_ciphertext = _pad_base64(ciphertext)
        
        # Decode base64 private key
        key_bytes = base64.b64decode(padded_key.encode('utf-8'))
        
        # Import the private key
        key = RSA.import_key(key_bytes)
        
        # Create cipher
        cipher = PKCS1_OAEP.new(key)
        
        # Decode base64 ciphertext
        encrypted_text = base64.b64decode(padded_ciphertext.encode('utf-8'))
        
        # Decrypt the text
        decrypted_text = cipher.decrypt(encrypted_text)
        
        return decrypted_text.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")

def _pad_base64(s: str) -> str:
    """
    Pad base64 string to ensure it's a multiple of 4 characters long
    """
    missing_padding = len(s) % 4
    if missing_padding:
        s += '=' * (4 - missing_padding)
    return s

# Demonstration function
def demonstrate_rsa():
    """
    Demonstrate RSA key generation, encryption, and decryption.
    """
    # Generate key pair
    public_key, private_key = generate_rsa_key_pair()
    
    # Original text to encrypt
    original_text = "SECURE COMMUNICATION"
    
    # Encrypt
    encrypted = rsa_encrypt(original_text, public_key)
    print("Encrypted:", encrypted)
    
    # Decrypt
    decrypted = rsa_decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)
    
    # Verify
    assert decrypted == original_text, "Decryption failed"
    print("RSA encryption/decryption successful!")