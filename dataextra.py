import linecache


readfile = '/home/marlboro/wht/trajdata/traj-Osak.csv'
file = open('/home/marlboro/wht/torodata/traj-Osak.txt','a+')

i=2
count = 0
for index, line in enumerate(open(readfile)):
    count += 1
#no user
while(i < count):
    line = linecache.getline(readfile,i)
    line = line.strip().split(',')
    # userId = line[0]
    trajLen = int(line[6])
    if trajLen>2:
        poiId = line[2]
        # file.write(userId+','+poiId+',')
        file.write(poiId+',')
        for j in range(trajLen-1):
            line = linecache.getline(readfile, i+j+1)
            line = line.strip().split(',')
            # userId = line[0]
            trajLen = int(line[6])
            poiId = line[2]
            if j+1 == trajLen-1:
                file.write(poiId + '\n')
            else:
                file.write(poiId + ',')
    i = i+trajLen

file.close()

