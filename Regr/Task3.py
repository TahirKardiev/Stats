# 3) Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться
# на каждом шаге одновременно (то есть изменение одного коэффициента 
# не должно влиять на изменение другого во время одной итерации).
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

zp = np.array([[1,1,1,1,1,1,1,1,1,1],[35, 45, 190, 200, 40, 70, 54, 150, 120, 110]])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


def mse_(B1, ks = ks, zp=zp, n=10):
  return np.sum((B1*zp-ks)**2)/n

alpha = 1e-6

B1 = 0.1
n = 10

for i in range (3000):
  B1 -= alpha * (2/n) * np.sum((B1 * zp - ks) * zp)
  if i%500 == 0:
     print ('Iteranion = {i}, B1 = {B1}, mse = {mse}'.format(i=i, B1=B1, mse=mse_(B1)))