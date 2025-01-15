import React, { useState } from 'react';
import axios from 'axios';

function ROT13Cipher() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/rot13/encrypt', null, {
        params: { text }
      });

      setResult(response.data.encrypted_text);
    } catch (error) {
      console.error('Error:', error);
      setResult('An error occurred');
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-8 rounded-xl shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">ROT13 Cipher</h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-2">
            Text to Encrypt/Decrypt:
            <input 
              type="text" 
              value={text}
              onChange={(e) => setText(e.target.value)}
              className="w-full p-2 border rounded mt-1"
              required
              placeholder="ROT13 is a symmetric cipher"
            />
          </label>
        </div>

        <button 
          type="submit" 
          className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600"
        >
          Encrypt/Decrypt
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

export default ROT13Cipher;