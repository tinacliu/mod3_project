"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import math
import hypothesis_tests
import api
import data_cleaning as dc

def generate_datapoints(borough):
    cleaned_data = dc.full_clean()
    call = api.get_place_aqi(cleaned_data, borough,1)
    borough_data = np.asarray(call)
    return borough_data

def sample_mu_std_var(sample):
    mean = np.mean(sample)
    std = np.std(sample)
    var = np.var(sample)
    return mean, std, var

def Cohen_d(sample1, sample2):
    #Calculate Difference
    diff = sample1.mean() - sample2.mean()
    #Calulate shape of arrays
    n1, n2 = len(sample1), len(sample2)
    var1 = sample1.var()
    var2 = sample2.var()
    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    return d

def twosample_tstatistic(sample1, sample2):
    stat = stats.ttest_ind(sample1, sample2, equal_var = False)
    t_stat = stat.statistic
    p_val = stat.pvalue
    print('T-Stat: ',t_stat, ' P-Val: ',p_val)

    
def normals(mean, std):
    return norm(mean, std)

def evaluate_PDF(rv, x=4):
    # Identify the mean and standard deviation of random variable 
    mean = rv.mean()
    std = rv.std()
    # Use numpy to calculate evenly spaced numbers over the specified interval (4 sd) and generate 100 samples.
    xs = np.linspace(mean - x*std, mean + x*std, 100)
    # Calculate the peak of normal distribution i.e. probability density. 
    ys = rv.pdf(xs)
    return xs, ys

# def create_sample_dists(cleaned_data, y_var=None, categories=[]):
#     """
#     Each hypothesis test will require you to create a sample distribution from your data
#     Best make a repeatable function

#     :param cleaned_data:
#     :param y_var: The numeric variable you are comparing
#     :param categories: the categories whose means you are comparing
#     :return: a list of sample distributions to be used in subsequent t-tests

#     """
#     htest_dfs = []

#     # Main chunk of code using t-tests or z-tests
#     return htest_dfs

# def compare_pval_alpha(p_val, alpha):
#     status = ''
#     if p_val > alpha:
#         status = "Fail to reject"
#     else:
#         status = 'Reject'
#     return status


# def hypothesis_test_one(alpha = None, cleaned_data):
#     """
#     Describe the purpose of your hypothesis test in the docstring
#     These functions should be able to test different levels of alpha for the hypothesis test.
#     If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

#     :param alpha: the critical value of choice
#     :param cleaned_data:
#     :return:
#     """
#     # Get data for tests
#     comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])

#     ###
#     # Main chunk of code using t-tests or z-tests, effect size, power, etc
#     ###

#     # starter code for return statement and printed results
#     status = compare_pval_alpha(p_val, alpha)
#     assertion = ''
#     if status == 'Fail to reject':
#         assertion = 'cannot'
#     else:
#         assertion = "can"
#         # calculations for effect size, power, etc here as well

#     print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
#           f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status

# def hypothesis_test_two():
#     pass

# def hypothesis_test_three():
#     pass

# def hypothesis_test_four():
#     pass
