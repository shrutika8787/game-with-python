import random
print("Welcome to the game ;)")
n = 7
score = 0
while n != 0:
    print("Enter your choice-->snake water gun")
    new = input()
    k = new.upper()
    lst = ["snake", "water", "gun"]
    choice = random.choice(lst)
    print(choice)
    if new == "snake" or new == "gun" or new == "water":
        if choice == "snake" and new == "snake":
            print("Tie")
        elif choice == "snake" and new == "water":
            print("loose")
        elif choice == "snake" and new == "gun":
            print("win")
            score += 1
        elif choice == "water" and new == "water":
            print("tie")
        elif choice == "water" and new == "gun":
            print("loose")
        elif choice == "water" and new == "snake":
            print("win")
            score += 1
        elif choice == "gun" and new == "gun":
            print("tie")
        elif choice == "gun" and new == "snake":
            print("loose")
        elif choice == "gun" and new == "water":
            print("win")
            score += 1
        else:
            print("Enter again")
    n -= 1
print("Your total score is:", score)