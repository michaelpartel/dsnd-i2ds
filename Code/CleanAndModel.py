import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

#Data cleaning function based on lessons from Udacity "Introduction to Data Science"
#The function, clean_fit_linear_mod(...) below is primarily based on the same-purpose
# function from the final notebook "Putting It All Together".
def clean_data(df, response_col_name):
    '''
    INPUT
    df - pandas dataframe
    response_col_name - String name of the response column

    OUTPUT
    X - A matrix holding all of the variables you want to consider when predicting the response
    y - the corresponding response vector

    This function cleans df using the following steps to produce X and y:
    1. Drop the rows that are missing a response.
    2. Split off the response column as y
    3. Remove unnecessary columns from the df that will become X.
    4. Impute the NANs of the numeric columns with the mean for the column.
    5. Replace the categorical columns with Dummy variables.
    '''
    #Drop rows with NANs in the response column.
    df = df.dropna(subset=[response_col_name], axis=0)

    #Assign y as only the response column.
    y = df[response_col_name]

    #Remove the response column and other unnecessary columns from the rest of the data.
    df = df.drop([response_col_name, 'TODO - OTHER COLUMNS'], axis=1)

    #Determine then numeric columns and replace any NANs with the mean for the column.
    num_cols = df.select_dtypes(include=['float', 'int']).columns
    for col in num_cols:
        df[col].fillna((df[col].mean()), inplace=True)

    #Replace the categorical columns with dummy variable columns.
    cat_cols = df.select_dtypes(include=['object']).copy().columns
    for col in  cat_cols:
        #Drop the original category column from df and concat with the new dummies.
        df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True)], axis=1)

    X = df
    return X, y
#End of clean_data

#Use the function to create X and y
#X, y = clean_data(df)
