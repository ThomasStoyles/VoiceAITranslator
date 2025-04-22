
# 🎙️ Voice AI Translator 🌐

An intelligent voice translation tool that allows you to speak in English and instantly receive a translated output in the language of your choice. This full-stack project combines a **FastAPI + Whisper + OpenAI** backend with a **React + Bootstrap** frontend for a smooth user experience.

---

## 📸 Demo

> 🖼️ Coming soon: Add a screenshot or screen recording of your working app here!

---

## 🔧 Features

✅ Record voice directly in the browser  
✅ Transcribe spoken English using OpenAI's Whisper  
✅ Translate transcribed text into any supported language using GPT-3.5  
✅ Clean Bootstrap-based interface  
✅ Choose between multiple target languages (Spanish, French, Chinese, etc.)  
✅ API-key protected backend for secure OpenAI usage

---

## 📦 Tech Stack

### 🧠 Backend

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/docs)
- [Whisper](https://github.com/openai/whisper) (speech-to-text)
- [Pydantic](https://docs.pydantic.dev/)

### 🎨 Frontend

- [React](https://reactjs.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Axios](https://axios-http.com/) (for HTTP requests)

---

## 🚀 Getting Started

### ✅ Backend Setup

1. **Install dependencies**:

```bash
pip install fastapi uvicorn openai whisper pydantic
```

2. **Add OpenAI API key**:
Create a file here with your key:
```
C:\Users\Thomas\.secerts\OPENAPIKEY.txt
```

3. **Run backend**:

```bash
uvicorn main:app --reload
```

This will launch the FastAPI backend at `http://127.0.0.1:8000`.

---

### 🖥️ Frontend Setup

1. Navigate to the frontend folder:

```bash
cd voice-ai-translator-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend server:

```bash
npm start
```

This will open the React app at `http://localhost:3000`.

---

## 🌍 Supported Languages

Choose from the following:
- Spanish (`es`)
- French (`fr`)
- German (`de`)
- Italian (`it`)
- Chinese (`zh`)
- Japanese (`ja`)
- Korean (`ko`)
- Hindi (`hi`)
- Arabic (`ar`)

---

## 📁 Folder Structure

```
voice-ai-translator/
├── backend/
│   └── main.py
├── voice-ai-translator-frontend/
│   ├── public/
│   ├── src/
│   │   └── App.js
│   └── package.json
└── README.md
```

---

## 🔐 Security

- Your API key is **never exposed to the frontend**.
- The backend handles all interactions with OpenAI.

---

## 🧾 License

This project is licensed under the MIT License. Feel free to modify and share.

---

## ✅ To-Do / Future Improvements

- [ ] Add real-time audio streaming
- [ ] Add authentication for API access
- [ ] Deploy using Docker / Railway / Render
- [ ] Add mobile-friendly design
