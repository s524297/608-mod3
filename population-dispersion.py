values = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print('mean: ', sum(values)/len(values))

value_mean = [value - 3.5 for value in values]

print('values_mean: ', value_mean)

value_sq = [value**2 for value in value_mean]

print('value_sq: ', value_sq) 

variance = sum(value_sq)/len(value_sq)

print('variance: ', variance)

import statistics as stat

print('variance_stat: ', stat.pvariance(values))

import math 

print('standard_deviation: ', math.sqrt(variance))