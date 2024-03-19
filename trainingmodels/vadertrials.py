import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import re
from sklearn.metrics import accuracy_score,classification_report, ConfusionMatrixDisplay
from string import punctuation
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.naive_bayes import GaussianNB

test=pd.DataFrame()
train=pd.DataFrame()
test = pd.read_csv('test.csv', 
                    delimiter=',', encoding='ISO-8859-1')
test.drop(columns=['textID','Time of Tweet', 'Age of User', 'Country', 'Population -2020', 'Land Area (Km²)', 'Density (P/Km²)'])
train = pd.read_csv('train.csv', 
                    delimiter=',', encoding='ISO-8859-1')
train.drop(columns=['textID','selected_text','Time of Tweet', 'Age of User', 'Country', 'Population -2020', 'Land Area (Km²)', 'Density (P/Km²)'])
stuff_to_be_removed = list(punctuation)

def vader():
    sia = SentimentIntensityAnalyzer()
    Y_label=[]
    Y_result=[]
    #test.to_csv('data.txt', sep='\t', index=False)
    f = open("results.txt", "a", encoding="utf-8")
    for index, row in test.iterrows():
        f.write(str(row['text'])+" ")
        f.write(str(row['sentiment'])+" ")
        #add to array of true labels
        Y_label.append(str(row['sentiment']))
        polarity=sia.polarity_scores(str(row['text']))
        pmax=max(polarity)
        if pmax=='pos':
            pmax='positive'
        elif pmax=='neg':
            pmax='negative'
        else:
            pmax='neutral'

        #add predicted label from Vader
        Y_result.append(pmax)
        f.write(pmax+" ")
        f.write("\n")
        
    f.close()
    print(classification_report(Y_label, Y_result))

vader()