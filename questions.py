import requests
from random import shuffle
from html import unescape

API_LINK = r"https://opentdb.com/api.php?"

class GetQuestions:
    def __init__(self, parameters):
        parameters = {
            item : val
            for item, val in sorted(parameters.items())
            if val != 0
        }
        response = requests.get(API_LINK, params=parameters)
        response.raise_for_status()
        data = response.json()
        self.question_data = data['results']
 
class Question:
    def __init__(self, question, answer, options):
        self.question = unescape(question)
        self.answer = answer
        shuffle(options)
        shuffle(options)
        self.options = [unescape(item) for item in options]