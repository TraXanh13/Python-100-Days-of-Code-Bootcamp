import question_model as qm
import data
import quiz_brain as qb

question_bank = []

for question in data.question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = qm.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = qb.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")