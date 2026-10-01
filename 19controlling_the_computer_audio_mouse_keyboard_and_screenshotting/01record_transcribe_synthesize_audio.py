import wavio
import sounddevice as sd
import pyttsx3

from speech_recognition import (
    Recognizer,
    AudioFile,
    UnknownValueError,
    RequestError
)

# Initialize TTS engine once
engine = pyttsx3.init()

# Record audio from microphone
def record_audio(file_path: str, duration: int = 10, fs: int = 44100) -> None:
    print("Recording...")
    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1
    )
    sd.wait()
    print("Recording finished.")
    wavio.write(file_path, audio, fs, sampwidth=2)


# Transcribe audio
def transcribe_audio(file_path: str) -> str:
    recognizer = Recognizer()

    with AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)

    except UnknownValueError:
        print("Could not understand the audio.")
        return ""

    except RequestError as e:
        print(f"Google Speech Recognition error: {e}")
        return ""


# Text-to-speech
def speak_text(text: str) -> None:
    if not text:
        return

    try:
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"TTS error: {e}")


# Main application in which we record, transcribe, and speak audio
def main():

    duration = 10
    fs = 44100

    try:
        record_audio("output.wav", duration, fs)
        transcription = transcribe_audio("output.wav")
        print("Transcribed text:", transcription)
        speak_text(transcription)

    finally:
        engine.stop()


if __name__ == "__main__":
    main()