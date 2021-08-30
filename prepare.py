# template for prepare.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from env import host, user, password
from acquire import get_connection, telco_churn_data, get_telco_churn_data

# prepare telco data

# this function displays the distributions of each column
def num_distributions(df):

    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()
            
            return df 
        
# cleaning up the telco data

def prep_telco(df):
    
    df = df.drop(columns = ['payment_type_id', 'contract_type_id', 'internet_service_type_id', 'customer_id', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies'], inplace = True) #dropping columns not needed
    
    #changing my values to '0' and '1' 
    df = telco_db.replace({'gender':{'Male':0,'Female':1}},inplace = True)
    df = telco_db.replace({'partner':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'dependents':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'phone_service':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'paperless_billing':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'churn':{'No':0,'Yes':1}},inplace = True)
    
   #renaming my gender column to is_female
    df = telco_db.rename(columns = {'gender':'is_female'},inplace = True)
    
    #creating dummies for my df
    dummy_df = pd.get_dummies(df[['multiple_lines','online_security','internet_service_type','contract_type','payment_type']], dummy_na=False, drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    df = df.drop(columns = ['multiple_lines','online_security','internet_service_type','contract_type','payment_type'])

    return df

             

def telco_churn_split(df, target, seed=123):
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