#!/usr/bin/python

"""
author: Gaston Pisacco

"""

import sys
import pandas as pd


#This funcition is used to 
#remove entries with invalid values
def dataFilter(df):
    for i in df:
        if i!='fdntext':
            for l,j in enumerate(df[i]):
                if(j>7):
                    df[i]=df[i].drop(df[i].index[l])
    
    return True

def main(argv):
    question_fields=['fdntext','fldimp','undrfld','advknow','pubpol','comimp','undrwr','undrsoc','orgimp','undrorg']
    
    data=pd.read_csv('../input/xl.csv')
    
    d = data.filter(question_fields)
    
    ## Task 1  ##
    dataFilter(d)
    d=d.groupby('fdntext')
    mean=d.mean()
    mean.to_csv('../output/mean.csv')
    
    ## Task 2  ##
    stats = mean.describe()
    stats.to_csv('../output/stats.csv')
    

if __name__ == "__main__":
   main(sys.argv[1:])