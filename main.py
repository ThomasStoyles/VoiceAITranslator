import whisper
import openai
import pyaudio
import wave
import tempfile
import os

def get_api_key():
    with open(r'C:\Users\Thomas\.secerts\OPENAPIKEY.txt', 'r') as file:
        return file.read().strip()
    
openai.api_key = get_api_key()

# Supported language options
LANGUAGES = {
    "1": ("Spanish", "es"),
    "2": ("French", "fr"),
    "3": ("German", "de"),
    "4": ("Italian", "it"),
    "5": ("Chinese", "zh"),
    "6": ("Japanese", "ja"),
    "7": ("Korean", "ko"),
    "8": ("Hindi", "hi"),
    "9": ("Arabic", "ar")
}

def choose_language():
    print("\n🌍 Choose a target language:")
    for key, (name, _) in LANGUAGES.items():
        print(f"{key}. {name}")
    choice = input("Enter the number of your choice: ").strip()
    return LANGUAGES.get(choice, ("Spanish", "es"))  # Default to Spanish if invalid


# Load the Whisper model (can use "tiny", "base", "small", "medium", "large")
model = whisper.load_model("base")

def record_audio(filename="output.wav", record_seconds=5):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100

    p = pyaudio.PyAudio()
    print("🎙️ Recording... Speak now.")
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []
    for _ in range(0, int(fs / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

    print(f"✅ Recording finished! Audio saved to: {filename}")
    return filename  # Ensure the filename is returned


def transcribe_audio(filename="output.wav"):
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return None
    print("📝 Transcribing...")
    try:
        result = model.transcribe(filename)
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


def translate_with_llm(text, target_lang_code="fr"):
    print("🌐 Translating...")
    prompt = f"Translate the following sentence to {target_lang_code}:\n\"{text}\""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    # Step 1: Choose a language
    language_name, lang_code = choose_language()
    print(f"\n🔁 Translating to: {language_name}\n")

    # Step 2: Record voice and transcribe
    filename = record_audio()  # Capture the returned filename
    if filename is None:
        print("Error: Audio file was not recorded correctly.")
        exit()

    text = transcribe_audio(filename)  # Pass the correct filename here

    # Step 3: Translate and show output
    if text:
        print(f"\n🗣️ You said:  {text}")
        print("🌐 Translating...")
        translated = translate_with_llm(text, target_lang_code=lang_code)  # Use lang_code here
        print(f"\n🈯 Translated ({language_name}): {translated}")
