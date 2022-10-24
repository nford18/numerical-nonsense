import math

# Problem 1
def power(x):
    rtnList = []
    for i in range(1,5):
        rtnList.append(math.pow(x,i))
    return rtnList

def exe1():
    print("\nProblem 1:___________")
    for i in range(1,11,1):
        results = power(i)
        for j in range(len(results)):
            print(results[j], end =" ")
        print("")

exe1()

##########################################################
# Problem 2
def trig(x):
    rtnList = []
    rad = math.radians(x)
    rtnList.append(rad)
    rtnList.append(1/math.tan(rad))
    return rtnList

def exe2():
    print("\nProblem 2:___________")
    degree = float(input('Enter an angle in degrees: '))
    result = trig(degree)
    print("The angle in radians is: ", result[0])
    print("The cotangent of the angle is: ", result[1])

exe2()

##########################################################
# Problem 3
def exe3():
    print("\nProblem 3:___________")
    names = [["Albert", "Einstein"], ["Ervin", "Schrodinger"], ["Maria", "Curie"]]
    namesFirst = [names[0][0], names[1][0], names[2][0]]
    namesLast = [names[0][1], names[1][1], names[2][1]]

    # print 1
    namesLast.sort()
    for o in namesLast:
        print(o) 

    # print 2
    for i in range(len(namesFirst)):
        tempStr = namesFirst[i]
        tempStr = tempStr.upper().center(15)
        # bars added to printed line to show the centering
        print("|", tempStr, "|") 

    # print 3
    for i in range(len(namesFirst)):
        strLen = len(namesFirst[i])
        print(namesFirst[i][strLen - 1]) 

exe3()
        



