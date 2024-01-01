import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
# i = 0
for questions in question_data:
    Question_text = questions["text"]
    Question_answer = questions["answer"]
    new_question = Question(Question_text, Question_answer)
    question_bank.append(new_question)
    # print(question_bank[i].text)
    # i = i+1
# print(question_bank[0].text)
newquiz = QuizBrain(question_bank)
newquiz.next_question()
