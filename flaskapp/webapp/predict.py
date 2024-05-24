import os
import numpy as np
import pickle 
from sklearn.base import ClassifierMixin

base = os.path.dirname(__name__)
regressor = pickle.load(open(os.path.join(base, 'src/models', 'catReg.pkl'), 'rb'))
classifier = pickle.load(open(os.path.join(base, 'src/models', 'catboost.pkl'), 'rb'))

def predict_input(inputs, model: ClassifierMixin=classifier):
    prediction = model.predict(inputs)
    probability = np.max(model.predict_proba(inputs)).round(4) * 100 
    
    return prediction, probability


def predict_time(inputs, model: ClassifierMixin=regressor):
    prediction = model.predict(inputs).round(2)
    
    return prediction
