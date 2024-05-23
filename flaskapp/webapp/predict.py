import os
import numpy as np
import pickle 
from sklearn.base import ClassifierMixin

from flask import current_app

model_path = os.path.join('/home/riri/Desktop/Soiling/src/models', 'catboost.pkl')
with open(model_path, 'rb') as path:
    model = pickle.load(path)

def predict_input(inputs, model: ClassifierMixin=model):
    labels = {0: 'No', 1: 'Yes'}

    # inputs = np.array(inputs)

    prediction = model.predict(inputs)
    probabilities = np.max(model.predict_proba(inputs))
    probability = np.round(probabilities * 100, 2)

    prediction = [int(label) for label in prediction]

    prediction = [labels[label] for label in prediction][0]
    
    return prediction, probability


def predict_time(inputs, model: ClassifierMixin=model):
    prediction = model.predict(inputs)
    return np.random.randint(1, 60)
