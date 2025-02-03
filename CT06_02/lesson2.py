# repeat 10 times
# say hey
# move 10 steps 
# set counter to 0
# repeat until counter is equal to 50
# move ten steps
# turn right 15 degrees
# change counter by +10
# ask what is your age and wait for answer
# if the answer is smaller than 18, then say access denied
# if the answer is bigger than 18, say welcome
print("Hello from lesson 2")

######## Write the pseudocode in comments for task 2 here
# Using comments, translate the code shown on screen into pseudocode.
# check what materials the item is made of
# if the item is made of plastic, then put it into the plastic bin
# if the item is made of glass, then put it into the glass bin
# if the item is made of paper, then put it into the paper bin

######## Write the pseudocode in comments for task 3 here
# Using comments, translate the code shown on screen into pseudocode.
# ask user for secret phrase
# check if secret phrase is correct
# if not, say error, the password is incorrect
# if correct, congradulations, the password is correct
# get sudents score 1
# get students score 2
# get students score 3
# take 20% of score 1
# take 40% of score 2
# take 40% of score 3
# add the three numbers
# print the final score
 
score1 = input("what is your score1 score?")
score1 = int(score1)
score2 = input("what is your score2 score?")
score2 = int(score2)
score3 = input("what is your score3 score?")
score3 = int(score3)
score4 = input("what is your score4 score?")
score4 = int(score4)

score1 = score1 * 0.20
score2 = score2 * 0.10
score3 = score3 * 0.40
score4 = score4 * 0.30

final = score1 + score2 + score3 + score4
print("Your final score is", final)