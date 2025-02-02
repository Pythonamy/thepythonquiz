"""Generate reports on learning performance"""

import sqlite3
from database import DB_NAME

def get_quiz_statistics():
    """Retrieves quiz performance statistics from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Get total number of attempts
    cursor.execute("SELECT COUNT(*) FROM attempts")
    total_attempts = cursor.fetchone()[0]
    
    # Get total number of correct answers
    cursor.execute("SELECT COUNT(*) FROM attempts WHERE score = 1")
    correct_answers = cursor.fetchone()[0]
    
    # Calculate success rate
    success_rate = (correct_answers / total_attempts * 100) if total_attempts > 0 else 0
    
    conn.close()
    
    return {
        "total_attempts": total_attempts,
        "correct_answers": correct_answers,
        "success_rate": success_rate
    }

def display_statistics():
    """Displays the quiz statistics in a readable format."""
    stats = get_quiz_statistics()
    print("\nQuiz Statistics:")
    print(f"Total Attempts: {stats['total_attempts']}")
    print(f"Correct Answers: {stats['correct_answers']}")
    print(f"Success Rate: {stats['success_rate']:.2f}%")

if __name__ == "__main__":
    display_statistics()
