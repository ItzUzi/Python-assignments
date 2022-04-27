# Made a test its own class to hold all questions in one organized place
class Test:
    def __init__(self, questions):
        self.question_list = questions
        self.counter = 0
        self.question_amount = len(questions)

    def take_test(self):    # Uses the question class function to ask question
        question_count = 1  # records if answer is correct or not
        for question in self.question_list:
            print("Question %d:" % question_count)
            self.counter += question.ask_question()
            question_count += 1
            print()

    def get_correct_answers(self):
        return self.counter

    def get_question_amount(self):
        return self.question_amount


# class that holds both question and answers to question
class Question:
    def __init__(self, new_question):
        self.question = new_question
        self.answers = list()   # answers are held in list
        self.correct_answer = ''

    def set_answers(self, answer_list, correct_option):
        self.answers = answer_list              # sets all possible answers for question
        self.correct_answer = correct_option    # sets which answer is correct

    def ask_question(self):
        print(self.question)
        for i in range(len(self.answers)):
            print("%d). %s" % (i + 1, self.answers[i]))
        answer = input("Enter your answer: ")
        if answer == self.correct_answer:       # checks if input matches with correct answer
            return 1
        else:
            return 0


def main():
    q1 = Question("Where is Cal Poly Pomona Located")                   # creates Question object with question string
    q1_correct_answer = "California"                                    # sets correct answer to question
    q1_answers = "Texas", q1_correct_answer, "Nevada", "Washington"     # sets all answers available for question
    q1.set_answers(q1_answers, q1_correct_answer)

    q2 = Question("On your student records system, what does CSU stand for?")
    q2_correct_answer = "California State Universities"
    q2_answers = q2_correct_answer, "Colorado State Universities", \
                 "Color Sparkling Unicorn", "Canadian Swan Upping"
    q2.set_answers(q2_answers, q2_correct_answer)

    q3 = Question("What is 2*10e1?")
    q3_correct_answer = "20"
    q3_answers = "10", "100", q3_correct_answer, "200"
    q3.set_answers(q3_answers, q3_correct_answer)

    q4 = Question("Does 3 ^ 2 = 6?")
    q4_correct_answer = "False"
    q4_answers = "True", q4_correct_answer
    q4.set_answers(q4_answers, q4_correct_answer)

    q5 = Question("Which one of these is not a dragon type")
    q5_correct_answer = "Gyarados"
    q5_answers = "Salamence", q5_correct_answer, "Flygon", "Altaria"
    q5.set_answers(q5_answers, q5_correct_answer)

    test_questions = q1, q2, q3, q4, q5     # creates list full of questions
    test = Test(test_questions)             # Creates test object with questions
    test.take_test()                        # goes through test
    print("You got %d out of %d" % (test.get_correct_answers(),
                                    test.get_question_amount()))


if __name__ == '__main__':
    main()

"""
Question 1:
Where is Cal Poly Pomona Located
1). Texas
2). California
3). Nevada
4). Washington
Enter your answer: California

Question 2:
On your student records system, what does CSU stand for?
1). California State Universities
2). Colorado State Universities
3). Color Sparkling Unicorn
4). Canadian Swan Upping
Enter your answer: Abra

Question 3:
What is 2*10e1?
1). 10
2). 100
3). 20
4). 200
Enter your answer: 20

Question 4:
Does 3 ^ 2 = 6?
1). True
2). False
Enter your answer: False

Question 5:
Which one of these is not a dragon type
1). Salamence
2). Gyarados
3). Flygon
4). Altaria
Enter your answer: Gyarados

You got 4 out of 5
"""