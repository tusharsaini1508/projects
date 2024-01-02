# import data
import requests
from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


url1 = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
url2 = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"         
url3 = "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard"
   
choice=input("Enter question type *Easy* *Medium* *Hard* ")
ch=choice.lower()
print(ch)
if ch == "easy":
    url=url1
elif ch == "medium":
    url=url2
elif ch == "hard":
    url=url3 
else:
    print("Enter valid input")          

print(url)  
data = fetch_data(url)

question_bank = []
# i = 0

# def level_function(data):
for questions in data["results"]:
    Question_text = questions["question"]
    Question_answer = questions["correct_answer"]
    new_question = Question(Question_text, Question_answer)
    question_bank.append(new_question)
    # print(question_bank[i].text)
    # i = i+1
 # print(question_bank[0].text)
newquiz = QuizBrain(question_bank)
while newquiz.still_have_question():
    newquiz.next_question()

print("You have completed the Quiz")
print(f"Your have final score was: {newquiz.score}/ {len(question_bank)}")
