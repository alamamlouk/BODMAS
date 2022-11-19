try:
    import myPythonFunctions
    userName=input("what's your name : ")
    UserScore=int(myPythonFunctions.getUserPoint(userName))
    newUser=True
    if UserScore==-1:
        newUser=True
    else:
        newUser=False
    if newUser==True:
         UserScore=0
    userChoice = 0
    while userChoice !=-1:
        UserScore+=myPythonFunctions.generateQuestion()
        userChoice=int(input(" do wish to conitnue ?"))
    myPythonFunctions.updateUserPoint(newUser,userName,UserScore)
except:
    print("sorry,something went wrong ")
