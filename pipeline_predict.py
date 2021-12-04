import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Binarizer

from sklearn.pipeline import Pipeline

from feature_engine.imputation import(
    AddMissingIndicator,
    MeanMedianImputer,
    CategoricalImputer
)

from feature_engine.encoding import (
    RareLabelEncoder,
    OrdinalEncoder
)

from feature_engine.transformation import LogTransformer
from feature_engine.transformation import PowerTransformer

from feature_engine.selection import DropFeatures
from feature_engine.wrappers import SklearnTransformerWrapper

from sklearn.metrics import mean_squared_error 

import joblib

import config as cfg

#Librería creada
import my_preprocessors as mypp

X_test = pd.read_csv("test.csv")
X_test = X_test[cfg.FEATURES]

# Cargamos modelo y pipeline
Survived_model = joblib.load('Survived_pipeline.pkl')

def predict(X):
    X = X[cfg.FEATURES]
    predicts = Survived_model.predict(X)
    #Survived = np.exp(predicts)
    #print(Survived)

predict(X_test)