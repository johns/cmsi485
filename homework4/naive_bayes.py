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
import scipy
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.impute import SimpleImputer


class NaiveBayesClassifier:
    """

    """
    # with open('income-training.csv') as csv_file:
    #     data = list(csv.reader(csv_file, delimiter=','))

    data = np.loadtxt(open("income-training.csv"), delimiter=",", dtype="object")

    imp = SimpleImputer(missing_values="?", strategy='most_frequent').fit(data)
    data = imp.transform(data)

    enc = preprocessing.OrdinalEncoder(dtype="object").fit(data)
    data = enc.transform(data)

    bin = preprocessing.KBinsDiscretizer(encode="ordinal", strategy="quantile").fit(data)
    data = bin.transform(data)

    print(data)




    def __init__(self):
        """

        """

class NaiveBayesClassifierTests(unittest.TestCase):
    """Unit Tests"""


if __name__ == "__main__":
    unittest.main()
