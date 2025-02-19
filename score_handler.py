FILE_PATH = "score_board.txt"

def update_score(player, score):
    with open(FILE_PATH, "a") as file:
        file.write(f"{player}: {score}\n")

def read_scores():
    with open(FILE_PATH, "r") as file:
        data = file.readlines()
    
    for line in data:
        print(" ".join(line.strip()))