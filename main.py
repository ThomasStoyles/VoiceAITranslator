import whisper
import openai
import pyaudio
import wave
import tempfile

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

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

    print("✅ Recording finished!")

def transcribe_audio(filename="output.wav"):
    print("📝 Transcribing...")
    result = model.transcribe(filename)
    return result["text"]

def translate_with_llm(text, target_lang="French"):
    print("🌐 Translating...")
    prompt = f"Translate the following sentence to {target_lang}:\n\"{text}\""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()
    print(f"\n🗣️ You said: {text}")
    
    translated = translate_with_llm(text, target_lang="Spanish")
    print(f"\n🈯 Translated: {translated}")
