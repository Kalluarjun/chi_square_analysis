import numpy as np 
import pandas as pd 
import scipy.stats as stats
from scipy.stats import chi2
df= pd.read_csv('C:\\Users\\Dell\\Documents\\python\\chi square test\\1\\marital_status_vs_educational_qualification.csv')
O= df.iloc[:, 1:].values
val= stats.chi2_contingency(O)
E= val[3]
chi_square_statistic= sum([((o-e)**2)/e for o,e in zip(O.flatten(),E.flatten())])
dof= 12
alpha= 0.05
critical_value= chi2.ppf(1-alpha, dof)
if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")

