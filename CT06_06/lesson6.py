# print("Hello from lesson 6")
numstudent = input("How many students do you have? ")
numscore = 0
for i in range(numstudent):
    score = int(input("What is your students score? "))
    numscore = numscore + score
print(numscore / int(numstudent))