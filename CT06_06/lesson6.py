# print("Hello from lesson 6")
numstudent = int(input("How many students do you have? "))
numscore = 0
for i in range(numstudent):
    score = int(input("What is your students score? "))
    numscore = numscore + score
print("Your classes average score is",numscore / numstudent)