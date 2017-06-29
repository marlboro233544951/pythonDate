# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_bar(labels, quants):
    font = {'family': 'serif',
            # 'color'  : 'darkred',
            'weight': 'normal',
            'size': 22,
            }
    lfont = {'family': 'serif',
            # 'color'  : 'darkred',
            'weight': 'normal',
            'size': 18,
            }
    width = 0.4
    ind = np.linspace(0.5, 9.5, 9)
    # make a square figure
    fig = plt.figure(1)
    # plt.ylim(0, 20)
    plt.ylim(0, 900)
    ax = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind - width / 2, quants, width, color='#5f779c')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels,fontdict=lfont)
    # labels
    ax.set_xlabel('Methods',fontdict=font)
    ax.set_ylabel('Time(Hours)',fontdict=font)
    # title
    # ax.set_title('Osak',fontdict=font)
    # ax.set_title('Glas',fontdict=font)
    # ax.set_title('Edin',fontdict=font)
    # ax.set_title('Toro',fontdict=font)
    # ax.set_title('Melb',fontdict=font)
    ax.set_title('Geolife',fontdict=font)
    # ax.set_title('F@100',fontdict=font)
    # ax.set_title('F@200',fontdict=font)
    # ax.set_title('F@400',fontdict=font)
    # ax.set_title('F@800',fontdict=font)
    plt.grid(True)
    plt.show()

def listdiv(l,num):
    new =[]
    for i in l:
        i = float(i)/num
        new.append(i)
    return new


labels = ['Random','Popu' ,'Rank','Markov', 'Markov-Rank', 'MarkovPath', 'MarkovPath-Rank', 'TRED-L', 'TRED-G']

# quants = [2, 65, 80, 70, 85, 513, 589, 354, 433]
# quants = [3, 311 , 319, 245, 324, 2189, 2176, 1004, 997]
# quants = [8, 6235 ,7639 , 4623, 3706, 31795, 31795, 2148, 2335]
# quants = [9, 2655 ,2278 , 1763, 1963, 15666, 14663, 1756, 1699]
# quants = [9, 11465 ,11744 , 23465, 28689, 63146, 67313, 1280, 1356]
quants = [70, 623500 ,763900 , 462300, 370600, 3179500, 3179500, 19450, 19455]
# quants = [2, 95, 110, 100, 123, 756, 810, 500, 512]
# quants = [4, 623 ,763 , 462, 370, 3179, 3179, 1213, 1135]
# quants = [4, 1011 , 1019, 845, 924, 6189, 6176, 1804, 1997]
# quants = [8, 4435, 5739, 3823, 3106, 26795, 25795, 2148, 2335]

quants = listdiv(quants,3600)

draw_bar(labels, quants)