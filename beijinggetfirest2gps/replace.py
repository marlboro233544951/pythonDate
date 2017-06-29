import re



loadfile = open('geolife_beijing_trajectory.txt','r')
savefile = open('geolife_beijing_trajectory_nc.txt','a+')

min = 100
max = 0
sum = 0
averge = 0
i = 0

for line in loadfile:
    if  line != '\n':
        line = re.sub(r',$','',line).strip()
        savefile.write(line+'\n')
        line = line.split(',')
        lenth = len(line)
        sum = sum + lenth
        i = i +1
        if min > lenth:
            min = lenth
        if max < lenth:
            max = lenth

print 'min=',min,'max=',max,'averge =',sum/i
savefile.close()
loadfile.close()
