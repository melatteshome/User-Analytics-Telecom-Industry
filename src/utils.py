import pandas as pd
import numpy as np
from scipy import stats

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

def remove_outliers(df, col, threshold=3):
    """
    Removes outliers from a DataFrame column using the Z-score method.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    col (str): The column name from which to remove outliers.
    threshold (float): The Z-score threshold to use for identifying outliers.

    Returns:
    pd.DataFrame: A DataFrame with outliers removed.
    """
    z_scores = stats.zscore(df[col])
    abs_z_scores = abs(z_scores)
    filtered_entries = abs_z_scores < threshold

    return df[filtered_entries]



    
# def check_for_outliers()





