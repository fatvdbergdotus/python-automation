from speech_recognition import Recognizer, AudioFile

from openai import OpenAI
# py -m pip install openai

import argostranslate.translate

# Initialize the recognizer
recognizer = Recognizer()

# Load the audio file
with AudioFile("chile.wav") as source:
    audio_data = recognizer.record(source)

# Recognize the speech in the audio file and print the result
text=""
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized text:", text)
except Exception as e:
    print("Error recognizing speech:", e)

# Translate the recognized text and print the result
translated = argostranslate.translate.translate(text, "en", "nl")
print("Translated text:", translated)