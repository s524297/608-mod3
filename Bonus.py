import random 
#Generate 120 numbers between 1 and 1000
list_120 = random.sample(range(1,1000),120)
print(list_120)

import statistics as stat 

print('variance: ', stat.pvariance(list_120))

print('standard_deviation: ', stat.pstdev(list_120))