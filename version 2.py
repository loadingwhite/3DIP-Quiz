import tkinter as tk
from tkinter import ttk

# List of quiz questions, options, and correct answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is the capital of China?", "options": ["New York", "Wellington", "Tokyo", "Beijing"], "answer": "Beijing"},
    {"question": "Which Federation is Dubai in?", "options": ["Soviet Union", "United Arab Emirates", "United States of America", "European Union"], "answer": "United Arab Emirates"},
    {"question": "Where is New York located?", "options": ["USA", "Russia", "India", "Brazil"], "answer": "USA"},
    {"question": "Which country is New Delhi in?", "options": ["Japan", "Russia", "India", "Egypt"], "answer": "India"},
    {"question": "Where is Brasília located?", "options": ["USA", "Brazil", "India", "United Kingdom"], "answer": "Brazil"},
    {"question": "Which country is Rio de Janeiro in?", "options": ["Portugal", "New Zealand", "China", "Brazil"], "answer": "Brazil"},
    {"question": "Which country is Hawaii in?", "options": ["Australia", "United Kingdom", "USA", "China"], "answer": "USA"},
    {"question": "Which continent is Argentina in?", "options": ["Asia", "Antarctica", "South America", "Europe"], "answer": "South America"},
    {"question": "Where is the 'Svalbard Global Seed Vault'?", "options": ["Greenland", "Norway", "Iceland", "Russia"], "answer": "Norway"},
    {"question": "Which continent is the 'Independent State of Papua New Guinea' in?", "options": ["India", "Oceania", "Asia", "Australia"], "answer": "Oceania"},
    {"question": "Which country is Papua in?", "options": ["India", "New Guinea", "Indonesia", "Australia"], "answer": "Indonesia"},
    {"question": "Where is the Amazon Rainforest located?", "options": ["Amazon", "Mexico", "South America", "Australia"], "answer": "South America"},
    {"question": "Where is Ethiopia located?", "options": ["Africa", "Oceania", "Asia", "Europe"], "answer": "Africa"},
    {"question": "Where is Greece located?", "options": ["Europe", "Oceania", "Asia", "North America"], "answer": "Europe"},
    {"question": "Where is Las Vegas located?", "options": ["Nevada", "Macau", "Chicago", "Amman"], "answer": "Nevada"},
]

# Class to represent a player
class Player:
    def __init__(self, name, age, score=0):
        self.name = name  # Player's name
        self.age = age    # Player's age
        self.score = score  # Player's score

    # Method to calculate score
    def calc_score(self):
        self.score += 1  # Increment score by 1

# Initialize current question index and player
current_question = 0
player = None

# Function to get player information
def get_player_info():
    global player  
    name = name_entry.get()  # Get name from input
    age = age_entry.get()    # Get age from input

    # Validate age input
    if not age.isdigit():
        result_label.config(text="Please enter a valid age!", fg="red")  # Show error message
        return
    
    age = int(age)

    # Check age eligibility
    if 12 <= age <= 20:
        player = Player(name, age)  # Create player object
        result_label.config(text=f"Hello, {name}!", fg="green")  # Welcome message
        hide_identity_inputs()  # Hide input fields
        show_quiz()  # Show quiz questions

    elif age > 20:
        result_label.config(text=f"Sorry {name}, you're too old to play this game now.", fg="blue")
        
    else:
        result_label.config(text="Sorry kid, you must be at least 12 years old to play.", fg="blue")

# Function to hide identity input fields
def hide_identity_inputs():
    name_label.pack_forget()
    age_label.pack_forget()
    name_entry.pack_forget()
    age_entry.pack_forget()
    submit_button.pack_forget()
    
# Function to show quiz questions
def show_quiz():
    global current_question
    question_label.config(text=questions[current_question]["question"])  # Set question text
    for i, option in enumerate(questions[current_question]["options"]):
        buttons[i].config(text=option, state=tk.NORMAL)  # Enable buttons and set options

    question_label.pack()  # Show question label
    for button in buttons:
        button.pack()  # Show answer buttons

# Function to check selected answer
def check_answer(select_option):
    global current_question, player
    correct_answer = questions[current_question]['answer']  # Get correct answer

    if select_option == correct_answer:
        player.calc_score()  # Update score if answer is correct
        result_label.config(text="Correct!", fg="green")  # Show correct message
    else:
        result_label.config(text=f"Wrong!\nThe correct answer is: {correct_answer}!", fg="red")  # Show wrong message
    
    current_question += 1  # Move to the next question
    if current_question < len(questions):
        root.after(2000, show_quiz)  # Show next question after 2 seconds
    else:
        result_label.config(text=f"Quiz complete!\nYour final score is: {player.score}", fg="blue")  
        question_label.pack_forget()  # Hide question label
        for button in buttons:
            button.pack_forget()  # Hide answer buttons

# Set up the main application window
root = tk.Tk()
root.title("Quiz")
root.geometry("500x500")  # Set window size

# Input for player name
name_label = tk.Label(root, text='Please enter your name:')
name_label.pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

# Input for player age
age_label = tk.Label(root, text='Please enter your age:')
age_label.pack(pady=10)
age_entry = tk.Entry(root)
age_entry.pack(pady=10)

# Button to submit player info
submit_button = ttk.Button(root, text="Enter", command=get_player_info)
submit_button.pack(pady=20)

# Label to display results
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Label to display quiz questions
question_label = tk.Label(root, text="", font=("Arial", 14))

# List to hold answer buttons
buttons = []
for i in range(4):
    btn = ttk.Button(root, text="", command=lambda i=i: check_answer(buttons[i].cget("text")))  # Use closure to capture button index
    btn.pack(pady=10)
    buttons.append(btn)

# Initially hide question label and buttons
question_label.pack_forget()
for button in buttons:
    button.pack_forget()

# Start the main loop
root.mainloop()
