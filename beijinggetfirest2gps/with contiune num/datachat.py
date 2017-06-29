readfile = open('newIduser-traj-geolife-nolastcom.txt')
savefile = open('geolife_beijing_trajectory_chat_', 'a+')

for line in readfile:
    item = line.strip().split(',')
    if len(item) < 4:
        pass
    else:
        savefile.write(item[1]+','+item[-1]+','+str(len(item))+'\n')
        savefile.write(','.join(item[2:-1])+'\n')

readfile.close()
savefile.close()
