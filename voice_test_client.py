import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import pyttsx3
import requests

# Load whisper model
model = whisper.load_model("base")

# Text to speech engine
engine = pyttsx3.init()


def record_audio():

    fs = 44100
    seconds = 5

    print("🎤 Speak now...")

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write("record.wav", fs, recording)

    print("✅ Recording complete")


def speech_to_text():

    result = model.transcribe("record.wav")

    return result["text"]


def ask_ai(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def speak(text):

    engine.say(text)
    engine.runAndWait()


def run():

    record_audio()

    user_text = speech_to_text()

    print("👤 You:", user_text)

    reply = ask_ai(user_text)

    print("🤖 AI:", reply)

    speak(reply)


run()