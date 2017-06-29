#!/usr/bin/python
# -*- coding:utf8 -*-

import os

import datetime

savefile = open('newIduser-traj-geolife.txt', 'a+')
poiFile = open('gps-poi.txt', 'a+')
allFileNum = 0
poiDict = {}
userId = 0
poi = 1

def printPath(path):
    global allFileNum
    '''''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别

    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            if (f == 'labels.txt'):
                pass
            else:
                fileList.append(f)
                # 当一个标志使用，文件夹列表第一个级别不打印
    # i_dl = 0
    dirList =sorted(dirList)
    fileList = sorted(fileList)
    for dl in dirList:
        # if (i_dl == 0):
        #     i_dl = i_dl + 1
        if (dl == 'Trajectory'):
            pass
            printPath(path + '/' + dl)

        else:
            # 打印至控制台，不是第一个的目录
            # print  dl
            global userId
            userId = int(dl)

            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath( path + '/' + dl)
    lenth =len(fileList)
    for fl in fileList:
        # 打印文件
        # if fl == lenth -1:
        #     savefile.write(dl + '\n')
        # if fl == 'labels.txt':
        #     continue
        # else:
        loadfile = open(path+'/'+fl)
        i = 0
        time = []
        # d2 = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
        set = 0

        for line in loadfile:
            if i<6:
                i+=1
            else:
                line =line.strip().split(',')
                if float(line[0]) >39.629169 and float(line[0]) < 40.477453 and float(line[1]) >115.534163 and float(line[1]) <117.201419:
                    gps = str(round(float(line[0]), 2))+','+str(round(float(line[1]), 2))
                    time.append(line[6])
                    d1 = datetime.datetime.strptime(str(line[6]), '%H:%M:%S')

                    # if  not  poiDict.has_key(gps):
                    #     global poi
                    #     poiDict[gps] = poi
                    #     poiFile.write(gps+','+str(poi)+'\n')
                    #     poi = poi + 1

                    if(set == 0):
                        if not poiDict.has_key(gps):
                            global poi
                            poiDict[gps] = poi
                            poiFile.write(gps + ',' + str(poi) + '\n')
                            poi = poi + 1
                        savefile.write(str(userId) + ',')
                        starTime = datetime.datetime.strptime(str(time[0]), '%H:%M:%S')

                        d2 = d1
                        savefile.write(str(poiDict[gps]) + ',')
                        set = 1


                    if (d1-d2).seconds > 60 and (d1-starTime).seconds < 3600*3:
                        if not poiDict.has_key(gps):
                            global poi
                            poiDict[gps] = poi
                            poiFile.write(gps + ',' + str(poi) + '\n')
                            poi = poi + 1
                        savefile.write(str(poiDict[gps])+',')
                        d2 = d1

                    elif (d1-d2).seconds > 60 and (d1-starTime).seconds > 3600*3:
                        if not poiDict.has_key(gps):
                            global poi
                            poiDict[gps] = poi
                            poiFile.write(gps + ',' + str(poi) + '\n')
                            poi = poi + 1
                        savefile.write('\n')
                        savefile.write(str(userId)+',')
                        savefile.write(str(poiDict[gps]) + ',')
                        starTime = d1
                        d2 = d1
                i += 1
        # else:
        #     savefile.write(dl + ',')
        # 随便计算一下有多少个文件
        savefile.write('\n')
        allFileNum = allFileNum + 1
        loadfile.close()


if __name__ == '__main__':
    printPath('/home/marlboro/Downloads/geolife/Geolife Trajectories 1.3/Data')
    print '总文件数 =', allFileNum
    savefile.close()
    # jsObj = json.dumps(poiDict)
    # poiFile.write(jsObj)
    poiFile.close()