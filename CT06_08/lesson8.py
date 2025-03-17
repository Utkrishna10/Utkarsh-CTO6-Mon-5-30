# print("Hello from lesson 8")
# product = 1
# for count in range(5):
#     num = input("Give me a number ")
#     num = int(num)
#     product = product * num
# print("The final result is", str(product))
import time
# start = int(input("What would you like to start at? "))
# for i in range(start,0,-1):
#     print(i)
#     time.sleep(1)
# print("Liftoff!")
import random
# num = random.randint(1,6)
# print(num)
# for i in range(1,20):
#     x = random.randint(0,9999)
#     print(x)
# var = True
# varss = False
# print(var == varss)
# num1 = random.randint(1,100)
# num2 = random.randint(1,100)
# test = "What is", num1,"+",num2,"?"
# cor = input(test)
# cor = int(cor)
# hidden = int(num1) + int(num2)
# if cor == hidden:
#     print("Correct!")
# else:
#     print("Wrong")
# print(cor == hidden)
num = random.randint(1,50)
corr1 = input("What number would you like to start at? ")
corr2 = input("What number would you like to end at? ")
corr = num >= corr1
fal = num <= corr2
if corr == fal:
    print("The number was inside your range!")
else:
    print*
print(num)