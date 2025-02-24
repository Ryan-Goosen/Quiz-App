import os
import requests

LEADERBOARD_PATH = "score_board.txt"
SETTINGS_PATH = "settings.txt"
DEFAULT_PARAMETERS = {
    "amount" : 10,
    "category" : 0,
    "difficulty" : 0,
    "type" : 0,
}


def update_score(player, score):
    check_file_exists(LEADERBOARD_PATH)
    with open(LEADERBOARD_PATH, "r+") as file:
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
    check_file_exists(LEADERBOARD_PATH)
    with open(LEADERBOARD_PATH, "r") as file:
        data = file.readlines()
    
    for line in data:
        print(" ".join(line.strip()))


def settings():
    defaults = get_settings()
    print("\nWhich settings would you like to change?: ")
    for key, value in defaults.items():
        os.system('cls')
        print(f"Category: {key.capitalize()}\nValue: {value}\n")
        if key == "amount":
            print("The amount of questions you would like to answer.\nPick a number between 10 and 50.")
            while True:
                user_input = input(": ")
                if user_input.strip() == "":
                        break
                try:
                    choice = int(user_input)
                    if not 10 <= choice <= 50:
                        print(f"Pick a number between 10 & 50, {choice} is over/under the limit.")
                    else:
                        break
                except:
                    print("Please enter a number")
        elif key == "category":
            response = requests.get("https://opentdb.com/api_category.php")
            response.raise_for_status()
            data = response.json()
            for pos, val in enumerate(data['trivia_categories']):
                print(f"{f'{pos+1}':<10}: {f'{val['name']}':<10}\n")

            while True:
                user_input = input(": ")
                if user_input.strip() == "":
                        break
                try:
                    choice = int(user_input)
                    if 1 <= choice <= len(data['trivia_categories']) + 1:
                        break
                    else:
                        print(f"Pick a number between 1 & {len(data['trivia_categories']) + 1}, {choice} is over/under the limit.")
                except:
                    print("Please enter a number")

            user_input = data['trivia_categories'][choice-1]['id']
        elif key == "difficulty":   
            while True:
                print("Options are:\n1. Easy    | 2. Medium     | 3. Hard")
                user_input   

        defaults[key] = value if user_input == "" or not user_input.isnumeric() else user_input
        write_to_file(defaults)

def check_file_exists(path):
    created = False
    if not os.path.exists(path):
        f = open(path, "x")
        print(f"File created at: {path}")
        created = True

        if "score_board" in path:
            with open(path, "w") as file:
                file.write(f"{'Player':<10}: {'Score':<10}\n")

        elif "settings" in path:
            write_to_file(DEFAULT_PARAMETERS)

    return created


def write_to_file(stuff):
    with open(SETTINGS_PATH, "a") as file:
            for key, value in stuff.items():
                file.write(f"{key} : {value}\n")   


def get_settings() -> dict:
    if check_file_exists(SETTINGS_PATH):
        dict_version = DEFAULT_PARAMETERS
    else:
        with open(SETTINGS_PATH, "r") as file:
                dict_version = {
                    key.strip() : value.strip()
                    for item in file.readlines()
                    if ":" in item
                    for key, value in [item.split(":")]
                }
    
    return dict_version