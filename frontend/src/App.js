import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CaesarCipher from './pages/CaesarCipher';
import VigenereCipher from './pages/VigenereCipher';
import AESCipher from './pages/AESCipher';
import RSACipher from './pages/RSACipher';
import ROT13Cipher from './pages/ROT13Cipher';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-blue-600 text-white p-4">
          <div className="container mx-auto flex justify-between items-center">
            <h1 className="text-2xl font-bold">Cryptography Tool</h1>
            <div className="space-x-4">
              <Link to="/caesar" className="hover:text-blue-200">Caesar</Link>
              <Link to="/vigenere" className="hover:text-blue-200">Vigenère</Link>
              <Link to="/aes" className="hover:text-blue-200">AES</Link>
              <Link to="/rsa" className="hover:text-blue-200">RSA</Link>
              <Link to="/rot13" className="hover:text-blue-200">ROT13</Link>
            </div>
          </div>
        </nav>

        <div className="container mx-auto mt-8 p-4">
          <Routes>
            <Route path="/caesar" element={<CaesarCipher />} />
            <Route path="/vigenere" element={<VigenereCipher />} />
            <Route path="/aes" element={<AESCipher />} />
            <Route path="/rsa" element={<RSACipher />} />
            <Route path="/rot13" element={<ROT13Cipher />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold mb-4">Welcome to the Cryptography Tool</h2>
      <p className="text-xl">Select a cipher from the navigation menu to get started!</p>
    </div>
  );
}

export default App;