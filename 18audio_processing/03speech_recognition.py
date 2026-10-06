from speech_recognition import Recognizer, AudioFile

from openai import OpenAI
# py -m pip install openai

# Initialize the recognizer
recognizer = Recognizer()

# Load the audio file
with AudioFile("chile.wav") as source:
    audio_data = recognizer.record(source)

# Recognize the speech in the audio file
text=""
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized text:", text)
except Exception as e:
    print("Error recognizing speech:", e)
