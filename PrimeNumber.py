'''
Created on Feb 13, 2021

@author: parij
'''
limit = input("Which number do u want to check?")
if int(limit) < 3:
    print(2)
else:
    primeNum = [2]
    for i in range (3,int(limit)+1):
        checkPrime = True
        for j in primeNum:
            if i%j == 0:
                checkPrime = False
                break
        if checkPrime == True:
            primeNum.append(i)
    print (primeNum)
    print (len(primeNum))
    if int(limit) in primeNum:
        print(limit + " is a prime number")
    #111    print("I love you Marya")
    else:
        print(limit + " is not a prime number")
        print(limit + " is divisible by " + str(j))
    
            