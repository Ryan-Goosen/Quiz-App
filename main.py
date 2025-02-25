from questions import GetQuestions, Question
from random import randint, shuffle
from ui import *
from time import sleep
from score_handler import *

import ast
import os

SCORE = 0

def get_questions() -> dict:
    parameters = get_settings()
    data = GetQuestions(parameters).question_data

    formatted_question = {
        pos + 1: Question(
            question=item["question"],
            answer=item["correct_answer"],
            options=item["incorrect_answers"] + [item["correct_answer"]]
        )
        for pos, item in enumerate(data)
        }

    return formatted_question

def display_questions(question:object, mode='cli') -> str:
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
    os.system('cls')
    print(quiz_start)
    count = 0
    for key,question in questions.items():
        options = display_questions(question)
        print(f"\nCurrent Score: {SCORE}/{count}\n{key}. QUESTION:\n", question.question, "\n\nOptions:")
        print(options)
        while True:
            user_answer = input(f"\nPick an option from 1-{len(question.options)}: ")
            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.options):
                    break
                print('Pick a valid option')
            except:
                print("Please enter a valid option.")

            
        if question.options[user_answer-1] == question.answer:
            SCORE += 1
            print(correct)
        else:
            print(incorrect)

        # sleep(1)
        count += 1
        os.system('cls')

    print(cli_game_over)
    print(f"FINAL SCORE WAS {SCORE}/{len(questions)}")

    
def game():
    global SCORE

    questions = get_questions()
    CLI_version(questions)

    
    tag = input("Please enter your gamer tag:\n")
    update_score(tag, SCORE, len(questions))

def main():
    while True:
        os.system('cls')
        print(cli_header)
        print("Please select what you want to do:\n1. Play a Game    |   2. View Leaderboard\n3. Settings\n")
        option = input(": ")
        try:
            if int(option) == 1:
                game()
            elif int(option) == 2:
                read_scores()
            elif int(option) == 3:
                defaults = settings()
        except:
            break
    
    os.system('cls')

        
if __name__ == "__main__":
    main()