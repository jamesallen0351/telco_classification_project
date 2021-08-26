# getting data for aquire.py

import pandas as pd
import numpy as np
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    This function gets my info from my env file and creats a connection url 
    
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
# Acquiring telco_churn data

def telco_churn_data():
    
    sql_query = '''SELECT * FROM customers
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN contract_types USING(contract_type_id)
    JOIN payment_types USING(payment_type_id)'''
    
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df 

def get_telco_churn_data():
    
    if os.path.isfile('telco_churn.csv'):
        
        df = pd.read_csv('telco_churn.csv', index_col=0)
    
    else:
        
        df = new_telco_churn_data()
        df.to_csv('telco_churn.csv')
    
    return df