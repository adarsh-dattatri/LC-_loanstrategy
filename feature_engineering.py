import numpy as np
import pandas as pd

def get_dummies(df,variable_name,sep = '_'):
    """Creates dummies for a given variable

    Args:
        df (pd.Dataframe): dataframe containing the variable 
        variable_name (str): variable to be transformed to dummies
        sep (str, optional): prefix separator for dummy variable names. Defaults to '_'.

    Returns:
        pd.DataFrame: Original dataframe with dummy variables appended
    """

    df = pd.get_dummies(df,columns = [variable_name],prefix_sep= sep)
    return df


def generate_col_names_for_deletion(columns,prefix,prefix_sep='_'):

    dummy_column_names = [prefix+prefix_sep+col for col in columns]
    return dummy_column_names

def coarse_class_discrete_variables(df):
    """Corse classing and dummy variable creation for discrete variables

    Args:
        df (pd.DataFrame):

    Returns:
        [pd.DataFrame]: dataframe with dummy variables appended
    """

    df['addr_state:IA_MS'] = df['addr_state_IA'] +  df['addr_state_MS']
    columns = generate_col_names_for_deletion(['IA','MS'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:AR_AL_NV_NE_OK'] = df['addr_state_AR'] + df['addr_state_AL'] + df['addr_state_NV'] + df['addr_state_NE'] + df['addr_state_OK']
    columns = generate_col_names_for_deletion(['AR','AL','NV','NE','OK'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:FL_TN'] = df['addr_state_FL'] + df['addr_state_TN']
    columns = generate_col_names_for_deletion(['FL','TN'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:NY_NM'] = df['addr_state_NY'] + df['addr_state_NM']
    columns = generate_col_names_for_deletion(['NY','NM'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:HI_MD_IN_NJ_KY_NC_PA'] = df['addr_state_HI'] + df['addr_state_MD'] + df['addr_state_IN'] + df['addr_state_NJ'] + df['addr_state_KY'] + df['addr_state_NC'] + df['addr_state_PA']
    columns = generate_col_names_for_deletion(['HI','MD','IN','NJ','KY','NC','PA'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:CA_MI_AZ_VA'] = df['addr_state_CA'] + df['addr_state_MI'] + df['addr_state_AZ'] + df['addr_state_VA']
    columns = generate_col_names_for_deletion(['CA','MI','AZ','VA'],'addr_state') 
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:DE_MN_AK'] = df['addr_state_DE'] + df['addr_state_MN'] + df['addr_state_AK']
    columns = generate_col_names_for_deletion(['DE','MN','AK'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:MA_UT_RI_ND_ID_GA'] = df['addr_state_MA'] + df['addr_state_UT'] + df['addr_state_RI'] + df['addr_state_ND'] + df['addr_state_ID'] + df['addr_state_GA']
    columns = generate_col_names_for_deletion(['MA','UT','RI','ND','ID','GA'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:IL_WI'] = df['addr_state_IL'] + df['addr_state_WI']
    columns = generate_col_names_for_deletion(['IL','WI'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:WA_CT'] = df['addr_state_WA'] + df['addr_state_CT']
    columns = generate_col_names_for_deletion(['WA','CT'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['addr_state:SC_WV_CO_WY_KS'] = df['addr_state_SC'] + df['addr_state_WV'] + df['addr_state_CO'] + df['addr_state_WY'] + df['addr_state_KS']
    columns = generate_col_names_for_deletion(['SC','WV','CO','WY','KS'],'addr_state')
    df.drop(columns, axis = 1, inplace = True)
    
    df['home_ownership:OTHER_RENT'] = df['home_ownership_OTHER'] + df['home_ownership_RENT']
    columns = generate_col_names_for_deletion(['OTHER','RENT'],'home_ownership')
    df.drop(columns, axis = 1, inplace = True)

    df['home_ownership:NONE_ANY_OWN'] = df['home_ownership_NONE'] + df['home_ownership_ANY'] + df['home_ownership_OWN']
    columns = generate_col_names_for_deletion(['NONE','ANY','OWN'],'home_ownership')
    df.drop(columns, axis = 1, inplace = True)
    
    df['sub_grade:G5_G3_G1_G2_F5_G4'] = df['sub_grade_G5'] + df['sub_grade_G3'] + df['sub_grade_G1'] + df['sub_grade_G2'] + df['sub_grade_F5'] + df['sub_grade_G4']
    columns = generate_col_names_for_deletion(['G5','G3','G1','G2','F5','G4'],'sub_grade')
    df.drop(columns, axis = 1, inplace = True)
    
    df['purpose:ed_re_mo_ho'] = df['purpose:educational'] + df['purpose:renewable_energy'] + df['purpose:moving'] + df['purpose:house']
    columns = generate_col_names_for_deletion(['educational','renewable_energy','moving','house'],'purpose',prefix_sep = ':')
    df.drop(columns, axis = 1, inplace = True)
    
    df['purpose:mp_hi'] = df['purpose:major_purchase'] + df['purpose:home_improvement']
    columns = generate_col_names_for_deletion(['major_purchase','home_improvement'],'purpose',prefix_sep = ':')
    df.drop(columns, axis = 1, inplace = True)
    
    df['purpose:wedding_car'] = df['purpose:wedding'] + df['purpose:car']
    columns = generate_col_names_for_deletion(['wedding','car'],'purpose',prefix_sep = ':')
    df.drop(columns, axis = 1, inplace = True)
    
    return df



def coarse_class_continuous_variables(df):
    """Corse classing and dummy variable creation for continuous variables

    Args:
        df (pd.DataFrame):

    Returns:
        [pd.DataFrame]: dataframe with dummy variables appended
    """


    
    df['emp_length:0'] = np.where(df['emp_length'].isin([0]), 1, 0)
    df['emp_length:1'] = np.where(df['emp_length'].isin([1]), 1, 0)
    df['emp_length:2-4'] = np.where(df['emp_length'].isin(range(2, 5)), 1, 0)
    df['emp_length:5-6'] = np.where(df['emp_length'].isin(range(5, 7)), 1, 0)
    df['emp_length:7-9'] = np.where(df['emp_length'].isin(range(7, 10)), 1, 0)
    df['emp_length:10'] = np.where(df['emp_length'].isin([10]), 1, 0)
    df.drop('emp_length',axis = 1, inplace = True)
    


    df['int_rate:<9.548'] = np.where((df['int_rate'] <= 9.548), 1, 0)
    df['int_rate:9.548-12.025'] = np.where((df['int_rate'] > 9.548) & (df['int_rate'] <= 12.025), 1, 0)
    df['int_rate:12.025-15.74'] = np.where((df['int_rate'] > 12.025) & (df['int_rate'] <= 15.74), 1, 0)
    df['int_rate:15.74-20.281'] = np.where((df['int_rate'] > 15.74) & (df['int_rate'] <= 20.281), 1, 0)
    df['int_rate:>20.281'] = np.where((df['int_rate'] > 20.281), 1, 0)
    df.drop('int_rate',axis = 1, inplace = True)


    df['mths_since_earliest_cr_line:<140'] = np.where(df['mths_since_earliest_cr_line'].isin(range(140)), 1, 0)
    df['mths_since_earliest_cr_line:141-164'] = np.where(df['mths_since_earliest_cr_line'].isin(range(140, 165)), 1, 0)
    df['mths_since_earliest_cr_line:165-247'] = np.where(df['mths_since_earliest_cr_line'].isin(range(165, 248)), 1, 0)
    df['mths_since_earliest_cr_line:248-270'] = np.where(df['mths_since_earliest_cr_line'].isin(range(248, 271)), 1, 0)
    df['mths_since_earliest_cr_line:271-352'] = np.where(df['mths_since_earliest_cr_line'].isin(range(271, 353)), 1, 0)
    df['mths_since_earliest_cr_line:>352'] = np.where(df['mths_since_earliest_cr_line'].isin(range(353, int(df['mths_since_earliest_cr_line'].max()))), 1, 0)
    df.drop('mths_since_earliest_cr_line',axis = 1, inplace = True)

    df['delinq_2yrs:0'] = np.where((df['delinq_2yrs'] == 0), 1, 0)
    df['delinq_2yrs:1-3'] = np.where((df['delinq_2yrs'] >= 1) & (df['delinq_2yrs'] <= 3), 1, 0)
    df['delinq_2yrs:>=4'] = np.where((df['delinq_2yrs'] >= 9), 1, 0)
    df.drop('delinq_2yrs',axis = 1, inplace = True)

    df['inq_last_6mths:0'] = np.where((df['inq_last_6mths'] == 0), 1, 0)
    df['inq_last_6mths:1-2'] = np.where((df['inq_last_6mths'] >= 1) & (df['inq_last_6mths'] <= 2), 1, 0)
    df['inq_last_6mths:3-6'] = np.where((df['inq_last_6mths'] >= 3) & (df['inq_last_6mths'] <= 6), 1, 0)
    df['inq_last_6mths:>6'] = np.where((df['inq_last_6mths'] > 6), 1, 0)
    df.drop('inq_last_6mths',axis = 1, inplace = True)

    df['open_acc:0'] = np.where((df['open_acc'] == 0), 1, 0)
    df['open_acc:1-3'] = np.where((df['open_acc'] >= 1) & (df['open_acc'] <= 3), 1, 0)
    df['open_acc:4-12'] = np.where((df['open_acc'] >= 4) & (df['open_acc'] <= 12), 1, 0)
    df['open_acc:13-17'] = np.where((df['open_acc'] >= 13) & (df['open_acc'] <= 17), 1, 0)
    df['open_acc:18-22'] = np.where((df['open_acc'] >= 18) & (df['open_acc'] <= 22), 1, 0)
    df['open_acc:23-25'] = np.where((df['open_acc'] >= 23) & (df['open_acc'] <= 25), 1, 0)
    df['open_acc:26-30'] = np.where((df['open_acc'] >= 26) & (df['open_acc'] <= 30), 1, 0)
    df['open_acc:>=31'] = np.where((df['open_acc'] >= 31), 1, 0)
    df.drop('open_acc',axis = 1, inplace = True)



    df['pub_rec:0-2'] = np.where((df['pub_rec'] >= 0) & (df['pub_rec'] <= 2), 1, 0)
    df['pub_rec:3-4'] = np.where((df['pub_rec'] >= 3) & (df['pub_rec'] <= 4), 1, 0)
    df['pub_rec:>=5'] = np.where((df['pub_rec'] >= 5), 1, 0)
    df.drop('pub_rec',axis = 1, inplace = True)

    df['total_acc:<=27'] = np.where((df['total_acc'] <= 27), 1, 0)
    df['total_acc:28-51'] = np.where((df['total_acc'] >= 28) & (df['total_acc'] <= 51), 1, 0)
    df['total_acc:>=52'] = np.where((df['total_acc'] >= 52), 1, 0)
    df.drop('total_acc',axis = 1, inplace = True)


    df['annual_inc:<20K'] = np.where((df['annual_inc'] <= 20000), 1, 0)
    df['annual_inc:20K-30K'] = np.where((df['annual_inc'] > 20000) & (df['annual_inc'] <= 30000), 1, 0)
    df['annual_inc:30K-40K'] = np.where((df['annual_inc'] > 30000) & (df['annual_inc'] <= 40000), 1, 0)
    df['annual_inc:40K-50K'] = np.where((df['annual_inc'] > 40000) & (df['annual_inc'] <= 50000), 1, 0)
    df['annual_inc:50K-60K'] = np.where((df['annual_inc'] > 50000) & (df['annual_inc'] <= 60000), 1, 0)
    df['annual_inc:60K-70K'] = np.where((df['annual_inc'] > 60000) & (df['annual_inc'] <= 70000), 1, 0)
    df['annual_inc:70K-80K'] = np.where((df['annual_inc'] > 70000) & (df['annual_inc'] <= 80000), 1, 0)
    df['annual_inc:80K-90K'] = np.where((df['annual_inc'] > 80000) & (df['annual_inc'] <= 90000), 1, 0)
    df['annual_inc:90K-100K'] = np.where((df['annual_inc'] > 90000) & (df['annual_inc'] <= 100000), 1, 0)
    df['annual_inc:100K-120K'] = np.where((df['annual_inc'] > 100000) & (df['annual_inc'] <= 120000), 1, 0)
    df['annual_inc:120K-140K'] = np.where((df['annual_inc'] > 120000) & (df['annual_inc'] <= 140000), 1, 0)
    df['annual_inc:>140K'] = np.where((df['annual_inc'] > 140000), 1, 0)
    df.drop('annual_inc',axis = 1, inplace = True)

    df['mths_since_last_delinq:Missing'] = np.where((df['mths_since_last_delinq'].isnull()), 1, 0)
    df['mths_since_last_delinq:0-3'] = np.where((df['mths_since_last_delinq'] >= 0) & (df['mths_since_last_delinq'] <= 3), 1, 0)
    df['mths_since_last_delinq:4-30'] = np.where((df['mths_since_last_delinq'] >= 4) & (df['mths_since_last_delinq'] <= 30), 1, 0)
    df['mths_since_last_delinq:31-56'] = np.where((df['mths_since_last_delinq'] >= 31) & (df['mths_since_last_delinq'] <= 56), 1, 0)
    df['mths_since_last_delinq:>=57'] = np.where((df['mths_since_last_delinq'] >= 57), 1, 0)
    df.drop('mths_since_last_delinq',axis = 1, inplace = True)


    df['dti:<=1.4'] = np.where((df['dti'] <= 1.4), 1, 0)
    df['dti:1.4-3.5'] = np.where((df['dti'] > 1.4) & (df['dti'] <= 3.5), 1, 0)
    df['dti:3.5-7.7'] = np.where((df['dti'] > 3.5) & (df['dti'] <= 7.7), 1, 0)
    df['dti:7.7-10.5'] = np.where((df['dti'] > 7.7) & (df['dti'] <= 10.5), 1, 0)
    df['dti:10.5-16.1'] = np.where((df['dti'] > 10.5) & (df['dti'] <= 16.1), 1, 0)
    df['dti:16.1-20.3'] = np.where((df['dti'] > 16.1) & (df['dti'] <= 20.3), 1, 0)
    df['dti:20.3-21.7'] = np.where((df['dti'] > 20.3) & (df['dti'] <= 21.7), 1, 0)
    df['dti:21.7-22.4'] = np.where((df['dti'] > 21.7) & (df['dti'] <= 22.4), 1, 0)
    df['dti:22.4-35'] = np.where((df['dti'] > 22.4) & (df['dti'] <= 35), 1, 0)
    df['dti:>35'] = np.where((df['dti'] > 35), 1, 0)
    df.drop('dti',axis = 1, inplace = True)


    df['mths_since_last_record:Missing'] = np.where((df['mths_since_last_record'].isnull()), 1, 0)
    df['mths_since_last_record:0-2'] = np.where((df['mths_since_last_record'] >= 0) & (df['mths_since_last_record'] <= 2), 1, 0)
    df['mths_since_last_record:3-20'] = np.where((df['mths_since_last_record'] >= 3) & (df['mths_since_last_record'] <= 20), 1, 0)
    df['mths_since_last_record:21-31'] = np.where((df['mths_since_last_record'] >= 21) & (df['mths_since_last_record'] <= 31), 1, 0)
    df['mths_since_last_record:32-80'] = np.where((df['mths_since_last_record'] >= 32) & (df['mths_since_last_record'] <= 80), 1, 0)
    df['mths_since_last_record:81-86'] = np.where((df['mths_since_last_record'] >= 81) & (df['mths_since_last_record'] <= 86), 1, 0)
    df['mths_since_last_record:>86'] = np.where((df['mths_since_last_record'] > 86), 1, 0)
    df.drop('mths_since_last_record',axis = 1, inplace = True)

    return df
























    
    



