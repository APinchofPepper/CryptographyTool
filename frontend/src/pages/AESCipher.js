import React, { useState } from 'react';
import axios from 'axios';

function AESCipher() {
  const [text, setText] = useState('');
  const [key, setKey] = useState('');
  const [result, setResult] = useState('');
  const [mode, setMode] = useState('encrypt');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const endpoint = mode === 'encrypt' ? 
        `/aes/encrypt` : 
        `/aes/decrypt`;
      
      const response = await axios.post(endpoint, null, {
        params: { text, key }
      });

      setResult(mode === 'encrypt' ? 
        response.data.encrypted_text : 
        response.data.decrypted_text
      );
    } catch (error) {
      console.error('Error:', error);
      setResult('An error occurred');
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-8 rounded-xl shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">AES Cipher</h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-2">
            Text to {mode}:
            <input 
              type="text" 
              value={text}
              onChange={(e) => setText(e.target.value)}
              className="w-full p-2 border rounded mt-1"
              required
            />
          </label>
        </div>

        <div>
          <label className="block mb-2">
            Encryption Key:
            <input 
              type="text" 
              value={key}
              onChange={(e) => setKey(e.target.value)}
              className="w-full p-2 border rounded mt-1"
              required
              placeholder="Must be 16, 24, or 32 characters"
            />
          </label>
        </div>

        <div className="flex space-x-4">
          <button 
            type="button"
            onClick={() => setMode('encrypt')}
            className={`flex-1 p-2 rounded ${mode === 'encrypt' ? 'bg-blue-600 text-white' : 'bg-gray-200'}`}
          >
            Encrypt
          </button>
          <button 
            type="button"
            onClick={() => setMode('decrypt')}
            className={`flex-1 p-2 rounded ${mode === 'decrypt' ? 'bg-blue-600 text-white' : 'bg-gray-200'}`}
          >
            Decrypt
          </button>
        </div>

        <button 
          type="submit" 
          className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600"
        >
          {mode === 'encrypt' ? 'Encrypt' : 'Decrypt'}
        </button>
      </form>

      {result && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h3 className="font-bold mb-2">Result:</h3>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default AESCipher;