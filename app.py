





import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import time
from google import genai

st.title("Voice AI Chatbot")
st.write("Ask anything — the bot will respond!")

# Initialize Gemini client
client = genai.Client(api_key="")

def get_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",   # ✅ updated model name
        contents=prompt
    )
    return response.text

if st.button("🎤 Speak"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=10)

    st.info("Recognizing...")

    try:
        user_text = recognizer.recognize_google(audio)
        st.success(f"You said: {user_text}")

        reply = get_ai_response(user_text)
        st.write("Bot says:", reply)

        # Convert reply to speech
        tts = gTTS(reply)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            path = fp.name
            tts.save(path)

        st.audio(path)

        time.sleep(1)
        os.remove(path)

    except Exception as e:
        st.error(f"Error: {e}")
