import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from pandas import read_csv
from pandas import concat
from pandas import DataFrame
from scipy.interpolate import UnivariateSpline
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pickle

from mealclassifier import MealClassifier

class TestMealClassifier():

    def __init__(self):
        print("Testing Meal Classifier ...")

    # Imports saved model
    # Converts test data to reduced feature matrix
    # Labels test data and saves to file
    def test_model(self):

        meal_classifier = MealClassifier()
        model_path = meal_classifier.OUTPUT_PATH_MODEL
        file_path = input('Please enter the data set directory path\n')
        final = pd.read_csv(file_path, header=None)
        final = final.iloc[:, ::-1].astype(int)
        # print(final)
        feature_df = meal_classifier.extract_features(final)
        reduced_feature_df = meal_classifier.reduce_dimensions(feature_df)
        # print(reduced_feature_df)
        loaded_model = pickle.load(open(model_path, 'rb'))
        result = loaded_model.predict(reduced_feature_df)
        # results
        print(result)



        print("Testing Meal Classifier ... DONE.")

if __name__ == '__main__':
    test_meal_classifier = TestMealClassifier()
    test_meal_classifier.test_model()