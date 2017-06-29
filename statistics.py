loadfile = open('newIduser-traj-geolife.txt','r')


sum = 0
averge = 0

userDict = {}

for line in loadfile:
    sum = sum + 1
    line =  line.strip().split(',')
    user = line[0]
    set = 0
    for n in xrange(182):

        if n == int(user):
            set = 1
        
        if n == 181 and set ==0:
            print user


    if userDict.has_key(user):
        i = i + 1
        userDict[user] = i
    else:
        i = 1
        userDict[user] = i

dict = sorted(userDict.iteritems(), key=lambda d:d[1],reverse =True)
print 'sumline=',sum,'averge user own %d line'%(sum/181),'max=',dict[0],'min=',dict[-1]
loadfile.close()