# timestamp related the currentFrame
from collections import defaultdict
magicConfidenceValue = 0.5

def dictToList(dictionary) :
    returnArray = []
    for key in dictionary:
        if dictionary[key] == 0: continue
        returnArray.append( (key, dictionary[key]) )
    return returnArray


def isNew(currentFrame, previousFrame, frameNum, *args) :
    # dictionary in each frame to dictionary(name: number) per
    typeNumberDict = {}

    if previousFrame == None: 
        for objects in currentFrame:
            name = objects["name"]

            # if none make one else incremenent by one
            try: typeNumberDict[name] = typeNumberDict[name] + 1
            except KeyError: typeNumberDict[name] = 0

    else:
        for i in currentFrame:
            name = i["name"]
            if typeNumberDict.get(name) == None:
                typeNumberDict[name] = 1
            else:
                typeNumberDict[name] += 1
                # print(name, "+1")

        for i in previousFrame:
            name = i["name"]
            if typeNumberDict.get(name) == None:
                typeNumberDict[name] = -1
            else:
                typeNumberDict[name] -= 1
                # print(name, "-1")


    return (dictToList(typeNumberDict), frameNum)
    


# # TESTCASE
# cf = [ {"name":"bird"}, {"name":"horse"}, {"name":"wold"}, {"name":"bird"}, {"name":"horse"}, {"name":"wold"} ]
# pf = [ {"name":"bird"}, {"name":"horse"}, {"name":"wold"}, {"name":"bird"}, {"name":"horse"}, {"name":"wold"} ]

# print(isNew(cf, pf, 5))
# # TESTCASE


def boxMidpoint(x1,y1,x2,y2):
    return (x1+x2)/2 , (y1+y2)/2
