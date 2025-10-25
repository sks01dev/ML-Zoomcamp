#!/usr/bin/env python
# coding: utf-8

# This is a starter notebook for an updated module 5 of ML Zoomcamp
# 
# The code is based on the modules 3 and 4. We use the same dataset: [telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

# Import the necessary libraries
import numpy as np
import pandas as pd
import sklearn
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


# Load the data
def load_data():    
    data_url =  "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/course_lead_scoring.csv"
    df = pd.read_csv(data_url)
    return df



def train_model(df):
    # Preprocessing using DictVectorizer and Training the Logistic Regressio model 
    categorical = ['lead_source']
    numeric = ['number_of_courses_viewed', 'annual_income']

    df[categorical] = df[categorical].fillna('NA')
    df[numeric] = df[numeric].fillna(0)

    train_dict = df[categorical + numeric].to_dict(orient='records')

    pipeline = make_pipeline(
        DictVectorizer(),
        LogisticRegression(solver='liblinear')
    )

    # the target variable
    y_train = df.converted

    pipeline.fit(train_dict, y_train)
    return pipeline


def save_model(filename, model):
    with open(filename, 'wb') as f_out:
        pickle.dump(model, f_out)
    
    print(f"Model saved to {filename}")


df = load_data()
pipeline = train_model(df)
save_model('model.bin', pipeline)


