# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import t

# # 在5-15范围内生成15个随机数据点
# X = np.random.randint(5, 15, 15)
#
# # 样本大小
# n = X.size
#
# # 平均
# X_mean = np.mean(X)
#
# # standard deviation
# X_std = np.std(X)
#
# # standard error
# X_se = X_std / np.sqrt(n)
# # alternatively:
# #    from scipy import stats
# #    stats.sem(X)
#
# # 95% Confidence Interval
#
# dof = n - 1  # degrees of freedom
# alpha = 1.0 - 0.95
# conf_interval = t.ppf(1 - alpha / 2., dof) * X_std * np.sqrt(1. + 1. / n)
font = {'family' : 'serif',
        # 'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 26,
        }

TranDPF1mean = 0.248
TranDPF1std = 0.308
TranILPF1mean = 0.248
TranILPF1std = 0.308
CombDPF1mean = 0.286
CombDPF1std = 0.353
CombILPF1mean = 0.286
CombILPF1std = 0.353
LSTMmean = 0.6424
LSTMstd = 0.1662
GRUmean = 0.6418
GRUstd = 0.1656

fig = plt.gca()
plt.errorbar(1, TranDPF1mean, yerr=TranDPF1std, fmt='-o',capsize=10)
plt.errorbar(2, CombDPF1mean, yerr=CombDPF1std, fmt='-o',capsize=10)
plt.errorbar(3, TranILPF1mean, yerr=TranILPF1std, fmt='-o',capsize=10)
plt.errorbar(4, CombILPF1mean, yerr=CombILPF1std, fmt='-o',capsize=10)
plt.errorbar(5, LSTMmean, yerr=LSTMstd, fmt='-o',capsize=10)
plt.errorbar(6, GRUmean, yerr=GRUstd, fmt='-o',capsize=10)

plt.xlim([0, 7])
# plt.ylim(X_mean - conf_interval - 2, X_mean + conf_interval + 2)
# plt.ylim(TranDPF1mean - TranDPF1std -0.2 ,TranDPF1mean + TranDPF1std +0.2)
plt.ylim([-0.2, 1.1])
# axis formatting
fig.axes.get_xaxis().set_visible(False)
fig.spines["top"].set_visible(False)
fig.spines["right"].set_visible(False)
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="on", right="off", labelleft="on")

plt.legend(['Markov', 'Markov-Rank', 'MarkovPath', 'MarkovPath-Rank','TRED-L', 'TRED-G'],
           loc='upper left',
           numpoints=1,
           fancybox=True)

plt.ylabel('Pairs-F1', fontdict=font)
plt.title('F@100', fontdict=font)

plt.show()