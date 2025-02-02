"""for command-line quiz mode"""

import sqlite3
import random

from database import DB_NAME

class Quiz:                                                                                 #Handles the quiz functionality including loading questions, presenting them, and storing results.
    def __init__(self):                                                                     #Initializes the quiz by loading questions from the database.
        self.questions = self.load_questions()

    def load_questions(self):                                                               #Retrieves all questions from the database and returns them as a list.
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, question, answer FROM questions")                        #Select all questions along with their IDs and answers
        questions = cursor.fetchall()
        conn.close()
        return questions

    def start(self):                                                                        #Begins a quiz session by asking each question and evaluating responses.
        if not self.questions:
            print("No questions available. Please add questions to the database.")
            return

        for question in random.sample(self.questions, len(self.questions)):                 #Randomize question order
            q_id, q_text, q_answer = question
            user_answer = input(f"{q_text}\nYour answer: ")
            self.evaluate_answer(q_id, user_answer, q_answer)

    def evaluate_answer(self, q_id, user_answer, correct_answer):                           # Checks the user's answer and records the result in the database.
        score = 1 if user_answer.strip().lower() == correct_answer.strip().lower() else 0   # Normalize answers by stripping whitespace and converting to lowercase
        
        # Store the result in the attempts table
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO attempts (question_id, date, score) VALUES (?, datetime('now'), ?)
        ''', (q_id, score))
        conn.commit()
        conn.close()

        # Provide feedback to the user
        print("Correct!" if score else f"Wrong! The correct answer was: {correct_answer}")

if __name__ == "__main__":                                                                  # Create a new quiz instance and start the quiz
    quiz = Quiz()
    quiz.start()