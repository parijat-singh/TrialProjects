'''
Created on Feb 13, 2021

@author: parij
'''
x = "Python"
print(x)
a,b,c = 1,2,3
print(a,b,c)
print(b)
print(c)
def age(t):
    if (t<18):
        print("Underage")
    elif (t==18):
        print("you are 18")
    else:
        print("you are old")

age(9)

q = 0
while (q<=5):
    q += 1
    print("the count value is " + str(q))
i = 1
for i in range(1,10):
    if i<5:
        print(str(i) + " is less than 5")
    elif i==5:
        print(str(i) + " is equal to 5")
    else:
        print(str(i) + " is greater than 5")