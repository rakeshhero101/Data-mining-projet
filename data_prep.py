# Importing the required libraries
import numpy as np
import pandas as pd

def DataPrep():
    #Reading the data
    df = pd.read_csv('online_shoppers_intention.csv', na_filter = False)
    
    #Dropping all the nan values
    df= df.dropna()
    
    # Replacing the empty strings in the series with nan and typecast to float
    df['Administrative'] = df['Administrative'].replace('', np.nan).astype(float)
    df['Administrative_Duration'] = df['Administrative_Duration'].replace('', np.nan).astype(float)
    df['Informational'] = df['Informational'].replace('', np.nan).astype(float)
    df['Informational_Duration'] = df['Informational_Duration'].replace('', np.nan).astype(float)
    df['ProductRelated'] = df['ProductRelated'].replace('', np.nan).astype(float)
    df['ProductRelated_Duration'] = df['ProductRelated_Duration'].replace('', np.nan).astype(float)

    df['BounceRates'] = df['BounceRates'].replace('', np.nan).astype(float)
    df['ExitRates'] = df['ExitRates'].replace('', np.nan).astype(float)
    
    # change month data from string to number
    df['Month'] = df['Month'].replace('Jan', 1)
    df['Month'] = df['Month'].replace('Feb', 2)
    df['Month'] = df['Month'].replace('Mar', 3)
    df['Month'] = df['Month'].replace('Apr', 4)
    df['Month'] = df['Month'].replace('May', 5)
    df['Month'] = df['Month'].replace('June', 6)
    df['Month'] = df['Month'].replace('Jul', 7)
    df['Month'] = df['Month'].replace('Aug', 8)
    df['Month'] = df['Month'].replace('Sep', 9)
    df['Month'] = df['Month'].replace('Oct', 10)
    df['Month'] = df['Month'].replace('Nov', 11)
    df['Month'] = df['Month'].replace('Dec', 12)

    #Type Casting it to int
    df['Month'] = df['Month'].astype(int)
    
    # Changing VisitorType into binary 0/1 variable
    Visitor_Type = {'Returning_Visitor':0, 'New_Visitor': 1}
    df['VisitorType'] = df['VisitorType'].map(Visitor_Type)
    
    # Changing visitor type into int
    df['VisitorType'] = df['VisitorType'].dropna().astype(int)
      
    # change boolean values(True&False) to integers 1 or 0
    weekend_type ={True : 1, False : 0}
    df['Weekend'] = df['Weekend'].map(weekend_type)
    df['Weekend'] = df['Weekend'].dropna().astype(int)

    revenue_type ={True : 1, False : 0}
    df['Revenue'] = df['Revenue'].map(revenue_type)
    df['Revenue'] = df['Revenue'].dropna().astype(int)
    
    # If 0 view of the page the duration should be 0 as well
    # Duration can not be negative. So, changing it to positive
    if np.any(df['Administrative'] <= 0.0):
        df['Administrative_Duration'] == 0.0

    df['Administrative_Duration'] = abs(df['Administrative_Duration'])
    
    if np.any(df['Informational'] <= 0.0):
        df['Informational'] == 0.0

    df['Informational_Duration'] = abs(df['Informational_Duration'])
    
    if np.any(df['ProductRelated'] <= 0.0):
        df['ProductRelated'] == 0.0

    df['ProductRelated_Duration'] = abs(df['ProductRelated_Duration'])
    
    df = df.dropna()
    
    return df