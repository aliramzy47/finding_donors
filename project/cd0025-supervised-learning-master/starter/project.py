import numpy as np
import pandas as pd
from time import time

# Import supplementary visualization code visuals.py
import visuals as vs

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

data = pd.read_csv("census.csv", header= 0)
#print(data.info())
#print(data[['age','income']].head(20))
#print(data.loc[40:50])
print(len(data[data.income == '<=50K']))

# TODO: Total number of records
n_records = len(data)
# TODO: Number of records where individual's income is more than $50,000
n_greater_50k = len(data[data.income == '>50K'])
# TODO: Number of records where individual's income is at most $50,000
n_at_most_50k = len(data[data.income == '<=50K'])

# TODO: Percentage of individuals whose income is more than $50,000
greater_percent = round((n_greater_50k/n_records)*100, 2) # two decimal places

# Print the results
print("Total number of records: {}".format(n_records))
print("Individuals making more than $50,000: {}".format(n_greater_50k))
print("Individuals making at most $50,000: {}".format(n_at_most_50k))
print("Percentage of individuals making more than $50,000: {}%".format(greater_percent))

# Split the data into features and target label
#income_raw = data['income']
#features_raw = data.drop('income', axis = 1)

# Visualize skewed continuous features of original data
#vs.distribution(data)


plt.figure()
print(sns.displot(data['capital-gain']))
plt.show()
plt.close()