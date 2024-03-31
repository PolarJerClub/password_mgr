import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import string

# Download NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = input("Enter a phrase or passage and I will analyze it to find the most common words: ")

def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())

    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

def analyze_text(text):
    # Preprocess the text
    tokens = preprocess_text(text)

    # Frequency distribution of words
    fdist = FreqDist(tokens)

    # Print the most common words
    print("Most common words:")
    for word, frequency in fdist.most_common(5):
        print(f"{word}: {frequency}")

    # Total number of unique words
    unique_words = len(fdist.keys())
    print(f"\nTotal unique words: {unique_words}")

if __name__ == "__main__":
    # Example text
    # text = "Natural language processing (NLP) is a subfield of linguistics, " \
    #        "computer science, and artificial intelligence concerned with " \
    #        "the interactions between computers and human language."

    # Analyze the text
    analyze_text(text)