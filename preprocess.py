import pandas as pd
import numpy as np


def object_to_date(df,columns):
    """Convert date strings to pandas datetime objects

    Args:
        df (pandas df): dataframe 
        columns (list): list of columns to convert

    Returns:
        [pandas df]: dataframe with datetime columns added
    """
    
    for col in columns:
        new_col_name = col + "_date"
        df[new_col_name] = pd.to_datetime(df[col], format = "%b-%Y")
    return df

def drop_columns(df):
    """drop columns

    Args:
        df (pandas df): [description]

    Returns:
        [pandas df]: dataframe with columns dropped 
    """

    #secondary applicant columns
    sec_cols = [col for col in list(df.columns) if col.find('sec_') != -1]
    # columns containing combined metrics for joint app
    joint_cols = [col for col in list(df.columns) if col.find('_joint') != -1]
    # hardship columns
    hardship_cols = [col for col in list(df.columns) if col.find('hardship_') != -1]
    #debt settlement columns
    settlement_cols = [col for col in list(df.columns) if col.find('settlement_') != -1]
    #other columns
    other_columns = ['id','member_id','url']

    df.drop(hardship_cols,axis = 1,inplace = True)
    df.drop(settlement_cols, axis = 1,inplace = True)
    df.drop(sec_cols,axis = 1,inplace = True)
    df.drop(joint_cols, axis = 1,inplace = True)
    df.drop(other_columns, axis = 1,inplace = True)

    return df


def emp_length_to_numeric(df):
    """Converts emp_length from string to numeric

    Args:
        df (pandas df):

    Returns:
        pandas df: emp_length is a numeric variable 
    """

    df.loc[df['emp_length'] == '< 1 year','emp_length'] = '0 years'
    df.loc[df['emp_length'] == '10+ years','emp_length'] = '10 years'
    is_emp_length_null = df['emp_length'].isnull()
    df.loc[~is_emp_length_null,'emp_length'] = df['emp_length'][~is_emp_length_null].map(lambda x: int(x.split(' ')[0]))
    df['emp_length'] = df['emp_length'].astype(float)
    return df


def vintage_selection_for_modeling(df):
    """selects vintages to keep in the dataset

    Args:
        df (pandas df): [description]

    Returns:
        pandas df: dataset after selection
    """

    is_mature_36_months = (df['issue_d_date'].dt.year < 2018) & (df['term'] == ' 36 months')
    is_mature_60_months = (df['issue_d_date'].dt.year < 2016) & (df['term'] == ' 60 months')
    df = df[is_mature_36_months|is_mature_60_months]
    return df

def good_bad_definition(target):
    """assigns good bad status to loans

    Args:
        target (pd.Series): contains target values

    Returns:
        pd.Series: contains good and bad labels (good = 1, bad = 0)
    """


    bads = ['Charged Off','Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)']
    target_good_bad = np.where(target.isin(bads),0,1)
    return target_good_bad



























    