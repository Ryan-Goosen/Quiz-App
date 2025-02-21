from html import unescape
import requests
from random import shuffle

API_LINK = r"https://opentdb.com/api.php?"

class GetQuestions:
    def __init__(self, parameters={"amount" : 10,"category" : '23',}):
        response = requests.get(API_LINK, params=parameters)
        response.raise_for_status()
        data = response.json()
        self.question_data = data['results']
 
class Question:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        shuffle(options)
        shuffle(options)
        self.options = options