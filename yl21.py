import random

x = random.randint(1, 100)

guess = -1

while x != guess:

    guess = int(input("Paku arv 1-100:")) 

    if x > guess:
        print("paku suurem")
    elif x < guess:
        print("paku väiksem")
    elif x == guess:
        print("Õige!")