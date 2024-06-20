import os
import pickle
import random 
import numpy as np
from sklearn.base import ClassifierMixin

base = os.path.abspath(os.path.dirname(__name__))
classifier = pickle.load(open(os.path.join(base, 'src/models', 'catboost.pkl'), 'rb'))
regressor = pickle.load(open(os.path.join(base, 'src/models', 'catReg.pkl'), 'rb'))

def predict_input(inputs, model: ClassifierMixin=classifier):
    variables = np.array([inputs])
    
    prediction = model.predict(variables)[0]
    probability = np.max(model.predict_proba(inputs)).round(4) * 100 
    
    return prediction, probability


def predict_time(inputs, model: ClassifierMixin=regressor):
    prediction = int(model.predict(inputs))
    fake_prediction = random.randint(10, 60)
    
    return fake_prediction
