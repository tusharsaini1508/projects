class QuizBrain:
    def __init__(self, qlist):
        self.question_Number = 0
        self.question_list = qlist
        self.score = 0

    def still_have_question(self):
        if self.question_Number < len(self.question_list):
            return True
        else:
            False


    def next_question(self):
        current_question = self.question_list[self.question_Number]
        self.question_Number += 1
        user_answer = input(f"Q.no {self.question_Number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right")
        else:
            print("That's Wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your Current Score is: {self.score}/{self.question_Number}")
        print("\n")

