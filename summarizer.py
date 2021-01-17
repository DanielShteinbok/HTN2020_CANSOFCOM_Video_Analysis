# timestamp related the currentFrame
import formatter 

def dictToList(dictionary) :
    returnArray = []
    for key in dictionary:
        if dictionary[key] == 0: continue
        returnArray.append( (key, dictionary[key]) )
    return returnArray


def isNew(currentFrame, previousFrame, frameNum, *args) :
    # dictionary in each frame to dictionary(name: number) per
    typeNumberDict = {}
    
    for i in currentFrame:
        name = i["name"]
        if typeNumberDict.get(name) == None:
            typeNumberDict[name] = 1
        else:
            typeNumberDict[name] += 1
            # print(name, "+1")

    if previousFrame != None:
        for i in previousFrame:
            name = i["name"]
            if typeNumberDict.get(name) == None:
                typeNumberDict[name] = -1
            else:
                typeNumberDict[name] -= 1
                # print(name, "-1")
                
    formatter.csv_format( (dictToList(typeNumberDict), frameNum, args) )
    # return (dictToList(typeNumberDict), frameNum, args)

# # TESTCASE
# cf = [ {"name":"bird"}, {"name":"horse"}, {"name":"wold"}, {"name":"bird"}, {"name":"horse"}, {"name":"wold"} ]
# pf = [ {"name":"bird"}, {"name":"horse"}, {"name":"wold"}, {"name":"bird"}, {"name":"horse"}, {"name":"wold"} ]

# print(isNew(cf, None, 5, "usncusncuen", "wnwhybcn"))
# # TESTCASE

def boxMidpoint(x1,y1,x2,y2):
    return (x1+x2)/2 , (y1+y2)/2
