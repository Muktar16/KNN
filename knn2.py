from importlib.resources import path
import os
import math
import numpy as np
from PIL import Image

tigerFlattenList = []
elephantFlattenList = []
distancesWithTigerImg = []
distancesWithElephantImg = []

K = int(input("Enter K: "))

tigerDir = os.listdir('tigers')
elephantDir = os.listdir('elephants')

for i in range(0,len(tigerDir)):
    img1 = Image.open('tigers/'+tigerDir[i]).resize((100,100))
    img2 = Image.open('elephants/'+elephantDir[i]).resize((100,100))
    
    img1Array = np.array(img1.getdata())
    tigerFlattenList.append(img1Array.flatten())
    img2Array = np.array(img2.getdata())
    elephantFlattenList.append(img2Array.flatten())


testingImg = Image.open('test2.png').resize((100,100))
testImgVector = np.array(testingImg.getdata()).flatten()

for i in range (0, len(tigerFlattenList)):
    d1 = 0
    d2 = 0
    for j in range (min(len(testImgVector), len(elephantFlattenList[i]))):
        d1 += (testImgVector[j] - tigerFlattenList[i][j])*(testImgVector[j] - elephantFlattenList[i][j])
        d2 += (testImgVector[j] - tigerFlattenList[i][j])*(testImgVector[j] - elephantFlattenList[i][j])
    distancesWithTigerImg.append(math.sqrt(d1))
    distancesWithElephantImg.append(math.sqrt(d2))

distancesWithTigerImg.sort()
distancesWithElephantImg.sort()

counter1 = 0
counter2 = 0

for _ in range(0,K):
    if(distancesWithTigerImg[counter1] < distancesWithElephantImg[counter2]):
        counter1 += 1
    else:
        counter2 +=1

if counter1 > counter2:
    print('Test image is a Tiger')
else:
    print("Test image is an Elephant")