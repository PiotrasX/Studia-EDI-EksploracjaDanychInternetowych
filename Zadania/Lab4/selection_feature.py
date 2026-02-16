import pandas as pd
import numpy as np
import string
import plotly.graph_objects as go

from matplotlib import pyplot
from plotly.subplots import make_subplots

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 35)

# Długość wiadomości oraz procentowy udział znaków interpunkcyjnych

def count_punctuation(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count / (len(text) - text.count(" ")), 3) * 100

data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(" "))
data['punctuation_%'] = data['body_text'].apply(lambda x: count_punctuation(x))

print("Długość wiadomości oraz procentowy udział znaków interpunkcyjnych:")
print(data.head(), "\n")

# Ewaluacja długości wiadomości
bins1 = np.linspace(0, 200, 50)
pyplot.hist(data[data['label'] == 'spam']['body_len'], bins1, alpha=0.5, density=True, label='spam')
pyplot.hist(data[data['label'] == 'ham']['body_len'], bins1, alpha=0.5, density=True, label='ham')
pyplot.legend(loc='upper left')
pyplot.show()

# Ewaluacja procentowej zawartości znaków interpunkcyjnych
bins2 = np.linspace(0, 50, 50)
pyplot.hist(data[data['label'] == 'spam']['punctuation_%'], bins2, alpha=0.5, density=True, label='spam')
pyplot.hist(data[data['label'] == 'ham']['punctuation_%'], bins2, alpha=0.5, density=True, label='ham')
pyplot.legend(loc='upper right')
pyplot.show()

# Ustalenie, które cechy należy poddać transformacji

pyplot.hist(data['body_len'], bins1)
pyplot.title("Body length distribution")
pyplot.show()
# Rozkład długości wiadomości jest względnie normalny, nie ma dużo przypadków odstających.
# Nie ma potrzeby transformacji.

pyplot.hist(data['punctuation_%'], bins2)
pyplot.title("Punctuation % distribution")
pyplot.show()
# Rozkład procentowej zawartości znaków interpunkcyjnych jest silnie skośny, ma większą ilość przypadków odstających.
# Warto poddać tę cechę transformacji.

print("Które cechy należy poddać transformacji:")
print("Transformacji należy poddać cechę z procentową zawartością znaków interpunkcyjnych.\n")

# Wskazanie, która transformacja Boxa Coxa będzie najlepsza

def box_cox_transform(x, lambd):
    if lambd == 0:
        return np.log(x)
    else:
        return (np.power(x, lambd) - 1) / lambd

data['punctuation_%_safe'] = data['punctuation_%'] + 1

box_cox_minus_2 = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, -2))
box_cox_minus_1 = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, -1))
box_cox_minus_pol = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, -0.5))
box_cox_0 = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, 0))
box_cox_pol = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, 0.5))
box_cox_1 = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, 1))
box_cox_2 = data['punctuation_%_safe'].apply(lambda x: box_cox_transform(x, 2))

fig = make_subplots(rows=3, cols=3)
fig.add_trace(go.Histogram(x=box_cox_minus_2, name='lambda = -2'), row=1, col=1)
fig.add_trace(go.Histogram(x=box_cox_minus_1, name='lambda = -1'), row=1, col=2)
fig.add_trace(go.Histogram(x=box_cox_minus_pol, name='lambda = -0.5'), row=1, col=3)
fig.add_trace(go.Histogram(x=box_cox_0, name='lambda = 0'), row=2, col=2)
fig.add_trace(go.Histogram(x=box_cox_pol, name='lambda = 0.5'), row=3, col=1)
fig.add_trace(go.Histogram(x=box_cox_1, name='lambda = 1'), row=3, col=2)
fig.add_trace(go.Histogram(x=box_cox_2, name='lambda = 2'), row=3, col=3)
fig.show()

print("Która transformacja Boxa Coxa będzie najlepsza:")
print("Najlepsza transformacja Boxa Coxa to będzie z lambda = 0.5.")
print("Dzieje się tak, ponieważ rozkład ten jest najbardziej symetryczny i przypomina normalny.")
print("Pozostałe wartości lambda dają rozkłady silnie skośne lub z dużą koncentracją przy jednym końcu.")
