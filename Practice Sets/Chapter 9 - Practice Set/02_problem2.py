import random

def game():
    print("You are playing a game.")
    score = random.randint(1,50)
    
    # Fetch the score 
    with open("hiscore.txt") as file:
        hiscore = file.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    print(f"Your Score : {score}")
        
    if(score > hiscore):
        with open("hiscore.txt", "w") as file:
            file.write(str(score))
    else:
        hiscore = 0
    return score

game()