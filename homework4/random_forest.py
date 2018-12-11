'''
Sam Chami
Jackson Myers
John Scott
Ben Smith

random_forest.py
'''

import unittest
import numpy as np
import pandas as pd
import scipy
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

class RandomForest:
    """

    """

    def preprocess(file_name):
        """
        Preprocesses the data for the NBC so that it is properly formatted for our training model.
        """
        names = ("age", "wrk_cls", "edu", "edu_num", "marital_sts", "occu_code",
                 "relation", "race", "sex", "gain", "loss", "hours", "country", "income")

        original_data = pd.read_csv(file_name, dtype=object, names=names)
        original_data = pd.DataFrame(original_data)

        imp = SimpleImputer(missing_values=' ?', strategy='most_frequent', verbose=1)
        data = imp.fit_transform(original_data)

        enc = preprocessing.OrdinalEncoder()
        data = enc.fit_transform(data)

        est = preprocessing.KBinsDiscretizer(encode="ordinal")
        data = est.fit_transform(data)

        return data

    def train_model(data):
        X, y = make_classification(n_samples=1000, n_features=4,
                                   n_informative=2, n_redundant=0,
                                   random_state=0, shuffle=False)

        # X = RandomForest.preprocess("income-training.csv")
        # y = RandomForest.preprocess("income-test.csv")

        print(X)
        print(y)

        clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
        clf.fit(X,y)

        print(clf.feature_importances_)
        print(clf.predict([[0, 0, 0, 0]]))


class RandomForestTests(unittest.TestCase):
    """Unit Tests"""
    def test(self):
        """
        Train agent using income-training data and test accuracy of agent on income-test data.
        """
        processed_training_data = RandomForest.preprocess("income-training.csv")
        processed_test_data = RandomForest.preprocess("income-test.csv")

        trained_model = RandomForest.train_model(processed_training_data)



if __name__ == "__main__":
    unittest.main()
