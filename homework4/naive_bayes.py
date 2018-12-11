'''
Sam Chami
Jackson Myers
John Scott
Ben Smith

naive_bayes.py
'''

import unittest
import numpy as np
import pandas as pd
import scipy
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.impute import SimpleImputer


class NaiveBayesClassifier:

    def preprocess(file_name):
        names = ("age", "wrk_cls", "edu", "edu_num", "marital_sts", "occu_code", "relation", "race", "sex", "gain", "loss", "hours", "country", "income")

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
        X, Y = data[:, :-1], data[:, -1]
        print(X)
        print(Y)

        classifier = MultinomialNB()
        classifier.fit(X, Y)
        return classifier


class NaiveBayesClassifierTests(unittest.TestCase):
    def test(self):

        processed_training_data = NaiveBayesClassifier.preprocess("income-training.csv")
        processed_test_data = NaiveBayesClassifier.preprocess("income-test.csv")

        trained_model = NaiveBayesClassifier.train_model(processed_training_data)
        print(trained_model.predict(processed_test_data))


if __name__ == "__main__":
    unittest.main()
