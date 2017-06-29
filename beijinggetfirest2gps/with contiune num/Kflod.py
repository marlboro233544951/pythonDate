import os
from sklearn.cross_validation import KFold

loadfile = open('geolife_beijing_trajectory_chat_withcon','r')
fold = 5
# savefiletrain = open('geolife_beijing_trajectory_train.txt','a+')
# savefiletest = open('geolife_beijing_trajectory_test.txt','a+')

def gfile(fold):
    ftrain = []
    ftest = []
    for i in range(1,fold+1):
        ftrain.append(os.path.join( 'train-' + str(i)))
        ftest.append(os.path.join('test-' + str(i)))

    return ftrain,ftest

X = []
y = []
i = 1
for line in loadfile:
    if i%2 == 1:
        X.append(line)
    else:
        y.append(line)
    i += 1
kf = KFold(i/2,fold)

ftrain,ftest = gfile(fold)
print ftrain,ftest
j = 0


for train,test in kf:
    f = open(ftrain[j],'a+')
    f.write(train+'\n'+test)
    j += 1
#
# j = 0
# for x in X_test:
#     savefiletest.write(x+y_test[j])
#     j += 1