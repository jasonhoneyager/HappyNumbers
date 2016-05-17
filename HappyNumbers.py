#######################Happy Numbers##########################
#                                                            #
#    square each digit, then add the results together        #
#    repeat with new number until reduced to single digit    #
#    if single digit is 1, then number is happy              #
#                                                            #
##############################################################

def Recycler():
    for Integer in range(10001):
        IntegerList = SplitInteger(Integer)
        HappyCheck = SquareInteger(IntegerList)
        DisplayHappiness(Integer, HappyCheck)
                
def SplitInteger(Integer):
        IntegerString = str(Integer)
#        print(IntegerString)
        IntegerList = list(IntegerString)
#        print(IntegerList)
        return IntegerList

def SquareInteger(IntegerList):
    Total = 0
    for Squares in IntegerList:
        Total += int(Squares)**2
    HappyCheck = RecheckTotal(Total)
#    print("sqint",HappyCheck)
    if HappyCheck == True:
        return HappyCheck
        
def RecheckTotal(Total):
        TotalString = str(Total)
        IntegerList = list(TotalString)
        HappyCheck = None
#        print(len(IntegerList))
#        print(IntegerList)
        if len(IntegerList) > 1:
            HappyCheck = SquareInteger(IntegerList)
        if len(IntegerList) == 1 and IntegerList[0] == "1":
            HappyCheck = True
#            print("Happy")
#        print("rechecktotal",HappyCheck)
        return HappyCheck
    
def DisplayHappiness(Integer, HappyCheck):
    if HappyCheck == True:
        print(Integer,"is Happy")

def RunCode():
    Recycler()
    

##############################################################

RunCode()