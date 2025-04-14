# print("Hello from lesson 12")
word = input("What is your word? ")
for letter in word:
    if letter == "o" and letter == "e":
        print("This word is valid!")
    else:
        print("This word invalid. Sorry!")