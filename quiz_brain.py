class QuizBrain:

    def __init__(self, question):
        self.number = 0
        self.list = question
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        text = input(f"Q.{self.number}: {current_question.text} (True/False)?: ")
        self.check_answer(text, current_question.solution)

    def check_answer(self, player, right_answer):
        if player == right_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {right_answer}")
        print(f"Your current score is {self.score}/{self.number}")
        print("\n")