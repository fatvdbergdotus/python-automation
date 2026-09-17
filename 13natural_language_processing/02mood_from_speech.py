import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# py -m pip install SpeechRecognition
from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

def transcribe_audio(file_path: str) -> str:
    with AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except Exception as e:
            return ""

# function to get sentiment scores for a given text
def get_sentiment_scores(text: str) -> tuple[str, str]:
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return text, sentiment+" "+str(scores['compound'])

# function to print sentiment scores for a given text
def print_sentiment_scores(text: str) -> None:
    text, sentiment = get_sentiment_scores(text)
    print(f"Sentiment scores for '{text}': {sentiment}")

# function to print mood from an audio file
def print_mood_from_audio(file_path: str) -> None:
    text = transcribe_audio(file_path)
    if text:
        print_sentiment_scores(text)
    else:
        print("Could not transcribe audio.")

if __name__ == "__main__":
    print_mood_from_audio('chile.wav')