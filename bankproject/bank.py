#!/bin/python

#Bank Project - Chris Spencer

import pandas
#import sciPy
#import numPy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import average_precision_score, recall_score

data = pandas.read_csv("bank-additional-full.csv", sep=';')
del data['duration'] #dont need it

y = data['y'] #pull col y from data
del data['y'] #delete y in original dataset

y = y.apply(lambda x: int(x == 'yes')) #convert y to bit field

#The following takes the categorical fields and makes them simply ints
le = preprocessing.LabelEncoder()

data['job'] = le.fit_transform(data['job'])
data['marital'] = le.fit_transform(data['marital'])
data['education'] = le.fit_transform(data['education'])
data['default'] = le.fit_transform(data['default'])
data['housing'] = le.fit_transform(data['housing'])
data['loan'] = le.fit_transform(data['loan'])
data['contact'] = le.fit_transform(data['contact'])
data['month'] = le.fit_transform(data['month'])
data['day_of_week'] = le.fit_transform(data['day_of_week'])
data['poutcome'] = le.fit_transform(data['poutcome'])

t = .75 #TODO: mess with train_size
data_training, data_test, y_training, y_test = train_test_split(data, y, train_size = t, random_state=1)

ne = 100 #TODO: mess with n_estimators 
rand_forest = RandomForestClassifier(n_estimators=ne)
rand_forest.fit(data_training, y_training)

prediction = rand_forest.predict(data_test)

accuracy = rand_forest.score(data_test, y_test)
precision = average_precision_score(y_test, prediction)
recall = recall_score(y_test, prediction)

print("For train_size= ", t, " and n_estimators= ", ne)
print('Accuracy:', accuracy * 100)
print('Precision:', precision * 100)
print('Recall:', recall * 100)

