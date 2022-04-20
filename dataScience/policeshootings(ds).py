import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#pie charts generated from police shooting statistics provided by washingtonpost
#shows distributions of a variety statistics based on race in the context of police shooting


dataset = pd.read_csv('fatal-police-shootings-data.csv')

newDataset = pd.DataFrame(columns=['totalDead', 'amt_unarmed', 'bodycamsPresent', 'popPercent'],
                          index=['Asian', 'White', 'Black', 'Native', 'Hispanic'])

#tuple declarations
newDataset['totalDead']['Asian'] = 0
newDataset['totalDead']['Black'] = 0
newDataset['totalDead']['White'] = 0
newDataset['totalDead']['Native'] = 0
newDataset['totalDead']['Hispanic'] = 0

newDataset['bodycamsPresent']['Asian'] = 0
newDataset['bodycamsPresent']['Black'] = 0
newDataset['bodycamsPresent']['White'] = 0
newDataset['bodycamsPresent']['Native'] = 0
newDataset['bodycamsPresent']['Hispanic'] = 0

newDataset['amt_unarmed']['Asian'] = 0
newDataset['amt_unarmed']['Black'] = 0
newDataset['amt_unarmed']['White'] = 0
newDataset['amt_unarmed']['Native'] = 0
newDataset['amt_unarmed']['Hispanic'] = 0

#based off of 2019 census(numbers taken from census.gov)
newDataset['popPercent']['Asian'] = 5.9
newDataset['popPercent']['Black'] = 13.4
newDataset['popPercent']['White'] = 60.4
newDataset['popPercent']['Hispanic'] = 18.3
newDataset['popPercent']['Native'] = 1.3

#2.7 percent are two or more races(this number doesn't seem accurate to me)

#iterator num
count = 0

for i in dataset.iterrows():
    
    if dataset['race'].iloc[count] == 'A':
        newDataset['totalDead']['Asian'] += 1
        if dataset['body_camera'].iloc[count] == True:
            newDataset['bodycamsPresent']['Asian'] += 1
        if dataset['armed'].iloc[count] == 'unarmed':
            newDataset['amt_unarmed']['Asian'] += 1

        
    elif dataset['race'].iloc[count] == 'B':
        newDataset['totalDead']['Black'] += 1
        if dataset['body_camera'].iloc[count] == True:
            newDataset['bodycamsPresent']['Black'] += 1
        if dataset['armed'].iloc[count] == 'unarmed':
            newDataset['amt_unarmed']['Black'] += 1
        
    elif dataset['race'].iloc[count] == 'W':
        newDataset['totalDead']['White'] += 1
        if dataset['body_camera'].iloc[count] == True:
            newDataset['bodycamsPresent']['White'] += 1
        if dataset['armed'].iloc[count] == 'unarmed':
            newDataset['amt_unarmed']['White'] += 1
            
    elif dataset['race'].iloc[count] == 'N':
        newDataset['totalDead']['Native'] += 1
        if dataset['body_camera'].iloc[count] == True:
            newDataset['bodycamsPresent']['Native'] += 1
        if dataset['armed'].iloc[count] == 'unarmed':
            newDataset['amt_unarmed']['Native'] += 1
            
    elif dataset['race'].iloc[count] == 'H':
        newDataset['totalDead']['Hispanic'] += 1
        if dataset['body_camera'].iloc[count] == True:
            newDataset['bodycamsPresent']['Hispanic'] += 1
        if dataset['armed'].iloc[count] == 'unarmed':
            newDataset['amt_unarmed']['Hispanic'] += 1            
    count += 1

plot = newDataset.plot.pie(subplots=True, figsize=(12,8))

plt.show()


