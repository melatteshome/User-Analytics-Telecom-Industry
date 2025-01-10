import pandas as pd
import numpy as np

def check_duplicates(df):
    duplicates = df.duplicated()

    if duplicates.any():
        return df[duplicates]
    else:
        return 'no duplicates found'
    

def check_missing_values(df):
    missing_values = df.isnull().sum()

    missing_values_datatype =  df.dtypes[missing_values > 0]

    missing_values_percentage = missing_values[missing_values > 0] / df.shape[0] * 100

    missing_values_info = pd.DataFrame({
        'missing_values': missing_values[missing_values > 0],
        'missing_values_percentage': missing_values_percentage,
        'datatype': missing_values_datatype
    })

    return missing_values_info

def filter_numerical_columns(df):
    return df.select_dtypes(include= [np.number])

def remove_outliers(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return df[(df[col] > lower_bound) & (df[col] < upper_bound)]



    
# def check_for_outliers()





