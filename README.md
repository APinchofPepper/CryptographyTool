# Cryptography Tool

A comprehensive web application for exploring various cryptographic algorithms, including Caesar Cipher, Vigenère Cipher, AES, RSA, and ROT13.

## Features

- Caesar Cipher: Shift-based encryption
- Vigenère Cipher: Polyalphabetic substitution cipher
- AES Encryption: Advanced Encryption Standard
- RSA Encryption: Asymmetric encryption with key generation
- ROT13 Cipher: Simple letter substitution cipher

## Technologies Used

### Backend
- Python
- FastAPI
- PyCryptodome

### Frontend
- React
- Axios
- Tailwind CSS

## Prerequisites

### Backend
- Python 3.12+
- pip
- Virtualenv (recommended)

### Frontend
- Node.js 14+
- npm

## Installation

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/APinchofPepper/CryptographyTool.git
cd CryptographyTool
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install backend dependencies
```bash
pip install -r requirements.txt
```

### Frontend Setup

1. Navigate to frontend directory
```bash
cd frontend
```

2. Install frontend dependencies
```bash
npm install
```

## Running the Application

### Backend
```bash
# From the project root
uvicorn app.main:app --reload
```

### Frontend
```bash
# From the frontend directory
npm start
```

## Testing

### Backend Tests
```bash
pytest tests/
```

### Frontend Tests
```bash
npm test
```

## Project Structure

```
CryptographyTool/
│
├── app/
│   ├── routes/           # API route handlers
│   ├── utils/            # Cryptographic utility functions
│   └── main.py           # FastAPI application
│
├── frontend/
│   ├── src/
│   │   ├── pages/        # React page components
│   │   ├── App.js        # Main React application
│   │   └── index.js      # Entry point
│
└── tests/                # Unit and integration tests
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Jack - jack@cookietowncookies.com

Project Link: [https://github.com/APinchofPepper/CryptographyTool](https://github.com/APinchofPepper/CryptographyTool)