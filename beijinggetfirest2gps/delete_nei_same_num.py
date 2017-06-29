# -*- coding:utf8 -*-
loadfile = open('newIduser-traj-geolife-nolastcom.txt', 'r')
savefile = open('geolife_beijing_trajectory.txt', 'a+')

for line in loadfile:

    list =[]
    line = line.strip().split(',')
    list.append(line[0])
    line = line[1:]
    lenth = len(line)# 同一个点停留2分钟及以上只用2个点表示
    if lenth > 2:#选取有3个POI点的轨迹
        set = 0
        for i in range(lenth-1):


            if int(line[i]) == int(line[i+1]) and set == 0:
                list.append(line[i])
                set =1

            elif int(line[i]) != int(line[i+1]):
                list.append(line[i])
                set = 0
            else:
                pass
        for num in list:

            savefile.write(num + ',')

        savefile.write('\n')

savefile.close()
loadfile.close()
