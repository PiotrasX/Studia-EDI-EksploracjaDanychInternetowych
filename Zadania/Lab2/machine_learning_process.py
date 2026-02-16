import pandas as pd
import string
import re
import nltk.corpus

pd.set_option('display.max_colwidth', 100)
data = pd.read_csv('Organizations.csv', sep=',')
data.drop(data.columns[[0, 1, 8]], axis=1, inplace=True)
print("Początkowe dane:")
print(data.head(), "\n")

# Usuwanie znaków interpunkcyjnych

def remove_punctuation(text):
    no_punctuation = text
    if not isinstance(text, int) and not isinstance(text, float):
        no_punctuation = "".join([char for char in text if char not in string.punctuation])
    return no_punctuation

data = data.apply(lambda text: text.apply(remove_punctuation))
print("Usuwanie znaków interpunkcyjnych:")
print(data.head(), "\n")

# Tokenizacja

def to_lower(text):
    lower = text
    if not isinstance(text, int) and not isinstance(text, float):
        lower = text.lower()
    return lower

def tokenize(text):
    tokens = text
    if not isinstance(text, int) and not isinstance(text, float):
        tokens = re.split(r'\W+', text)
    return tokens

data = data.apply(lambda text: text.apply(to_lower).apply(tokenize))
print("Tokenizacja:")
print(data.head(), "\n")

# Usuwanie stopwords

# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")

def remove_stopwords(text):
    no_stopwords = text
    if not isinstance(text, int) and not isinstance(text, float):
        no_stopwords = [word for word in text if word not in stopwords]
    return no_stopwords

data = data.apply(lambda text : text.apply(remove_stopwords))
print("Usuwanie stopwords:")
print(data.head())
