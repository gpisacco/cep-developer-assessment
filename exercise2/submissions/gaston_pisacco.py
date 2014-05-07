#!/usr/bin/python

"""
author: Gaston Pisacco

"""

import sys
import pandas as pd
from scipy.stats import percentileofscore


def dataFilter(df):
    for i in df:
        if i!='fdntext':
            for l,j in enumerate(df[i]):
                if(j>7):
                    df[i]=df[i].drop(df[i].index[l])
def main(argv):
    
    data=pd.read_csv('../../exercise1/output/mean.csv')
    df=pd.read_csv('../../exercise1/input/xl.csv')
    question_fields=['fdntext','fldimp','undrfld','advknow','pubpol','comimp','undrwr','undrsoc','orgimp','undrorg']

    d = df.filter(question_fields)
    data= data.groupby('fdntext')
    d=d.groupby('fdntext')
    
    df3 = pd.DataFrame(columns=question_fields)
    for client, mean in data:
        clientPercentiles={question_fields[0]:client}
        for question in question_fields[1:10]:
            for u in mean[question]:
                clientPercentiles[question]=percentileofscore(d.get_group(client)[question].dropna(), u, kind='mean')

        df3=df3.append([clientPercentiles])

    df3.to_csv('../output/pct.csv',index=False)
    
   
if __name__ == "__main__":
   main(sys.argv[1:])