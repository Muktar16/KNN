from importlib.resources import path
import os
import math
import numpy as np
from PIL import Image


def buildImgVector(path):
    Img = Image.open(path)
    Img = Img.resize((100,100))
    ImageSequence = Img.getdata()
    imageArray = np.array(ImageSequence)
    imageVector = imageArray.flatten()
    return imageVector


def buildImgVectorList():
    tigerFolder = os.listdir('tigers')
    elephantFolder = os.listdir('elephants')
    tigerVectorList = []
    elephantVectorList = []
    
    for i in range(0, len(tigerFolder)):
        imageVector=buildImgVector('tigers/'+tigerFolder[i])
        tigerVectorList.append(imageVector)

        imageVector=buildImgVector('elephants/'+elephantFolder[i])
        elephantVectorList.append(imageVector)
        
    return tigerVectorList,elephantVectorList


def calculate_ED(vectorList,testVector):
    distanceList =  []

    for i in range (0, len(vectorList)):
        distance = 0
        for j in range (min(len(testVector), len(vectorList[i]))):
            distance += (testVector[j] - vectorList[i][j])*(testVector[j] - vectorList[i][j])
            
        distance = math.sqrt(distance)
        distanceList.append(distance)
    return distanceList

def predict(distanceList1,distanceList2,k):
    distanceList1.sort()
    distanceList2.sort()

    Count1 = 0
    Count2 = 0

    for _ in range(0,k):
        if(distanceList1[Count1]< distanceList2[Count2]):
            Count1+=1
        else:
            Count2 +=1

    if Count1 > Count2:
        print('Tiger')
    else:
        print("Elephant")


def main():
    k = int(input("Enter value of k: "))
    tigerVectorList = []
    elephantVectorList = []
    tigerVectorList, elephantVectorList = buildImgVectorList()
    testImgVector = buildImgVector('cat.png')
    distanceList_WithTigers = calculate_ED(tigerVectorList,testImgVector)
    distanceList_WithElephant = calculate_ED(elephantVectorList,testImgVector)
    predict(distanceList_WithTigers,distanceList_WithElephant,k)
    

if __name__ == "__main__":
    main()