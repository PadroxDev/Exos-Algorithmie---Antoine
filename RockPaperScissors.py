from random import randint

signs = ["Rock", "Paper", "Scissors"]

def convertToSign(index):
    return signs[index]

def PaperRockScissors(bo:int, p1_name, p2_name)->None:
    p1_score, p2_score = 0, 0

    while (p1_score < bo and p2_score < bo):
        p1_action = input("Veuillez rentrer un nombre entre 1 et 3")
        p2_action = randint(1, 3)

        if (p1_action == p2_action):
            print("Egalité entre " + convertToSign(p1_action)) + " et " + convertToSign(p2_action)

        elif (p1_action == 1):
            if (p2_action == 2):
                p2_score += 1
                print("Manche remporté par " + p2_name + "!")
                print(convertToSign(p2_action) + " à gagner contre " + convertToSign(p1_action) + "!")
            else:
                p1_score += 1
                print("Manche remporté par " + p1_name + "!")
                print(convertToSign(p1_action) + " à gagner contre " + convertToSign(p2_action) + "!")
        
        