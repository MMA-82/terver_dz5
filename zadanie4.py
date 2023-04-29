import numpy as np
import scipy.stats as stats

m = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
d = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
alpha = 0.05
print(stats.ttest_ind(m, d))