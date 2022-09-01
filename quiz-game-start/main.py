from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

while quiz_brain.still_has_question():
    quiz_brain.next_question()
print(f"\nYou've completed the quiz\nYour final score was: {quiz_brain.score}/{quiz_brain.question_number}")

