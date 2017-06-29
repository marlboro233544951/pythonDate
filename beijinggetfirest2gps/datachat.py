readfile = open('geolife_beijing_trajectory_nc.txt')
savefile = open('geolife_beijing_trajectory_chat', 'a+')
for line in readfile:
    item = line.strip().split(',')
    if len(item) < 4:
        pass
    else:
        savefile.write(item[1]+','+item[-1]+'\n')
        savefile.write(','.join(item[2:-1])+'\n')
readfile.close()
savefile.close()