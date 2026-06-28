# stone paper seasor

import random

def record_save():
    with open ("P1/record.txt", "a") as f:
        name = input("\nEnter your good name : ") 
        f.write(f"Name =  {name}\n")
        f.write(f"Your wins = {user_win}\n")
        f.write(f"Computer wins = {comp_win}\n")
        f.write(f"Match draws = {draw_win}\n\n")

def record_see():
    print("*---Score-Board---*")
    print("Your wins = ", user_win)
    print("Computer Wins = ", comp_win)
    print("Match Draw = ", draw_win)
        
user_win = 0
comp_win = 0
draw_win = 0

while True: 

    computer = random.choice(["s", "p", "x"])

    print(""" select choice : 
    s = For stone"
    p = For paper
    x = For seasor
    r = For see record
    v = For view score
    e = For save result""")
    user = input("Enter choice here: ")
    print("Computer chioce" , computer , "and Your choice" , user, " ")

    if(user == "s" and computer == "x" ) or (user == "p" and computer == "s" ) or (user == "x" and computer == "p" ):
        print("You win")
        user_win += 1

    elif(computer == user):
        print("Match Draw")
        draw_win += 1

    elif(user == "e"): 
        # record_see() 
        record_save()
        break

    elif(user == "r"):
        with open ("P1//record.txt", "r") as f:
            print(f.read())

    elif(user == "s" and computer == "p" ) or (user == "p" and computer == "x" ) or (user == "x" and computer == "s" ):
        print("Computer win")
        comp_win += 1

    elif(user == "v"):
        record_see()

    else:
        print("Invalid choice ")
