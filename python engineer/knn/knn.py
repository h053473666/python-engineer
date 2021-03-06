# -*- coding: utf-8 -*-
"""knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zOUlENSo2-s72WBjv-F5DL4jVwYHrW7y
"""

import numpy as np
from collections import Counter

def euclidiean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:

    def __init__(self, k=3):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predicted(x) for x in X]
        return np.array(predicted_labels)
    
    def _predicted(self, x):
        distance = [euclidiean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distance)[:self.k]
        k_nearest_laybels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_laybels).most_common(1)
        return most_common[0][0]

