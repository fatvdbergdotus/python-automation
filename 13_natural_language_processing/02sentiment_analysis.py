import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('twitter_samples')

# function to get sentiment scores for a given text
def get_sentiment_scores(text: str) -> str:
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

# Example usage
text1 = "I love programming, but sometimes it can be frustrating."
print_sentiment_scores(text1)

text2 = "I hate debugging, it is so annoying."
print_sentiment_scores(text2)

for i in range(5):
    text = nltk.corpus.twitter_samples.strings()[i]
    print_sentiment_scores(text)
    
