from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import caesar, vigenere, aes, rsa, rot13

# Create FastAPI app
app = FastAPI(
    title="Cryptography Tool API",
    description="An API for encryption and decryption using various algorithms, including Caesar Cipher, Vigenère Cipher, AES, RSA, and ROT13.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for each encryption algorithm
app.include_router(caesar.router, prefix="/caesar", tags=["Caesar Cipher"])
app.include_router(vigenere.router, prefix="/vigenere", tags=["Vigenère Cipher"])
app.include_router(aes.router, prefix="/aes", tags=["AES"])
app.include_router(rsa.router, prefix="/rsa", tags=["RSA"])
app.include_router(rot13.router, prefix="/rot13", tags=["ROT13 Cipher"])

# Health check endpoint
@app.get("/", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok", "message": "Cryptography Tool API is running!"}