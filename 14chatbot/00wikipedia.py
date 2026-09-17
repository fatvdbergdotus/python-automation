import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# py -m pip install wikipedia
import wikipedia

wikipedia.set_lang("en")

page = wikipedia.page("Vegetable")
original_text = page.content

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

prompt = "Hi, what do you want to know?"

lemmatizer = nltk.WordNetLemmatizer()

# Function to lemmatize a sentence based on its POS tags
def lemma_me(sentence: str) -> list[str]:
    words = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(words)

    sentence_lemmas = []
    for word, pos in pos_tags:
        if pos.startswith('J'):
            sentence_lemmas.append(lemmatizer.lemmatize(word, pos='a'))
        elif pos.startswith('V'):
            sentence_lemmas.append(lemmatizer.lemmatize(word, pos='v'))
        elif pos.startswith('N'):
            sentence_lemmas.append(lemmatizer.lemmatize(word, pos='n'))
        elif pos.startswith('R'):
            sentence_lemmas.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            sentence_lemmas.append(lemmatizer.lemmatize(word))
    return sentence_lemmas

# Function to get the most similar sentence from the original text based on the question
def get_most_similar_sentence(question: str, original_text: str) -> str:
    sentence_tokens = [question] + nltk.sent_tokenize(original_text)
    tv = TfidfVectorizer(tokenizer=lemma_me, token_pattern=None)
    tfidf_matrix = tv.fit_transform(sentence_tokens)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    most_similar_sentence_index = cosine_similarities.argmax()
    if cosine_similarities[0, most_similar_sentence_index] > 0:
        return sentence_tokens[most_similar_sentence_index + 1]  # +1 because we skipped the question
    else:
        return "I don't know the answer to that question."

# Main loop to interact with the user
if __name__ == "__main__":
    while True:
        question = input(prompt + "\n")
        if question.lower() in ["exit", "quit"]:
            break
        most_similar_sentence = get_most_similar_sentence(question, original_text)
        print(most_similar_sentence)