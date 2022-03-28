from importlib.resources import path
import os
import math
import numpy as np
from PIL import Image

tigerFolder = os.listdir('tigers')
tiger_img_count = len(tigerFolder)
iceFolder = os.listdir('elephants')


def buildImgVector(path):
    Img = Image.open(path)
    Img = Img.resize((24,24))
    ImageSequence = Img.getdata()
    imageArray = np.array(ImageSequence)
    imageVector = imageArray.flatten()
    return imageVector


tigerVector = []
elephantVector = []
for itr in range(0, tiger_img_count):
    imageVector=buildImgVector('tigers/'+tigerFolder[itr])
    tigerVector.append(imageVector)

    imageVector=buildImgVector('elephants/'+iceFolder[itr])
    elephantVector.append(imageVector)


testImgVector = buildImgVector('test1.png')


distanceWithFire =  []
distanceWithIce = []

for i in range (0, len(tigerVector)):
    distance = 0
    for j in range (min(len(testImgVector), len(tigerVector[i]))):
        distance += (testImgVector[j] - tigerVector[i][j])*(testImgVector[j] - tigerVector[i][j])
        
    distance = math.sqrt(distance)
    distanceWithFire.append(distance)

for i in range (0, len(elephantVector)):
    distance = 0
    for j in range (min(len(testImgVector), len(elephantVector[i]))):
        distance += (testImgVector[j] - elephantVector[i][j])*(testImgVector[j] - elephantVector[i][j])
    
    distance = math.sqrt(distance)
    distanceWithIce.append(distance)

distanceWithFire.sort()
distanceWithIce.sort()

k = int(input("enter the value for k: "))
i=0
j=0
fireCount = 0
iceCount = 0

for _ in range(0,k):
    if(distanceWithFire[i]< distanceWithIce[j]):
        fireCount += 1
        i += 1
    else:
        iceCount +=1
        j+=1

if iceCount >fireCount:
    print('Elephant')
else:
    print("Royel Bengal Tiger")