# 2)Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
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

# Iteranion = 0, B1 = 0.25952808, mse = 493237.7212546963
# Iteranion = 500, B1 = 5.889815595583751, mse = 56516.858416040064
# Iteranion = 1000, B1 = 5.8898204201285544, mse = 56516.85841571941
# Iteranion = 1500, B1 = 5.889820420132673, mse = 56516.85841571943
# Iteranion = 2000, B1 = 5.889820420132673, mse = 56516.85841571943
# Iteranion = 2500, B1 = 5.889820420132673, mse = 56516.8584157194
#almost