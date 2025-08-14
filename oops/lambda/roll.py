
import random



print("press 1 to play:press 2 to quit")
roll=input("enter ur choice")

if roll=="1":
    s=random.randint(1,6)
    print(s)
elif roll=="2":
    print("quit")
else:
    print("next game")