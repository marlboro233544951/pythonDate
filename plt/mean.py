import numpy as np
# use skplit random_num=1
# Tran  : F1 (0.848, 0.120), pairsF1 (0.636, 0.150) acc25_2*64 LSTM
# Tran  : F1 (0.843, 0.124), pairsF1 (0.646, 0.151) acc25_2*64 GRU
#
# use skplit random_num=2
# Tran  : F1 (0.898, 0.098), pairsF1 (0.658, 0.167) acc45_2*64 LSTM
# Tran  : F1 (0.896, 0.100), pairsF1 (0.633, 0.160) acc40_2*64 GRU
#
# use skplit random_num=3
# Tran  : F1 (0.871, 0.098), pairsF1 (0.661, 0.177) acc25_2*64 LSTM
# Tran  : F1 (0.895, 0.101), pairsF1 (0.676, 0.169) acc35_2*64 GRU
#
#
# use skplit random_num=4
# Tran  : F1 (0.855, 0.124), pairsF1 (0.572, 0.176) acc40_2*64 LSTM
# Tran  : F1 (0.846, 0.123), pairsF1 (0.582, 0.170) acc35_2*64 GRU
#
# use skplit random_num=5
# Tran  : F1 (0.856, 0.097), pairsF1 (0.685, 0.161) acc25_2*64 LSTM
# Tran  : F1 (0.852, 0.101), pairsF1 (0.672, 0.178) acc25_2*64 GRU
LSTMF1 = [0.848,0.898,0.871,0.855,0.856]
LSTMF1S = [0.120,0.098,0.098,0.124,0.097]
GRUF1 = [0.843,0.896,0.895,0.846,0.852]
GRUF1S = [0.124,0.100,0.101,0.123,0.101]
LSTMP1 = [0.636,0.658,0.661,0.572,0.685]
LSTMP1S = [0.150,0.167,0.177,0.176,0.161]
GRUP1 = [0.646,0.633,0.676,0.582,0.672]
GRUP1S =[0.151,0.160,0.169,0.170,0.178]
LSTMF1mean = np.mean(LSTMF1)
LSTMF1std= np.mean(LSTMF1S)
GRUF1mean = np.mean([0.843,0.896,0.895,0.846,0.852])
GRUF1std = np.mean([0.124,0.100,0.101,0.123,0.101])
LSTMP1mean = np.mean([0.636,0.658,0.661,0.572,0.685])
LSTMP1std = np.mean([0.150,0.167,0.177,0.176,0.161])
GRUP1mean = np.mean([0.646,0.633,0.676,0.582,0.672])
GRUP1std =np.mean([0.151,0.160,0.169,0.170,0.178])
print LSTMF1mean,LSTMF1std,GRUF1mean,GRUF1std,LSTMP1mean,LSTMP1std,GRUP1mean,GRUP1std