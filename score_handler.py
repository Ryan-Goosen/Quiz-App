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


def update_score(player, score, amount_questions):
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
                file.write(f"{key:<10}: {value:<10}/{amount_questions}\n")
                
        else:
            file.write(f"{player:<10}: {score:<10}/{amount_questions}\n")
            
def read_scores():
    os.system('cls')
    check_file_exists(LEADERBOARD_PATH)
    with open(LEADERBOARD_PATH, "r") as file:
        data = file.readlines()
    
    for line in data:
        print(" ".join(line.strip()))

    while True:
        user_input = input('Type "Done" to continue: ')
        if user_input or user_input.strip() == "":
            break


def settings():
    os.system('cls')
    defaults = get_settings()
    print("\nWhich settings would you like to change?: ")
    for key, value in defaults.items():
        os.system('cls')
        print(f"Category: {key.capitalize()}\nValue: {value}\n")
        if key == "amount":
            print("The amount of questions you would like to answer.\nPick a number between 10 and 50.")
            while True:
                user_input = str(input(": "))
                if user_input.strip() == "":
                        break
                try:
                    user_input = int(user_input)
                    if not 10 <= choice <= 50:
                        print(f"Pick a number between 10 & 50, {user_input} is over/under the limit.")
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
                user_input = str(input(": "))
                if user_input.strip() == "":
                    break
                try:
                    user_input = int(user_input)
                    if 1 <= user_input <= len(data['trivia_categories']) + 1:
                        break
                    else:
                        print(f"Pick a number between 1 & {len(data['trivia_categories']) + 1}, {user_input} is over/under the limit.")
                except:
                    print("Please enter a number")

            user_input = data['trivia_categories'][user_input-1]['id'] if user_input.strip() != "" else value

        elif key == "difficulty":   
            while True:
                print("Options are:\n1. Easy    | 2. Medium     | 3. Hard")
                user_input = str(input(": "))
                if user_input.strip() == "":
                    break
                try:
                    user_input = int(user_input)
                    if 1 <= user_input <= 3:
                        break
                    else:
                        print(f"Pick a number between 1 & 3.")
                except:
                    print("Please enter a number")

            user_input = 'easy' if user_input == 1 else 'medium' if user_input == 2 else "hard" if user_input == 3 else value
        else:
            while True:
                print("Options are:\n1. True/False    | 2. Multiple Choice")
                user_input = str(input(": "))
                if user_input.strip() == "":
                        break
                try:
                    choice = int(user_input)
                    if 1 <= choice <= 2:
                        break
                    else:
                        print(f"Pick a number between 1 & 2.")
                except:
                    print("Please enter a number")

            user_input = 'boolean' if user_input == 1 else 'multiple' if user_input == 1 else value
            

        defaults[key] = value if str(user_input) == "" or not str(user_input).isnumeric() else user_input
        write_to_file(defaults)

def check_file_exists(path):
    created = False
    if not os.path.exists(path):
        f = open(path, "x")
        print(f"File created at: {path}")
        created = True

        if "score_board" in path:
            with open(path, "w") as file:
                file.write(f"{'Player':<10}: {'Score':<10}\n\n")

        elif "settings" in path:
            write_to_file(DEFAULT_PARAMETERS)

    return created


def write_to_file(stuff):
    with open(SETTINGS_PATH, "w") as file:
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
