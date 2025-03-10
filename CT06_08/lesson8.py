# print("Hello from lesson 8")
# product = 1
# for count in range(5):
#     num = input("Give me a number ")
#     num = int(num)
#     product = product * num
# print("The final result is", str(product))
import time
start = input("What would you like to start at? ")
for i in range(start,0,-1):
    print(i)
    time.sleep(1)
print("Liftoff!")