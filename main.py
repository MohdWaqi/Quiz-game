from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for number in question_data:
    new = Question(number["text"], number["answer"])
    question_bank.append(new)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.number}")