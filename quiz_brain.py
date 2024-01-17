class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_input = input(f"Q.{self.question_number}: {self.current_question.text} (True / False): ")
    def check_ans(self):
        if self.user_input == self.current_question.answer:
            self.score += 1
            print("You are Right!")
        else:
            print("You are Wrong!")

        print(f"The correct answer is {self.current_question.answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
    def check_qes_limit(self):
        return self.question_number < len(self.question_list)

            