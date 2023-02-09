# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

# import numpy as np
# import scipy.stats
# Variance = np.var(2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34)
# Standard_deviation = np.std(2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34)
# Average_value = np.mean(2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34)
# import numpy as np
# import scipy.stats

# import numpy as np
# import scipy.stats

# def mean_confidence_interval(data, confidence=0.95):
#     data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
#     a = 1.0 * np.array(data)
#     n = len(a)
#     m, se = np.mean(a), scipy.stats.sem(a)
#     h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
#     return m, m-h, m+h

import numpy as np
import scipy.stats as st
  
party = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
  

print (st.t.interval(alpha=0.95, df=len(party)-1, loc=np.mean(party), scale=st.sem(party)))

#Данная гипотеза принимается так как истинное значение лежит между 2.4155071095954663 и 2.640492890404533.