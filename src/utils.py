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



    
# def check_for_outliers()





