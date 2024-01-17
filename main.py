from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    ques = question["question"]
    ques_ans = question["correct_answer"]
    new_question = Question(ques, ques_ans)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)
quiz = True
while brain.check_qes_limit():
    brain.next_question()
    brain.check_ans()
