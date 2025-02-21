FILE_PATH = "score_board.txt"

def update_score(player, score):
    global FILE_PATH
    with open(FILE_PATH, "r+") as file:
        content = file.read()
        if player in content:
            content = content.split("\n")
            players = {
                key.strip() : score if player.strip().lower() == key.strip().lower() else value.strip()
                for line in content
                if ":" in line
                for key, value in [line.split(":")]
            }
            
            file.seek(23)
            for key, value in players.items():
                file.write(f"{key:<10}: {value:<10}\n")
                
        else:
            file.write(f"{player:<10}: {score:<10}\n")
            
        

def read_scores():
    with open(FILE_PATH, "r") as file:
        data = file.readlines()
    
    for line in data:
        print(" ".join(line.strip()))