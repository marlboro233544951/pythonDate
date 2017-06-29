readfile = open('geolife_beijing_trajectory_chat')
savefile9 = open('geolife_beijing_trajectory_chat9','a+')
savefile1 = open('geolife_beijing_trajectory_chat1','a+')
i = 1
for line in readfile:

    if i % 10 == 1 or i % 10 == 2:
        savefile1.write(line)
    else:
        savefile9.write(line)

    i = i + 1