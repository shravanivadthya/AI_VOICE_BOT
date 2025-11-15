import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source, phrase_time_limit=10)
        text = recognizer.recognize_google(audio_data)
    return text

def text_to_speech(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        path = fp.name
        tts.save(path)
    return path
