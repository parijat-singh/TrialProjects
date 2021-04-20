'''
Created on Feb 13, 2021

@author: parij
'''
primeNum = [2]
for i in range (3,10):
    checkPrime = True
    for j in primeNum:
        if i%j == 0:
            checkPrime = False
    if checkPrime == True:
        primeNum.append(i)
print (primeNum)