#! /usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""

__all__ = ['BaseModel']

__version__ = "0.1.0.0"
__author__ = "Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"
__maintainers__ = ["Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"]

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class BaseModel:

    score_card = pd.DataFrame(columns=['Algorithm', 'Mean Absolute Error', 'Mean Squared Error', 'Root Mean Squared Error', 'R-squared'])

    def __init__(self, name):
        self.name = name
        self.model = None

    def train(self, X_train, y_train):
        # Placeholder for training logic
        print(f"Training {self.name} model...", flush=True)

    def predict(self, X_test):
        # Placeholder for prediction logic
        print(f"Predicting with {self.name} model...")

    def evaluate(self, y_true, y_pred):
        # Placeholder for evaluation logic
        print(f"Evaluating with {self.name} model...")
        return metrics.accuracy_score(y_true, y_pred)

    def display_summary(self):
        return self.model.summary()

    @classmethod
    def update_score_card(cls, name, y_test, y_pred):
        new_scores = {
            'Algorithm': name,
            'Mean Absolute Percentage Error': metrics.mean_absolute_percentage_error(y_test, y_pred),
            'Root Mean Squared Error': np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
            'Mean Absolute Error': metrics.mean_absolute_error(y_test, y_pred)
        }
        new_row = pd.DataFrame([new_scores])

        cls.score_card = pd.concat([cls.score_card, new_row], ignore_index=True)

    @classmethod
    def display_score_card(cls):
        print(cls.score_card)

    def plot_bias_variance(self, X, y, test_size=0.2, random_state=None):
        train_errors = []
        test_errors = []
        train_sizes = []

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        for i in range(10, len(X_train) + 1, 10):
            train_sizes.append(i)
            self.train(X_train[:i], y_train[:i])

            train_pred = self.predict(X_train[:i])
            test_pred = self.predict(X_test)

            train_error = metrics.mean_squared_error(y_train[:i], train_pred)
            test_error = metrics.mean_squared_error(y_test, test_pred)

            train_errors.append(train_error)
            test_errors.append(test_error)

        plt.figure(figsize=(10, 6))
        plt.plot(train_sizes, train_errors, label='Train Mean Squared Error')
        plt.plot(train_sizes, test_errors, label='Test Mean Squared Error')
        plt.xlabel('Training Size')
        plt.ylabel('Mean Squared Error')
        plt.title('Bias-Variance Tradeoff: Mean Squared Error vs Training Size')
        plt.legend()
        plt.show()
