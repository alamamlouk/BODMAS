import random
import os
def getUserPoint(name):
    with open("userScores.txt","r") as point:                    #open file
        if os.stat("userScores.txt").st_size != 0:
            for i in point:                                          #read everyline of the fille
                list=i.split(",")                                    # put every line in a list
                if list[0]==name:                                    # check if the name exist
                    print(list[0],",",list[1])                       #print user and his score
                    return list[1]
                    break
                else:
                     return "-1"
        else:

            return "-1"                                            #return score


def updateUserPoint(newUser,userName,score):
    if newUser==True:
        with open("userScores.txt","a") as US:                   #open file to append
            US.write(userName+","+str(score)+"\n")               #append newUSER
    else:
        NUS = open("userScores.tmp", "w")                        #createt new file .tmp
        US = open("userScores.txt", "r")                         #open file
        for i in US:
            list=i.split(",")
            if list[0]==userName:
                list[1]=score
            NUS.write(list[0]+","+str(list[1])+"\n")                   #write in file .tmp
        US.close()
        os.remove("userScores.txt")                               #delete file.txt
        NUS.close()
        os.rename("userScores.tmp","userScores.txt")              #rname file.tmp tp file.txt
def generateQuestion():
    operandList=[0,0,0,0,0]
    operatorList=["","","",""]
    operatorDict={
        1:"+",
        2:"-",
        3:"*",
        4:"**"
    }
    for i in range(len(operandList)):                              #generate random number
        operandList[i]=random.randint(0,9)
    operatorList[0] = operatorDict[random.randint(1, 4)]           # 3abit awil elemnt fil operatorlist
    for i in range(1,len(operatorList)):
        if operatorList[i-1]=="**":                                #check if the elemnt before = **
            operatorList[i]=operatorDict[random.randint(1,3)]
        else:
            operatorList[i]=operatorDict[random.randint(1,4)]
    questionString=""
    for i in range(len(operandList)):                               #3abit questionString
        questionString+=str(operandList[i])
        if i<4:
            questionString+=(operatorList[i])
    result=eval(questionString)                                     #resulta imta3 il equation
    questionString=questionString.replace("**","^")
    print("solve the equation: ",questionString)                    #affichage imta3 questionQtring
    answear=input("put your answear here:")                         #demand lil player bich ida5il a3dad
    while True:
        try:
            answear=int(answear)                                    #convertion lil chaie ili da5laha li a3ded
            if answear==result:
                print("well done you win ")
                return 1
                break
            else:
                print("sorry you lost, the right answear is :",result)
                return 0
                break
        except ValueError:
            answear=input("failed to convert \n please enter a  number:")






