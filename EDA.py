import pandas as pd
import numpy as np
import category_encoders as ce
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from IPython.core.display import HTML




def null_values(df):
    """Null values summary

    Args:
        df (pd.DataFrame): 

    Returns:
        [pd.DataFrame]: Table of null values containing count of missing values  and % of total for each column
    """
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    mis_val_table_ren_columns.sort_values(by = '% of Total Values',ascending = False,inplace = True)
    return mis_val_table_ren_columns


def woe_discrete(df,discrete_variable_name,target):
    """Generates woe transformation of discrete variables

    Args:
        df (pd.Dataframe): dataframe containing discrete variables to be trnasformed
        discrete_variable_name (list): list of discrete variables to be transformed
        target (str): target variable name

    Returns:
        pd.Dataframe: dataframe with woe transformed discrete variables added as columns to the original dataframe
    """


    woe_encoder = ce.WOEEncoder(cols=discrete_variable_name)
    woe_of_discrete_variables = woe_encoder.fit_transform(df[discrete_variable_name], df[target]).add_suffix('_woe')
    df = df.join(woe_of_discrete_variables)
    return df


def woe_table(df,variable_name,rotation_of_x_axis_labels = 0,variable_type = 'discrete'):
    """Generates weight of evidence plots for a given variabe

    Args:
        df (pd.DataFrame): dataframe containing variable for WoE plot
        variable_name (str): variable for WoE
        rotation_of_x_axis_labels (int, optional): . Defaults to 0.
        variable_type (str, optional): . Defaults to 'discrete'.
    """

    


    df_WoE = df.groupby(variable_name,as_index = False).agg({variable_name+'_woe':['mean','count']})
    df_WoE.columns = [variable_name,'WoE','nobs']

    if variable_type == 'discrete':
        df_WoE.sort_values(by = 'WoE',inplace = True)
    else:
        pass

    
    return df_WoE

    
    
def woe_discrete_plot(df,rotation_of_x_axis_labels=0):
    """Generate woe plot for a discrte variable

    Args:
        df (pd.DataFrame): dataframe containing woe values for each category in a discrete variable
        rotation_of_x_axis_labels (int, optional): [description]. Defaults to 0.

    Returns:
        [None]: [description]
    """
    
    
    x = np.array(df.iloc[:,0].apply(str))
    y = df['WoE']
    plt.figure(figsize = (18,6))
    plt.plot(x,y, marker = 'o', linestyle = '--', color = 'k')
    plt.xlabel(df.columns[0])
    plt.ylabel('Weight of evidence')
    plt.title(str('Weight of Evidence by ' + df.columns[0]))
    plt.xticks(rotation = rotation_of_x_axis_labels)

    return None




















