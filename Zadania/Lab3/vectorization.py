import pandas as pd
import nltk
import re
import string
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("SMSDataset.csv", sep=',')
data = data.drop(columns=data.columns[-3:])
data.columns = ['label', 'body_text']
print("Początkowe dane:")
print(data.head(), "\n")

# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")
ps = PorterStemmer()

def clean_text(text):
    if not isinstance(text, int) and not isinstance(text, float):
        no_punctuation = "".join([char for char in text if char not in string.punctuation])
        lower = no_punctuation.lower()
        tokens = re.split(r'\W+', lower)
        text = tokens
    text = [word for word in text if word not in stopwords]
    return text

def steaming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text

data_clear_text = data.apply(lambda text: text.apply(clean_text))
data_clear_text.columns = ['label', 'body_clear_text']
print("Usuwanie znaków interpunkcyjnych, tokenizacja, usuwanie stopwords:")
print(data_clear_text.head(), "\n")

data_text_stemmed = data_clear_text.apply(lambda text: text.apply(steaming))
data_text_stemmed.columns = ['label', 'body_text_stemmed']
print("Stemming:")
print(data_text_stemmed.head(), "\n")

data_text_stemmed['body_text_stemmed'] = (
    data_text_stemmed['body_text_stemmed']
    .apply(lambda text: ' '.join(text) if isinstance(text, list) else ''))

# Count Vectorizer

count_vect = CountVectorizer()
X_counts_1 = count_vect.fit_transform(data_text_stemmed['body_text_stemmed'])
print("Kształt 'Count Vectorizer':", X_counts_1.shape)
X_counts_1_array = X_counts_1.toarray()
count_vect_result = pd.DataFrame(X_counts_1_array, columns=count_vect.get_feature_names_out())
print("Macierz 'Count Vectorizer':\n", count_vect_result, "\n")

# N-Gram

ngram_vect = CountVectorizer(ngram_range=(2,2))
X_counts_2 = ngram_vect.fit_transform(data_text_stemmed['body_text_stemmed'])
print("Kształt 'N-Gram':", X_counts_2.shape)
X_counts_2_array = X_counts_2.toarray()
ngram_vect_result = pd.DataFrame(X_counts_2_array, columns=ngram_vect.get_feature_names_out())
print("Macierz 'N-Gram':\n", ngram_vect_result, "\n")

# TF-IDF

tfidf_vect = TfidfVectorizer()
X_counts_3 = tfidf_vect.fit_transform(data_text_stemmed['body_text_stemmed'])
print("Kształt 'TF-IDF':", X_counts_3.shape)
X_counts_3_array = X_counts_3.toarray()
tfidf_vect_result = pd.DataFrame(X_counts_3_array, columns=tfidf_vect.get_feature_names_out())
print("Macierz 'TF-IDF':\n", tfidf_vect_result)
