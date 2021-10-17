import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def get_best_3_country(file_path):
    
    df=pd.read_csv(file_path)
    df.loc[:,'covid_severity_index'] = df.loc[:,'Death/1 mil population'] * df.loc[:,'Total Cases/1 mil population']
    df = df.sort_values('covid_severity_index').reset_index(drop=True)
    new_table = df.loc[:,['Country','covid_severity_index','Total Recovered','Total Deaths','Total Tests']]
    new_table = new_table.dropna().reset_index(drop=True)
    best_3_countries = new_table.iloc[:3,:]
    best_3_countries.loc[:,'Recovery_Ratio'] = best_3_countries.loc[:,'Total Recovered'] / df.loc[:,'Total Recovered'].sum()
    best_3_countries.loc[:,'Death_Ratio'] = best_3_countries.loc[:,'Total Deaths'] / df.loc[:,'Total Deaths'].median()
    best_3_countries.loc[:,'Tests_Ratio'] = best_3_countries.loc[:,'Total Tests'] / df.loc[:,'Total Tests'].std()
    best_3_countries = best_3_countries.loc[:,['Country','Recovery_Ratio','Death_Ratio','Tests_Ratio']]
    best_3_countries.to_csv('best_3_countries.csv',index=False)
    
    print('\n..Done..!\n')

