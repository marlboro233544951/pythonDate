readfile = open('/home/marlboro/Documents/temp/newIduser-traj-geolife-nolastcom.txt')
savefile = open('/home/marlboro/Documents/temp/newIduser-traj-geolife-nolastcomdata_chat','a+')
for line in readfile:
    item = line.strip().split(',')
    if len(item) < 4:
        pass
    else:
        savefile.write(item[1]+','+item[-1]+'\n')
        savefile.write(','.join(item[2:-1])+'\n')
readfile.close()
savefile.close()