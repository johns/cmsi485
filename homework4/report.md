#  Homework 4: Ridiculously Good Looking Models
####  Sam Chami, Jackson Myers, John Scott, and Ben Smith

## How did we preprocess the data?
Read csv file with pandas read_csv(), which also eliminated leading whitespaces. That was turned into a pandas data frame. We used SimpleImputer from sklearn to replace missing values with the most frequent value in the feature. We encoded the data with the OrdinalEncoder then used KBinsDiscretizer to transform continuous values to discrete values.

## Naive Bayes Classifier
##### What hyper parameters did we set?
For the SimpleImputer we used the following parameters: missing_value="?", strategy="most_frequent", verbose=2(because when =0 it did not replace all "?")

For KBinsDiscretizer n_bins=7, encode=ordinal

No additional hyperparameters were applied for training


##### What was our resulting classification accuracy?
77.89% Accuracy

## Decision Trees
##### What hyper parameters did we set?
For KBinsDiscretizer n_bins=8

##### What was our resulting classification accuracy?
81.15% Accuracy


## Random Forest
##### What hyper parameters did we set?
For KBinsDiscretizer n_bins=5(default)

For training the RandomForest we used the following parameters:
n_estimators=45, max_depth=10, random_state=0

##### What was our resulting classification accuracy?
83.16% Accuracy
