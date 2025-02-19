from questions import GetQuestions, Question
from random import randint
from ui import cli_header, cli_game_over
from time import sleep
from score_handler import *
import ast
import os

SCORE = 0
# question = GetQuestions().question_data
# formatted_question = [Question(question=item['question'] , answer=item['correct_answer'] , options=item['incorrect_answers'] + [item['correct_answer']]) for item in question]

print(cli_header)


def game():
    with open('multiple.txt', 'r') as file:
        data = file.readlines()

    formatted_question = {}
    for pos,item in enumerate(data):
        item = ast.literal_eval(item)
        formatted_question[pos+1] = Question(question=item['question'] , answer=item['correct_answer'] , options=item['incorrect_answers'] + [item['correct_answer']])

    # CLI VERSION


    for key,question in formatted_question.items():
        print(f"\n{key}. QUESTION:\n", question.question)
        print("OPTIONS: \n", " / ".join(question.options))
        user_answer = input("\n")
        if user_answer == question.answer:
            SCORE += 1
            print("That was correct!\nCurrent Score", SCORE)
        else:
            print("That was incorrect!\nCurrent Score", SCORE)
        # sleep(1)
        os.system('cls')

    print(cli_game_over)
    username = input("Please enter your gamer tag:\n")
    update_score(username, SCORE)

def main():
    option = input("Please select what you want to do:\n1. Play a Game    |   2. View Leaderboard\n")
    os.system('cls')
    
    if int(option) == 1:
        game()
    else:
        read_scores()

        
if __name__ == "__main__":
    main()