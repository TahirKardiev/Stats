# 2)Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import numpy as np
import scipy.stats as st
  
IQs = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
  

print (st.t.interval(alpha=0.95, loc=np.mean(IQs), scale=st.sem(IQs), df = len(IQs) - 1))
#сигма (диспа ген совокупности) не известна, поэтому st.t