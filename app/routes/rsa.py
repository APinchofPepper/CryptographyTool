from fastapi import APIRouter
from app.utils.rsa import generate_rsa_key_pair, rsa_encrypt, rsa_decrypt
import base64

router = APIRouter()

@router.get("/generate-keys")
def generate_keys():
    """
    Generate a new RSA key pair.
    """
    public_key, private_key = generate_rsa_key_pair()
    return {
        "public_key": public_key,
        "private_key": private_key
    }

@router.post("/encrypt")
def encrypt_rsa(text: str, public_key: str):
    """
    Encrypt text using RSA.
    """
    # Ensure the text is encrypted and base64 encoded
    encrypted = rsa_encrypt(text, public_key)
    return {"encrypted_text": encrypted}

@router.post("/decrypt")
def decrypt_rsa(text: str, private_key: str):
    """
    Decrypt text using RSA.
    Assume the input might not be base64 encoded yet.
    """
    try:
        # First, try to base64 encode the text if it isn't already
        try:
            # Check if it's already base64 encoded
            base64.b64decode(text)
            base64_text = text
        except:
            # If not, encode the text to base64
            base64_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        
        decrypted = rsa_decrypt(base64_text, private_key)
        return {"decrypted_text": decrypted}
    except Exception as e:
        return {"error": str(e)}