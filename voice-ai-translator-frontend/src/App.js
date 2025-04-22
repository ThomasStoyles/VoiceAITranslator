import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

const App = () => {
  const [transcript, setTranscript] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [targetLanguage, setTargetLanguage] = useState('es'); // default Spanish

  const handleVoiceInput = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert('Your browser does not support Speech Recognition');
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();
    setIsListening(true);

    recognition.onresult = (event) => {
      const result = event.results[0][0].transcript;
      setTranscript(result);
      setIsListening(false);
    };

    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error);
      setIsListening(false);
    };

    recognition.onend = () => {
      setIsListening(false);
    };
  };

  const handleTranslate = async () => {
    try {
      const response = await axios.post('http://localhost:8000/translate', {
        text: transcript,
        target_language: targetLanguage
      });
      setTranslatedText(response.data.translation);
    } catch (error) {
      console.error('Translation error:', error);
      alert('Failed to translate. Check backend.');
    }
  };

  return (
    <div className="container py-5">
      <h1 className="text-center mb-4">🎤 Voice AI Translator</h1>

      <div className="text-center mb-3">
        <button className="btn btn-primary" onClick={handleVoiceInput} disabled={isListening}>
          {isListening ? 'Listening...' : 'Start Voice Input'}
        </button>
      </div>

      <div className="text-center mb-3">
        <label htmlFor="languageSelect" className="form-label">Translate to:</label>
        <select
          className="form-select w-auto d-inline-block"
          id="languageSelect"
          value={targetLanguage}
          onChange={(e) => setTargetLanguage(e.target.value)}
        >
          <option value="es">Spanish</option>
          <option value="fr">French</option>
          <option value="de">German</option>
          <option value="hi">Hindi</option>
          <option value="zh">Chinese</option>
          {/* Add more languages as needed */}
        </select>
      </div>

      {transcript && (
        <div className="text-center mb-3">
          <h5>Original (English):</h5>
          <p className="lead">{transcript}</p>
          <button className="btn btn-success mt-2" onClick={handleTranslate}>
            Translate
          </button>
        </div>
      )}

      {translatedText && (
        <div className="text-center mt-4">
          <h5>Translation:</h5>
          <p className="lead text-success">{translatedText}</p>
        </div>
      )}
    </div>
  );
};

export default App;
