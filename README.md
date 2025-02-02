# Python Quiz Application 

This is a Flask-based quiz application that allows users to test their knowledge with predefined questions. The project uses SQLite for data storage and Bootstrap for styling.

## Features

- Web-based quiz system using Flask
- Stores questions and answers in an SQLite database
- Option to add, delete, and modify questions
- Predefined questions can be imported from a CSV file
- Results tracking to monitor performance
- Responsive design using Bootstrap

## Installation

### 1. Download the Project

You can get the project in two ways:

#### **Option 1: Clone with Git**

```sh
git clone https://github.com/Pythonamy/thepythonquiz.git
cd thepythonquiz
```

#### **Option 2: Download as a ZIP**
```sh
1. Go to [GitHub Repository](https://github.com/Pythonamy/thepythonquiz).
2. Click **"Code" → "Download ZIP"**.
3. Extract the ZIP file to your preferred location.
4. Open the project folder in your IDE (e.g., VS Code, PyCharm).
```

### 2. Install Dependencies

Ensure you have Python installed, then run:

```sh
pip install -r requirements.txt
```

### 3. Initialize the Database

Run the following command to create the database and tables:

```sh
python database.py
```

### 4. Import Default Questions (Optional)

To load predefined questions from `questions.csv`, run:

```sh
python import_questions.py
```

### 5. Run the Application

Start the Flask application with:

```sh
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## How to Use

### Adding a Question

1. Click on **"Add a Question"** in the menu.
2. Enter the question, answer, and optional category.
3. Submit the form to save the question.

### Deleting a Question

1. Click on **"Delete a Question"** in the menu.
2. Select a question from the dropdown list.
3. Click **"Delete"** to remove the question from the database.

### Taking the Quiz

1. Click **"Start Quiz"** to begin.
2. Answer the displayed question and submit your response.
3. The system will check your answer and display the result.
4. You can continue answering more questions or return to the main menu.

### Viewing Analytics

1. Click **"View Analytics"** to see statistics on total attempts, correct answers, and overall success rate.

### Exporting Questions

To export the current set of questions to a CSV file:

```sh
python export_questions.py
```

## License

This project is open-source and can be modified or distributed as needed.




