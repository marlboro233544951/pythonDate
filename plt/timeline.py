import numpy as np
import matplotlib.pyplot as plt

def listdiv(l,num):
    li =[]
    for i in l:
        i = float(i)/num
        li.append(i)
    return li

# def readquant(qlabels,quants1,quants2,quants3,quants4):
#     new = [ [0 for i in range(4)] for i in range(9)]
#     quants1 = listdiv(quants1,3600)
#     quants2 = listdiv(quants2,3600)
#     quants3 = listdiv(quants3,3600)
#     quants4 = listdiv(quants4,3600)
#     for rank,colum in enumerate(qlabels):
#
#         new[rank][0]=quants1[rank]
#         new[rank][1]=quants2[rank]
#         new[rank][2]=quants3[rank]
#         new[rank][3]=quants4[rank]
#
#     return new
def readquant(qlabels,quants1,quants2,quants3,quants4,quants5):
    new = [ [0 for i in range(5)] for i in range(9)]
    quants1 = listdiv(quants1,3600)
    quants2 = listdiv(quants2,3600)
    quants3 = listdiv(quants3,3600)
    quants4 = listdiv(quants4,3600)
    quants5 = listdiv(quants5,3600)
    for rank,colum in enumerate(qlabels):

        new[rank][0]=quants1[rank]
        new[rank][1]=quants2[rank]
        new[rank][2]=quants3[rank]
        new[rank][3]=quants4[rank]
        new[rank][4]=quants5[rank]

    return new
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd']
font = {'family': 'serif',
        # 'color'  : 'darkred',
        'weight': 'normal',
        'size': 36,
        }
lfont = {'family': 'serif',
        # 'color'  : 'darkred',
        'weight': 'normal',
        'size': 30,
        }
labels = ['Random', 'Popu', 'Rank', 'Markov', 'Markov-Rank', 'MarkovPath', 'MarkovPath-Rank', 'TRED-L', 'TRED-G']
# dataset = ['F@100', 'F@200', 'F@400', 'F@800']
dataset = ['Osak', 'Glas', 'Toro', 'Edin', 'Melb']
# quants1 = [2, 95, 110, 100, 123, 756, 810, 500, 512]
# quants2 = [4, 623 ,763 , 462, 370, 3179, 3179, 1213, 1135]
# quants3 = [4, 1011 , 1019, 845, 924, 6189, 6176, 1804, 1997]
# quants4 = [8, 4435, 5739, 3823, 3106, 26795, 25795, 2148, 2335]
# y_offsets = {'TRED-L':-0.35,'MarkovPath-Rank':-0.1,'Rank':0,'Popu':0.1,'Markov':0,'Markov-Rank':-0.03,'TRED-G':-0.1}

y_offsets = {'TRED-G':0.7,'Popu':-0.6}
quants1 = [2, 65, 80, 70, 85, 513, 589, 354, 433]
quants2 = [3, 311 , 319, 245, 324, 2189, 2176, 1004, 997]
quants3 = [8, 6235 ,7639 , 4623, 3706, 31795, 31795, 2148, 2335]
quants4 = [9, 2655 ,2278 , 1763, 1963, 15666, 14663, 1756, 1699]
quants5= [9, 11465 ,11744 , 23465, 28689, 63146, 67313, 2380, 2456]

new = readquant(labels,quants1,quants2,quants4,quants3,quants5)
# new = readquant(labels,quants1,quants2,quants3,quants4)
width = 0.4
# ind = np.linspace(0.9, 20.5, 4)
# ind = np.linspace(0.5, 20.5, 4)
# make a square figure
ind = np.linspace(0.5, 20.5, 5)
# yind = np.linspace(0, 8, 5)
yind = np.linspace(0, 20, 5)
fig = plt.figure(1)
# plt.ylim(0, 20)
plt.xlim(0, 3)
plt.ylim(0, 8)
# plt.ylim(0, 20)
ax = fig.add_subplot(111)
ax.set_xticks(ind)
ax.set_xticklabels(dataset, fontdict=font)
ax.set_yticks(yind)
# yli = [0,2,4,6,8]
yli = [0,5,10,15,20]
ax.set_yticklabels(yli,fontdict=lfont)
# ax.set_title('Foursquare',fontdict=font)
ax.set_title('Flickr',fontdict=font)

for rank, column in enumerate(labels):
    # Plot each line separately with its own color.


    line = plt.plot(ind - width / 2,
                    new[rank],
                    lw=2.5,
                    color=color_sequence[rank],
                    label=labels[rank])
    y_pos = new[rank][-1]

    if column in y_offsets:
        y_pos += y_offsets[column]

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(20.5, y_pos, column, fontdict=lfont, color=color_sequence[rank],withdash=True)

ax.set_ylabel('Time(hours)',fontdict=font)
# plt.legend(loc='upper left',
#            numpoints=1,
#            fancybox=True)
plt.show()