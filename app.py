"""Set up the app.py file with routes for the homepage and quiz functionality"""

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from database import DB_NAME
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Function to establish database connection
db_connection = lambda: sqlite3.connect(DB_NAME)

@app.route('/')
def home():
    """Renders the homepage with quiz options."""
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Handles the quiz display and answer submission."""
    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        # Retrieve user's answer and corresponding question ID
        question_id = request.form.get('question_id')
        user_answer = request.form.get('user_answer').strip().lower()
        
        # Fetch the correct answer from the database
        cursor.execute("SELECT answer FROM questions WHERE id = ?", (question_id,))
        correct_answer = cursor.fetchone()[0].strip().lower()
        
        # Determine if the answer is correct
        score = 1 if user_answer == correct_answer else 0
        
        # Store the attempt in the database
        cursor.execute("INSERT INTO attempts (question_id, date, score) VALUES (?, datetime('now'), ?)", (question_id, score))
        conn.commit()
        conn.close()
        
        # Render the result template with feedback
        return render_template('result.html', correct=score == 1, correct_answer=correct_answer)
    
    # Retrieve a random question from the database
    cursor.execute("SELECT id, question FROM questions ORDER BY RANDOM() LIMIT 1")
    question = cursor.fetchone()
    conn.close()
    
    # Render the quiz template with the selected question
    return render_template('quiz.html', question=question)

@app.route('/analytics')
def analytics():
    """Displays quiz statistics."""
    conn = db_connection()
    cursor = conn.cursor()
    
    # Fetch total number of attempts
    cursor.execute("SELECT COUNT(*) FROM attempts")
    total_attempts = cursor.fetchone()[0]
    
    # Fetch total number of correct answers
    cursor.execute("SELECT COUNT(*) FROM attempts WHERE score = 1")
    correct_answers = cursor.fetchone()[0]
    
    # Calculate success rate
    success_rate = (correct_answers / total_attempts * 100) if total_attempts > 0 else 0
    conn.close()
    
    # Render the analytics template with statistics
    return render_template('analytics.html', total_attempts=total_attempts, correct_answers=correct_answers, success_rate=success_rate)

#To add questions
@app.route('/add_question', methods=['GET', 'POST'])
def add_question_view():
    """Allows users to add questions via a web form."""
    if request.method == 'POST':
        question_text = request.form.get('question')
        answer = request.form.get('answer')
        category = request.form.get('category')

        if question_text and answer:
            from database import add_question
            add_question(question_text, answer, category)
            return redirect(url_for('home'))  # Redirect back to the homepage

    return render_template('add_question.html')

#To delete questions
@app.route('/delete_question', methods=['GET', 'POST'])
def delete_question_view():
    """Allows users to delete questions from the database."""
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        question_id = request.form.get('question_id')
        if question_id:
            cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
            conn.commit()

    # Fetch all questions to display in the delete form
    cursor.execute("SELECT id, question FROM questions")
    questions = cursor.fetchall()
    conn.close()
    
    return render_template('delete_question.html', questions=questions)


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
