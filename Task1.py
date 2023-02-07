import numpy as np
import scipy.stats as stats
from scipy.stats import mannwhitneyu
x1= np.array ([380,420, 290])
x2= np.array ([140,360,200,900])
print (stats.mannwhitneyu(x1, x2))
#MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
#Так как пвалуе больше даже 0,1, принимается нулевая гипотеза равенства