import re
import nltk
import pandas as pd
import string
import warnings

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")
ps = nltk.PorterStemmer()

warnings.filterwarnings("ignore", category=DeprecationWarning)

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']

pd.set_option('display.width', 225)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 50)

def count_punctuation(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count / (len(text) - text.count(" ")), 3) * 100

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

data['body_text_stemmed'] = data['body_text'].apply(clean_text).apply(steaming)
data['body_text_stemmed'] = (data['body_text_stemmed']
                             .apply(lambda text: ' '.join(text) if isinstance(text, list) else ''))
data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(" "))
data['punctuation_%'] = data['body_text'].apply(lambda x: count_punctuation(x))

# Count Vectorizer
count_vect = CountVectorizer()
x_count = count_vect.fit_transform(data['body_text_stemmed'])
X_count_feat = pd.concat([data['body_len'], data['punctuation_%'],
                              pd.DataFrame(x_count.toarray(), columns=count_vect.get_feature_names_out())], axis=1)
# print("Count Vectorizer:\n", X_count_feat.head(), "\n")

# N-Gram
ngram_vect = CountVectorizer(ngram_range=(2,2))
x_ngram = ngram_vect.fit_transform(data['body_text_stemmed'])
X_ngram_feat = pd.concat([data['body_len'], data['punctuation_%'],
                              pd.DataFrame(x_ngram.toarray(), columns=ngram_vect.get_feature_names_out())], axis=1)
# print("N-Gram:\n", X_ngram_feat.head(), "\n")

# TF-IDF
tfidf_vect = TfidfVectorizer()
x_tfidf = tfidf_vect.fit_transform(data['body_text_stemmed'])
X_tfidf_feat = pd.concat([data['body_len'], data['punctuation_%'],
                              pd.DataFrame(x_tfidf.toarray(), columns=tfidf_vect.get_feature_names_out())], axis=1)
# print("TF-IDF:\n", X_tfidf_feat.head(), "\n")

# GridSearchCV

rf = RandomForestClassifier()
param = {'n_estimators': [10, 150, 300], 'max_depth': [30, 60, 90, None]}
gs = GridSearchCV(rf, param, cv=5, n_jobs=-1)

gs_fit_count = gs.fit(X_count_feat, data['label'])
print("Count:\n", pd.DataFrame(gs_fit_count.cv_results_).sort_values('mean_test_score', ascending=False)[0:5], "\n")

gs_fit_ngram = gs.fit(X_ngram_feat, data['label'])
print("N-Gram:\n", pd.DataFrame(gs_fit_ngram.cv_results_).sort_values('mean_test_score', ascending=False)[0:5], "\n")

gs_fit_tfidf = gs.fit(X_tfidf_feat, data['label'])
print("TF-IDF:\n", pd.DataFrame(gs_fit_tfidf.cv_results_).sort_values('mean_test_score', ascending=False)[0:5], "\n")

print("Najlepszy mean_test_score:")

gs.fit(X_count_feat, data['label'])
print("Count:", round(gs.best_score_, 5))

gs.fit(X_ngram_feat, data['label'])
print("N-Gram:", round(gs.best_score_, 5))

gs.fit(X_tfidf_feat, data['label'])
print("TF-IDF:", round(gs.best_score_, 5))
