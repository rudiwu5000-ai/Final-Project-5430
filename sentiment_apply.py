#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 14:17:24 2025

@author: rudiwu
"""

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df_train = pd.read_csv("wsb3000_with_sentiment.csv")
df_new = pd.read_csv("Stock wallstreetbets.csv")

TEXT_COL_TRAIN = "Title"
LABEL_COL_TRAIN = "Sentiment"
TEXT_COL_NEW = "Headline"

# Data training
train_mask = df_train[TEXT_COL_TRAIN].astype(str).str.len() > 0
X_train = df_train.loc[train_mask, TEXT_COL_TRAIN].astype(str)
y_train = df_train.loc[train_mask, LABEL_COL_TRAIN]
clf = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000, ngram_range=(1, 2))),
    ("logreg", LogisticRegression(max_iter=1000))
])

# Model training for sentiment analysis
clf.fit(X_train, y_train)


X_new = df_new[TEXT_COL_NEW].astype(str)
df_new["ml_sentiment"] = clf.predict(X_new)

# Output
output_path = "Stock_wallstreetbets_with_ml_sentiment.csv"
df_new.to_csv(output_path, index=False)

