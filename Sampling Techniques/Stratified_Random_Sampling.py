# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:52:59 2020

@author: SayanPal
"""

import pandas as pd
import numpy as np
import random

population = pd.read_csv("cdp_population_raw.csv")
cont = pd.read_csv("Trimcontributiongiven.csv")
cont = cont.dropna()

cont['percentage']= 200*cont['percentage']
cont['Sample_pick']=cont['percentage'].apply(np.ceil)

#Trim check
trim_check=cont['trim'].isin(population['vehicle_trim'])

trim_list = cont['trim']

#Picking Random Sample
count = 0
df_final = pd.DataFrame
for i in trim_list.values:
    n_samples = int(cont['Sample_pick'][cont['trim']==i].values[0])
    df_temp = population[population['vehicle_trim']==i].sample(n=n_samples, replace = True)
    if(count == 0):
        df_final = df_temp.copy(deep=True)
        count = 1
    else:
        df_final = pd.concat([df_final,df_temp])

df_final['vehicle_trim'].value_counts()

df_final.to_csv('final_sample.csv',index=False)
