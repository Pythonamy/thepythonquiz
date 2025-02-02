"""Implement functions to create tables and manage questions"""

import sqlite3

#Define the name of the SQLite database file 
DB_NAME = "thepythonquiz.db"                   

#Creates the necessary tables if they do not exist.
#This records which question was answered, when, and if it was correct
def create_tables():                            
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT
        )
    ''')

    #Create table for tracking quiz attempts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    ''')
    
    conn.commit()
    conn.close()

#Insert a new question along with its answer and optional category
def add_question(question, answer, category=None):
    """Adds a new question to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questions (question, answer, category) VALUES (?, ?, ?)
    ''', (question, answer, category))
    conn.commit()
    conn.close()

#Remove the question with the specified ID
def delete_question(question_id):
    """Deletes a question from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM questions WHERE id = ?
    ''', (question_id,))
    conn.commit()
    conn.close()

#Select all questions and return them as a list
def get_all_questions():
    """Retrieves all questions from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM questions''')
    questions = cursor.fetchall()
    conn.close()
    return questions

#Initialize the database and create tables if they don't exist
if __name__ == "__main__":   
    create_tables()
    print("Database and tables initialized.")
