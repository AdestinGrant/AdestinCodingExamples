import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading john hopkins data into dataset
dataset = pd.read_csv('time_series_covid19_deaths_US.csv')

#grouping data by state, summing the deaths of each state
dataset=pd.DataFrame(data=dataset.groupby(['Province_State'], as_index=True).sum())

#dropping columns irrelevant to this process
dataset=pd.DataFrame(data=dataset.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_',  'Population']))

#making a list of dates matching the data(this line of code has to be updated with new data imports)
dates = pd.date_range(start='1/22/2020', end='5/14/2020')

#declaring empty lists to populate with deaths by state
alabama = []
california = []
florida = []
georgia = []

#declaring an integer interator
count = 0

#debug print to ensure correct row for state
print(dataset.iloc[0])
print(dataset.iloc[5])
print(dataset.iloc[11])
print(dataset.iloc[12])

#populating empty states lists with death counts, in order to use for plotting
for i in dates:
    
    alabama.append(dataset.iloc[0, count])
    california.append(dataset.iloc[5,count])
    florida.append(dataset.iloc[11,count])
    georgia.append(dataset.iloc[12,count])
    
    count += 1

#empty dataframe for new dataset
data=pd.DataFrame()

#populating empty dataframe with desired columns of data
data['Dates'] = dates
data['Alabama Deaths'] = alabama
data['California Deaths'] = california
data['Florida Deaths'] = florida
data['Georgia Deaths'] = georgia

#debug print for final dataset
print(data)

#style choices
sns.set(style='darkgrid', palette='deep', font='helvetica', color_codes=True)

#setting up subplot grid and size
fig, axes = plt.subplots(2,2, figsize=(12.8, 8), sharex=True)

#seaborn lineplot
sns.lineplot(x='Dates', y='Alabama Deaths', data=data, color='r', ax=axes[0,0])
sns.lineplot(x='Dates', y='California Deaths', data=data, color='b', ax=axes[0,1])
sns.lineplot(x='Dates', y='Florida Deaths', data=data, color='purple', ax=axes[1,0])
sns.lineplot(x='Dates', y='Georgia Deaths', data=data, color='r', ax=axes[1,1])

#iterating through axes in order to rotate tick labels
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
