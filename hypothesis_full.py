# READ THIS ------------------------------------------------
# TEMP FILE, evetually need to go into hypothesis_testing.py
# READ THIS ------------------------------------------------

import hypothesis_tests as ht
import api

import pandas as pd
import numpy as np
import scipy.stats as stats

def read_aqi24_data():
  """
  This method reads the aqi_24 data (air quality data from last 24hours) from
  csv file in /data folder and return a dataframe

  """

  # RUN THIS ONLY ONCE, afterwards, read_csv
  # dc.aqi_data(borough_data, 24)
  aqi = pd.read_csv('./data/borough_data_cleaned_aqi.csv',index_col=0)

  # after reading the saved aqi data, turn it into a list and calcualte mean and average
  aqi.aqi_24 = aqi.aqi_24.map(lambda x: [int(i) for i in x[1:-1].split(', ')])

  aqi['aqi_mean'] = aqi.aqi_24.map(lambda x: np.asarray(x).mean())
  aqi['aqi_med'] = aqi.aqi_24.map(lambda x: stats.median(x))

  return aqi

def aqi_by_group(aqi,col,group1, group2):
  group1_raw = aqi[aqi[col]==group1].aqi_24.tolist()
  group1_aqi = api.flatten_list(group1_raw)

  group2_raw = aqi[aqi[col]==group2].aqi_24.tolist()
  group2_aqi = api.flatten_list(group2_raw)

  return np.array(group1_aqi), np.array(group2_aqi)


def create_sample_means(data, num = 1000):
  """
  Create a sample mean distribution from given data (np.array format).
  """
  sample_mean = []

  for x in range(num):
    ele = np.random.choice(data, size=50).mean()
    sample_mean.append(ele)

  return np.array(sample_mean)


def welch_t(a, b):

    """ Calculate Welch's t-statistic for two samples. """

    numerator = a.mean() - b.mean()
    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)

    return np.abs(numerator/denominator)

def welch_df(a, b):

    """ Calculate the effective degrees of freedom for two samples. """

    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size

    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)

    return numerator/denominator

def p_value(a, b, two_sided=False):

    t = welch_t(a, b)
    df = welch_df(a, b)

    p = 1- stats.t.cdf(np.abs(t), df)

    if two_sided:
      return 2*p
    else:
      return p


def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status



# ADDTIONAL THINGS THERE ->

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
