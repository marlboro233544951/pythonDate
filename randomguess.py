import numpy as np
import sys
from F1AndPairsF1 import calc_F1,calc_pairsF1


def extract_traj(tid, traj_all):
    return traj_all[tid]

def maketrajall(file):
    trajall = open(file)
    id = 0
    traj_all = {}
    trajid_set_all = []
    for line in trajall:
        line = line.strip().split(',')
        l = []
        for item in line:
            l.append(int(item))
        traj_all[id] = l
        trajid_set_all.append(id)
        id += 1
    trajall.close()
    return traj_all,trajid_set_all

file = '/home/marlboro/wht/trajdata/geolife_traj.txt'
traj_all,trajid_set_all = maketrajall(file)


recdict_rand = dict()
cnt = 1

poi_dict = dict()
for tid in trajid_set_all:
    tr = extract_traj(tid, traj_all)
    for poi in tr:
        if poi in poi_dict:
            poi_dict[poi] += 1
        else:
            poi_dict[poi] = 1

for times in range(5):
    F1_rand2 = []
    pF1_rand2 = []
    for i in range(len(trajid_set_all)):
        tid = trajid_set_all[i]
        t = extract_traj(tid, traj_all)

        # trajectory is too short
        if len(t) < 3: continue

        pois = [x for x in sorted(poi_dict.keys()) if poi_dict[x] > 1]

        # start/end is not in training set
        if not (t[0] in pois and t[-1] in pois): continue


        cnt += 1


        pois1 = [x for x in pois if x not in {t[0], t[-1]}]
        rec_ix = np.random.choice(len(pois1), len(t) - 2, replace=True)
        rec_rand = [t[0]] + list(np.array(pois1)[rec_ix]) + [t[-1]]
        F1_rand2.append(calc_F1(t, rec_rand))
        recdict_rand[tid] = {'REAL': t, 'REC_RAND': rec_rand}
        pF1_rand2.append(calc_pairsF1(recdict_rand[tid]['REAL'], recdict_rand[tid]['REC_RAND']))

    print('Experimental  F1: mean=%.3f, std=%.3f, pairsF1 (%.3f, %.3f)' % (np.mean(F1_rand2), np.std(F1_rand2),np.mean(pF1_rand2), np.std(pF1_rand2)))
    sys.stdout.flush()