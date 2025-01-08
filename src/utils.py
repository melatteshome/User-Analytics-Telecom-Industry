import pandas as pd
import numpy as np

def check_duplicates(df):
    duplicates = df.duplicated()

    if duplicates.any():
        return df[duplicates]
    else:
        return 'no duplicates found'




