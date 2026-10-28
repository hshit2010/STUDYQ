import requests
import random

def get_amount(amount = 5):
    url = "https://opentdb.com/api.php"
    my_choices = {"amount":amount,
                    "type":"multiple"}

    respond = requests.get(url,params=my_choices)
    data = respond.json()

    formatted_quiz=[]

    for q in data["results"]:
        options = (q["incorrect_answers"])
        options.append(q["correct_answer"])
        random.shuffle(options)

        questions_dict = {
            "question":q["question"],
            "options":options,
            "answer":q["correct_answer"]
        }
        formatted_quiz.append(questions_dict)
        return formatted_quiz
