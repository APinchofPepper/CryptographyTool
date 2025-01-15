import React, { useState } from 'react';
import axios from 'axios';

function RSACipher() {
  const [text, setText] = useState('');
  const [key, setKey] = useState('');
  const [result, setResult] = useState('');
  const [mode, setMode] = useState('encrypt');
  const [generatedKeys, setGeneratedKeys] = useState({
    publicKey: '',
    privateKey: ''
  });

  const handleGenerateKeys = async () => {
    try {
      const response = await axios.get('/rsa/generate-keys');
      setGeneratedKeys({
        publicKey: response.data.public_key,
        privateKey: response.data.private_key
      });
      // Automatically set the key based on current mode
      setKey(mode === 'encrypt' ? response.data.public_key : response.data.private_key);
    } catch (error) {
      console.error('Error generating keys:', error);
      setResult('Failed to generate keys');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const endpoint = mode === 'encrypt' ? 
        `/rsa/encrypt` : 
        `/rsa/decrypt`;
      
      const response = await axios.post(endpoint, null, {
        params: { 
          text, 
          [mode === 'encrypt' ? 'public_key' : 'private_key']: key 
        }
      });

      // Check if the response contains an error
      if (response.data.error) {
        setResult(`Error: ${response.data.error}`);
      } else {
        setResult(mode === 'encrypt' ? 
          response.data.encrypted_text : 
          response.data.decrypted_text
        );
      }
    } catch (error) {
      console.error('Error:', error);
      setResult('An error occurred');
    }
  };

  const handleCopyPublicKey = () => {
    navigator.clipboard.writeText(generatedKeys.publicKey);
    alert('Public Key copied to clipboard!');
  };

  const handleCopyPrivateKey = () => {
    navigator.clipboard.writeText(generatedKeys.privateKey);
    alert('Private Key copied to clipboard!');
  };

  return (
    <div className="max-w-md mx-auto bg-white p-8 rounded-xl shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">RSA Cipher</h2>
      
      {/* Key Generation Section */}
      <div className="mb-6">
        <button 
          onClick={handleGenerateKeys}
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 mb-4"
        >
          Generate New Key Pair
        </button>

        {generatedKeys.publicKey && (
          <div className="mt-4 space-y-2">
            <div>
              <h3 className="font-bold">Public Key:</h3>
              <div className="flex">
                <textarea 
                  readOnly 
                  value={generatedKeys.publicKey}
                  className="w-full p-2 border rounded text-xs h-24 mr-2 overflow-auto"
                />
                <button 
                  onClick={handleCopyPublicKey}
                  className="bg-green-500 text-white p-2 rounded hover:bg-green-600"
                >
                  Copy
                </button>
              </div>
            </div>
            <div>
              <h3 className="font-bold">Private Key:</h3>
              <div className="flex">
                <textarea 
                  readOnly 
                  value={generatedKeys.privateKey}
                  className="w-full p-2 border rounded text-xs h-24 mr-2 overflow-auto"
                />
                <button 
                  onClick={handleCopyPrivateKey}
                  className="bg-green-500 text-white p-2 rounded hover:bg-green-600"
                >
                  Copy
                </button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Encryption/Decryption Form */}
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
            {mode === 'encrypt' ? 'Public Key:' : 'Private Key:'}
            <textarea 
              value={key}
              onChange={(e) => setKey(e.target.value)}
              className="w-full p-2 border rounded mt-1 h-32 overflow-auto"
              required
              placeholder={mode === 'encrypt' 
                ? 'Paste your public key' 
                : 'Paste your private key'}
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
          <div className="break-words w-full max-w-full overflow-x-auto">
            {result}
          </div>
        </div>
      )}
    </div>
  );
}

export default RSACipher;