class QuizBrain:
    def __init__(self, qlist):
        self.question_Number = 0
        self.question_list = qlist
        # self.answer_Number = 0
        # self.answer_list = qlist
    
    def matched(self,ch):
        current_answer = self.question_list[self.question_Number]
        answer = current_answer.answer
        # print(answer)
        answer2 = answer == ch
        # print(answer2)
        return answer2
        
    
    def next_question(self):
        
        for _ in self.question_list: 
            Total_point=0
            current_question = self.question_list[self.question_Number]
            ch=input(f"Q.no {self.question_Number + 1}: {current_question.text} (True/False)")
            answer=self.matched(ch)
            if answer:
                print("oky")
                self.question_Number += 1
                Total_point
                
                print(Total_point)
            else:
                print("not okay")
                self.question_Number += 1
                Total_point += 1
                print(Total_point)
        

        