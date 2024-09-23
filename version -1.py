import tkinter as tk
from tkinter import ttk

# Question and Answer Data
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is the capital of China?", "options": ["New York", "Wellington", "Tokyo", "Beijing"], "answer": "Beijing"},
    {"question": "Which country is New Delhi in?", "options": ["USA", "Russia", "India", "Brazil"], "answer": "India"},
    {"question": "Which country is Dubai in?", "options": ["Soviet Union", "United Arab Emirates", "United States of America", "European Union"], "answer": "United Arab Emirates"},
]

# Index of current issues and the scores
current_question = 0
score = 0  # player's scores
# function to display the question with question numbers
def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):#enumerate function gives numbers to question
        buttons[i].config(text=option, state=tk.NORMAL)
    feedback_label.config(text="")

def check_answer(selected_option):
    global score
    correct_answer = questions[current_question]["answer"]
    if selected_option == correct_answer:
        feedback_label.config(text="Correct!", fg="green")
        score += 1  # +1 if correct
    else:
        feedback_label.config(text=f"Wrong! The correct answer is: {correct_answer}", fg="red")
    next_question()

def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        root.after(2500, show_question)
    else:
        feedback_label.config(text=f"Quiz Complete! Your score: {score}/{len(questions)}", fg="blue")  # show the final score
        for button in buttons:
            button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Quiz")
root.geometry("500x500")

# show question and label
question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

# option buttons
buttons = []
for i in range(4):
    btn = ttk.Button(root, text="", command=lambda i=i: check_answer(buttons[i].cget("text")))
    btn.pack(pady=10)
    buttons.append(btn)

# show feedback and label
feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=20)

# show the first question first
show_question()

root.mainloop()
