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
from sklearn.naive_bayes import BernoulliNB
from sklearn.impute import SimpleImputer


class NaiveBayesClassifier:
    """

    """
    #np.set_printoptions(threshold=np.nan)
    names = ("age", "wrk_cls", "educ", "educ_num", "marital_sts", "occu_code", "realtion", "race", "sex", "gain", "loss", "hours", "country", "income")


    original_data = pd.read_csv("income-training.csv", dtype=object, names=names)
    original_data = pd.DataFrame(original_data)

    imp = SimpleImputer(missing_values=' ?', strategy='most_frequent', verbose=1)
    data = imp.fit_transform(original_data)

    enc = preprocessing.OneHotEncoder()
    data = enc.fit_transform(data)
    print(data.toarray())

    classifier = BernoulliNB()
    classifier.fit(data, income-test.csv)


    def __init__(self):
        """

        """

class NaiveBayesClassifierTests(unittest.TestCase):
    """Unit Tests"""


if __name__ == "__main__":
    unittest.main()
