# py -m pip install nltk
import nltk
from nltk.stem import WordNetLemmatizer

# py -m pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd

divider = "-" * 50 + "\n"

nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()

# check if two verbs have the same lemma
def check_same_lemma(word1: str, word2: str) -> bool:
    lemma1 = lemmatizer.lemmatize(word1, "v")
    lemma2 = lemmatizer.lemmatize(word2, "v")
    return lemma1 == lemma2

x = 'is'
y = 'was'
print(divider + f"Do '{x}' and '{y}' have the same lemma? {check_same_lemma(x, y)}")


# lemmatization of sentences
sentence1 = "Vegetables are types of plants"
sentence2 = "A carrot is a type of vegetable"

def lemmatize_sentence(sentence1: str) -> list[str]:
    # Tokenize the sentence and convert it to lowercase
    tokenized_sentence = nltk.word_tokenize(sentence1.lower())

    # Get the part-of-speech tags for the tokens
    pos_tags = nltk.pos_tag(tokenized_sentence)

    # Lemmatize each token based on its part-of-speech tag
    sentence_lemmas = [] 
    for token, pos in pos_tags:
        if pos[0].lower() in ['n', 'v', 'a', 'r']: # Only lemmatize nouns, verbs, adjectives, and adverbs
            sentence_lemmas.append(lemmatizer.lemmatize(token, pos[0].lower()))

    return sentence_lemmas

print(divider + f"Lemmas of sentence 1: {lemmatize_sentence(sentence1)}")
print(f"Lemmas of sentence 2: {lemmatize_sentence(sentence2)}")


# similarity of sentences using Jaccard similarity
def sentence_similarity(sentence1: str, sentence2: str) -> float:
    lemmas1 = set(lemmatize_sentence(sentence1))
    lemmas2 = set(lemmatize_sentence(sentence2))

    # Compute the Jaccard similarity between the sets of lemmas
    intersection = lemmas1.intersection(lemmas2)
    union = lemmas1.union(lemmas2)
    return len(intersection) / len(union) if union else 0.0

print(f"Similarity between sentence 1 and sentence 2: {sentence_similarity(sentence1, sentence2)}")


# answer a question based on a text of multiple sentences using Jaccard similarity
def answer_question(question: str, text: str) -> str:
    max_similarity = 0.0
    best_sentence = "I don't know."
    split_text = nltk.sent_tokenize(text)

    for sentence in split_text:
        similarity = sentence_similarity(question, sentence)
        if similarity > max_similarity:
            max_similarity = similarity
            best_sentence = sentence
    return best_sentence


question = "what are vegetables?"
original_text = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked."
print(divider + f"Answer to the question: {answer_question(question, original_text)}")
print(divider)

# answer a question based on a text of multiple sentences using TF-IDF and cosine similarity
def answer_question2(question: str, text: str) -> str:
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)
    tv = TfidfVectorizer(tokenizer=lemmatize_sentence)

    # Fit the TF-IDF vectorizer on the question and the sentences
    tfidf_matrix = tv.fit_transform([question] + sentences)

    # Print the TF-IDF matrix for debugging purposes
    df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=tv.get_feature_names_out())
    print(f"TF-IDF DataFrame:\n{df_tfidf}")

    # Compute the cosine similarity between the question and each sentence in the text
    values = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    print(f"Cosine similarity values:\n{values}")

    # Find the sentence with the highest cosine similarity to the question
    best_sentence_index = values.argmax()
    best_sentence = sentences[best_sentence_index]
    return best_sentence

print(f"Answer to the question using TF-IDF and cosine similarity: {answer_question2(question, original_text)}")
