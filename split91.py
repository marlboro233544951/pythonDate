readfile = open('/home/marlboro/Documents/temp/traj-geolife-nolastcomdata_chat.txt')
savefile9 = open('/home/marlboro/Documents/temp/traj-geolife-nolastcomdata_chat9.txt','a+')
savefile1 = open('/home/marlboro/Documents/temp/traj-geolife-nolastcomdata_chat1.txt','a+')
i = 1
for line in readfile:

    if i % 10 == 1 or i % 10 == 2:
        savefile1.write(line)
    else:
        savefile9.write(line)

    i = i + 1