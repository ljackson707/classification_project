#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import acquire

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For Telco data

def prep_telco_data(df):
    df = df
    df = rename_columns(df)
    dummy_df = pd.get_dummies(df[["internet_service"]], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    dummy_df2 = pd.get_dummies(df[["gender"]], drop_first=True)
    df = pd.concat([df, dummy_df2], axis=1)
    dummy_df3 = pd.get_dummies(df[["payment_method", "contract"]], drop_first=True)
    df = pd.concat([df, dummy_df3], axis=1)
    dummy_df4 = pd.get_dummies(df[["partner", "dependents", "phone_service", "multiple_lines",
                                    "online_security",'online_backup', 'device_protection','Churn',
                                    'tech_support','streaming_movies','streaming_tv','paperless_billing']], drop_first=True)
    df = pd.concat([df, dummy_df4], axis=1)
    df = remove_columns(df)
    return (df)

def rename_columns(df):
    return df.rename(columns={'customerID':'customer_id',
                                'SeniorCitizen':'senior_citizen',
                                'Partner':'partner',
                                'Dependents':'dependents',
                                'PhoneService':'phone_service',
                                'MultipleLines':'multiple_lines',
                                'InternetService':'internet_service',
                                'OnlineSecurity':'online_security',
                                'StreamingTV':'streaming_tv',
                                'StreamingMovies':'streaming_movies',
                                'Contract':'contract',
                                'PaperlessBilling':'paperless_billing',
                                'PaymentMethod':'payment_method',
                                'MonthlyCharges':'monthly_charges',
                                'TotalCharges':'total_charges',
                                'OnlineBackup':'online_backup',
                                'DeviceProtection':'device_protection',
                                'TechSupport':'tech_support'})

def remove_columns(df):
    return df.drop(columns=['internet_service', 'gender', 'payment_method', 'contract',"partner", "dependents", "phone_service", "multiple_lines",
                            "online_security",'online_backup', 'device_protection','Churn','tech_support','streaming_movies','streaming_tv','paperless_billing','monthly_charges', 'total_charges'])

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test

    
def data_target_split(data_set):
    '''
    Accepts a DataFrame set to train a ML model
    Returns X_train/validation/test set, with y_train/validate/test 
    '''
    
    data = data_set.drop(columns='Churn_Yes')
    target = data_set[['Churn_Yes']]

    return data, target