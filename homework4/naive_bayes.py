'''
Sam Chami
Jackson Myers
John Scott
Ben Smith

naive_bayes.py
'''

import unittest
import csv
import numpy as np
import pandas as pd
import scipy
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.impute import SimpleImputer


class NaiveBayesClassifier:
    """

    """
    np.set_printoptions(threshold=np.nan)

    original_data = pd.read_csv("income-test.csv", na_values = ['?'])


    imp = SimpleImputer(missing_values='?', strategy='most_frequent')
    data = pd.DataFrame(imp.fit_transform(original_data))
    print(data)

    enc = preprocessing.OrdinalEncoder(dtype="object").fit(data)
    data = enc.transform(data)

    bin = preprocessing.KBinsDiscretizer(encode="ordinal", strategy="quantile").fit(data)
    data = bin.transform(data)




    def __init__(self):
        """

        """

class NaiveBayesClassifierTests(unittest.TestCase):
    """Unit Tests"""


if __name__ == "__main__":
    unittest.main()
