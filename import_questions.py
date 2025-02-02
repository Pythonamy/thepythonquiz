import csv
from database import add_question

def import_questions_from_csv(filename="questions.csv"):
    """Reads questions from a CSV file and adds them to the database."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                add_question(row["question"], row["answer"], row["category"])
        
        print("Questions imported successfully from CSV.")
    except FileNotFoundError:
        print(f"Error: {filename} not found. Make sure the file exists.")

if __name__ == "__main__":
    import_questions_from_csv()
