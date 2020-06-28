import pandas as pd
import numpy as np

from IPython.core.display import HTML


def null_values(df):
    """Null values summary

    Args:
        df (pandas df): 

    Returns:
        [pandas df]: Table of null values containing count of missing values  and % of total for each column
    """
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    return mis_val_table_ren_columns

