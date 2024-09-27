import tkinter as tk
from tkinter import ttk
import os

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
    {"question": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "What is the largest desert in the world?", "options": ["Sahara", "Arabian", "Gobi", "Kalahari"], "answer": "Sahara"},
    {"question": "Which country has the most population?", "options": ["India", "China", "USA", "Indonesia"], "answer": "China"},
    {"question": "Which continent is the country of Brazil located in?", "options": ["Africa", "Asia", "Europe", "South America"], "answer": "South America"},
    {"question": "What is the smallest country in the world by area?", "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "answer": "Vatican City"},
    {"question": "Which is the largest ocean in the world?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},
    {"question": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "answer": "Canberra"},
    {"question": "Mount Everest is located in which two countries?", "options": ["India and China", "Nepal and China", "Bhutan and India", "Pakistan and Afghanistan"], "answer": "Nepal and China"},
    {"question": "Which country has the largest land area?", "options": ["Canada", "China", "United States", "Russia"], "answer": "Russia"},
    {"question": "What is the longest mountain range in the world?", "options": ["Himalayas", "Rocky Mountains", "Andes", "Alps"], "answer": "Andes"}
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

# Get the directory where the current script is located and create files in the same directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "record.txt")

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
def check_answer(index):
    global current_question, player
    select_option = buttons[index].cget("text")  # Get current button's text
    correct_answer = questions[current_question]['answer']  # Get correct answer

    if select_option == correct_answer:
        player.calc_score()  # Update score if answer is correct
        result_label.config(text="Correct!", fg="green")  # Show correct message
    else:
        result_label.config(text=f"Wrong!\nThe correct answer is: {correct_answer}!", fg="red")  # Show wrong message

# Function to show final score
def show_final_score():
    total_questions = len(questions)
    percentage = (player.score / total_questions) * 100  # Calculate percentage score
    
    # Determine color based on percentage score
    if percentage >= 80:
        color = "green"  # High score in green
    elif 50 <= percentage < 80:
        color = "orange"  # Medium score in orange
    else:
        color = "red"  # Low score in red

    result_label.config(text=f"Quiz complete!\nYour final score is: {player.score} / {total_questions}\n{percentage:.2f}%", fg=color)  
    record(player.name, player.age, player.score, percentage)  # Record the result

    question_label.pack_forget()  # Hide question label
    button_frame.pack_forget()  # Hide answer buttons


# Function to record results to a file
def record(name, age, score, percentage):
    try:
        with open(file_path, "a") as f:
            f.write(f"--------------\nName: {name}\nAge: {age}\nScore: {score}\nPercentage: {percentage:.2f}%\n")
        print(f"Results recorded successfully for {name}.")  # Debugging output
    except Exception as e:
        print(f"Error writing to file: {e}")  # Print error message if failed

# Set up the main application window
root = tk.Tk()
root.title("Quiz")
root.geometry("700x300")  # Set window size

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

# Create a frame to hold buttons with consistent spacing
button_frame = tk.Frame(root)  # Create a single frame to hold all buttons
button_frame.pack(pady=20)  # Padding around the entire button frame

for i in range(4):
    btn = ttk.Button(button_frame, text="", command=lambda i=i: check_answer(i))
    btn.pack(pady=10, fill="x")  # Add pady between buttons and fill width-wise
    buttons.append(btn)

# Initially hide question label and buttons
question_label.pack_forget()
button_frame.pack_forget()

# Function to show quiz questions
def show_quiz():
    global current_question
    question_label.config(text=questions[current_question]["question"])  # Set question text
    for i, option in enumerate(questions[current_question]["options"]):
        buttons[i].config(text=option, state=tk.NORMAL)  # Enable buttons and set options

    question_label.pack()  # Show question label
    button_frame.pack()  # Show the button frame (which contains buttons)

# Function to check selected answer
def check_answer(i):
    global current_question, player
    select_option = buttons[i].cget("text")  # Get current button's text
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
        root.after(2000, show_final_score)  # Show final score after 2 seconds

# Start the main loop
root.mainloop()

