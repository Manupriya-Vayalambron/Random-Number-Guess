import random
print("***RANDOM GUESS GAME***")
num=random.randint(1,100)
while(1):
 user=int(input("Guess the number which is btwn 1 and 100 : "))
 if user>=1 and user<=100:
     if user>num:
         print("High")
     elif user<num:
         print("Low")
     else:
         print("CONGRATULATIONS!!! You Guessed The Number")
         exit(0)
 else:
     print("Invalid guess, try again")
