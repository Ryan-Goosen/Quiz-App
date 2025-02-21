from questions import GetQuestions, Question
from random import randint, shuffle
from ui import cli_header, cli_game_over
from time import sleep
from score_handler import *

import ast
import os

SCORE = 0

def store_questions() -> dict:
    with open('multiple.txt', 'r') as file:
        data = file.readlines()

    # data = GetQuestions().question_data

    formatted_question = {
        pos+1 : Question(question=ast.literal_eval(item)['question'] , answer=ast.literal_eval(item)['correct_answer'] , options=ast.literal_eval(item)['incorrect_answers'] + [ast.literal_eval(item)['correct_answer']])
        for pos,item in enumerate(data)
    }
    
    return formatted_question

def get_questions(question:object, mode='cli') -> str:
    # q_n_a = {key+1:val for key, val in enumerate(question.options)}
    # if mode is 'cli':
    #     options = ""
    #     for key,val in q_n_a.items():
    #         options += f"{key} : {val}\n"
    #     return options
    # return q_n_a

    q_n_a = {key + 1: val for key, val in enumerate(question.options)}
    if mode is 'cli':
        options = ""
        columns = 2  
        max_len = len(str(len(q_n_a)))

        for idx, (key, val) in enumerate(q_n_a.items()):
            options += f"{key:<{max_len}}. {val:<20}"
            if (idx + 1) % columns == 0:
                options += "\n"
            else:
                options += " |    "

        options = options.rstrip(" | \n") + "\n"  # Add a newline at the end

        return options
    return q_n_a
        

def CLI_version(questions) -> None:
    global SCORE
    print(cli_header)

    for key,question in questions.items():
        options = get_questions(question)
        print(f"\n{key}. QUESTION:\n", question.question, "\n\nOptions:")
        print(options)

        user_answer = int(input(f"\nNum 1-{len(question.options)}: "))
        if question.options[user_answer-1] == question.answer:
            SCORE += 1
            print(f"That was correct!\nCurrent Score {SCORE}/{key}")
        else:
            print(f"That was incorrect!\nCurrent Score {SCORE}/{key}")
        # sleep(1)
        os.system('cls')

    print(cli_game_over)

    
def game():
    global SCORE

    questions = store_questions()
    CLI_version(questions)

    
    tag = input("Please enter your gamer tag:\n")
    update_score(tag, SCORE)

def main():
    option = input("Please select what you want to do:\n1. Play a Game    |   2. View Leaderboard\n")
    os.system('cls')
    
    if int(option) == 1:
        game()
    else:
        read_scores()

        
if __name__ == "__main__":
    main()