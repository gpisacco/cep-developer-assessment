#!/usr/bin/python
"""
author: Gaston Pisacco

"""

import sys
import pandas as pd
from scipy.stats import percentileofscore
import json

def main(argv):
    
    means=pd.read_csv('../../exercise1/output/mean.csv')
    stats=pd.read_csv('../../exercise1/output/stats.csv')
    pct=pd.read_csv('../../exercise2/output/pct.csv')
    question_fields=['fdntext','fldimp','undrfld','advknow','pubpol','comimp','undrwr','undrsoc','orgimp','undrorg']

    #for simpler usage I put all the values 
    #for the first stats cols in a dict for reference
    idx={}
    for i,j in enumerate(stats.icol(0)):
        idx[j]=i
        
    output={'version':'1.0'}
    report={'name': 'Tremont 14S Report',
            'title': 'Tremont 14S Report',
            'cohorts': [],
            'segmentations': []
            }
    elements={}
    for question in question_fields[1:10]:
        element={}
        element['type']='percentileChart'
        element['cohorts']= []
        element['past_results']= []
        element['segmentations']= []
        answers=stats[question]
        element['absolut']= [answers[idx['min']],answers[idx['25%']],answers[idx['50%']],answers[idx['75%']],answers[idx['max']] ]
        #to get single values in a simple way I group the means and pct
        m=means.groupby('fdntext')
        p=pct.groupby('fdntext')        
        element['current']= {
                                'name': '2014',
                                'value': m.get_group('Tremont 14S')[question],
                                'percentage': p.get_group('Tremont 14S')[question],
                            }
        elements[question]=element

    report['elements']=elements
    output['reports']=[]
    output['reports'].append(report)
    
    #the output is not the same, but it does not means sense to cast
    #all values or create a custom serializer to be 100% like the example
    pd.DataFrame(output).to_json('../output/output.json',orient="records")    
   
if __name__ == '__main__':
   main(sys.argv[1:])