loadfile = 'user-traj-Toro.txt'
savefile = open('newIduser-traj-Toro.txt','a+')

temp = dict()
i = 1
for line in open(loadfile,'r'):
    old =line.strip().split(',',1)
    line = line.strip().split(',')
    userId = line[0]
    if userId not in temp.keys():
        temp[userId] = i
        savefile.write(str(i)+','+old[1]+'\n')
        i += 1
    else:
        j = temp[userId]
        savefile.write(str(j)+','+old[1]+'\n')

