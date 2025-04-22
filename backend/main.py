from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import whisper
import openai
import os

# Load API key
def get_api_key():
    with open(r'C:\Users\Thomas\.secerts\OPENAPIKEY.txt', 'r') as file:
        return file.read().strip()

openai.api_key = get_api_key()

# Load Whisper model once
model = whisper.load_model("base")

# FastAPI setup
app = FastAPI()

# Enable frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Translation function
def translate_with_llm(text, target_lang_code="fr"):
    prompt = f"Translate the following sentence to {target_lang_code}:\n\"{text}\""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

# API route
@app.post("/translate")
async def translate(request: TranslationRequest):
    translated_text = translate_with_llm(request.text, request.target_language)
    return {"translation": translated_text}
