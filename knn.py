from msilib.schema import Directory
from pickle import LONG4
from pickletools import long4
import pandas as pd
import os
import math
import numpy as np
import cv2
try:
    import Image
except ImportError:
    from PIL import Image

fireFolder = os.listdir('fire')
iceFolder = os.listdir('ice')

n_fire_image = len(fireFolder)
n_ice_image = len(iceFolder)

iceVector = []
fireVector = []

for _ in range(0, n_fire_image):
    fire = 'fire/'+fireFolder[_]
    ice = 'ice/'+iceFolder[_]
    fireImg = Image.open(fire)
    fireImg = fireImg.resize((32,32))
    fireImageSequence = fireImg.getdata()
    imageArray = np.array(fireImageSequence)
    #print(imageArray)
    imageVector = imageArray.flatten()
    #print(imageArray)
    fireVector.append(imageVector)

    iceImg = Image.open(ice)
    iceImg = iceImg.resize((32,32))
    iceImgSequence = iceImg.getdata()
    imageArray = np.array(iceImgSequence)
    imageVector = imageArray.flatten()
    iceVector.append(imageVector)

testImg = Image.open('test2.png')
testImg = testImg.resize((32,32))
testImgSequence = testImg.getdata()
testImgArray = np.array(testImgSequence)
testImgVector = testImgArray.flatten()


distanceWithFire =  []
distanceWithIce = []

for i in range (0, len(fireVector)):
    distance = 0
    for j in range (min(len(testImgVector), len(fireVector[i]))):
        distance += (testImgVector[j] - fireVector[i][j])*(testImgVector[j] - fireVector[i][j])
        
    distance = math.sqrt(distance)
    distanceWithFire.append(distance)

for i in range (0, len(iceVector)):
    distance = 0
    for j in range (min(len(testImgVector), len(iceVector[i]))):
        distance += (testImgVector[j] - iceVector[i][j])*(testImgVector[j] - iceVector[i][j])
    
    distance = math.sqrt(distance)
    distanceWithIce.append(distance)

distanceWithFire.sort()
distanceWithIce.sort()

k = int(input("enter the value for k: "))
i=0
j=0
fireCount = 0
iceCount = 0

for itr in range(0,k):
    if(distanceWithFire[i]< distanceWithIce[j]):
        fireCount += 1
        i += 1
    else:
        iceCount +=1
        j+=1

if iceCount >fireCount:
    print('input image is ice')
else:
    print("input image is fire")

    





