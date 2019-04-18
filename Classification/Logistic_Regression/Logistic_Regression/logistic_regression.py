# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[: , 4].values

# Splitting dataset to training and testing set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

 # Fitting Logistic Regression to the training set
 from sklearn.linear_model import LogisticRegression
 classifier = LogisticRegression(random_state = 0)
 classifier.fit(X_train, y_train)
 
 # predicting the test set results
 y_pred = classifier.predict(X_test)
 
 # Making the Confusion Matrix
 from sklearn.metrics import confusion_matrix
 cm = confusion_matrix(y_test, y_pred)
 
  
 