import pandas as py 
import numpy as np
import matplotlib.pyplot as plt

data=py.read_csv('owid-covid-data.csv')
data.columns=["people_vaccinated","total_vaccinations","people_fully_vaccinated","people_fully_vaccinated","new_vaccinations"]
data.head()