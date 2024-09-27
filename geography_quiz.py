import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow modules for image handling

# List of questions and answers
questions = [
    {
        "question": "Who was the first President of the United States?",
        "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "Thailand", "Korea"],
        "answer": "Japan"
    },
    {
        "question": "What is the largest continent on Earth?",
        "options": ["Africa", "Asia", "North America", "South America"],
        "answer": "Asia"
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
        "answer": "Tokyo"
    },
    {
        "question": "Which desert is the largest in the world?",
        "options": ["Sahara", "Arabian", "Gobi", "Kalahari"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "answer": "Vatican City"
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "India", "Russia", "United States"],
        "answer": "Canada"
    },
    {
        "question": "What mountain range separates Europe and Asia?",
        "options": ["Andes", "Rocky Mountains", "Himalayas", "Ural Mountains"],
        "answer": "Ural Mountains"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which country is known as the Land of the Maple Leaf?",
        "options": ["USA", "Australia", "Canada", "New Zealand"],
        "answer": "Canada"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    }
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Quiz")  # Set the title of the window
        self.master.geometry("700x300")  # Set the size of the window
        self.current_question = 0  # Initialize the current question index
        self.score = 0  # Initialize the score

        # Load and set the background image
        self.background_image = Image.open("E:/DIP/y13/91907/version - 4/image/Geography.png")  # Use Pillow to open the image
        self.background_image = self.background_image.resize((700, 300), Image.LANCZOS)  # Resize the image
        self.background_photo = ImageTk.PhotoImage(self.background_image)  # Convert to a format usable by Tkinter

        # Create a label to display the background image
        background_label = tk.Label(master, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)  # Fill the entire window

        # Create a label for the question text
        self.question_label = tk.Label(master, text="", font=("Arial", 14), bg="white")  # Set background color for the question
        self.question_label.pack(pady=20)  # Add padding around the question label

        # Create a frame for the answer buttons using grid layout
        self.button_frame = tk.Frame(master, bg="white")  # Frame to hold buttons
        self.button_frame.pack(pady=20)  # Add padding around the button frame

        self.answer_buttons = []  # List to hold the answer buttons
        for option in range(4):  # Create four buttons for the answer options
            btn = tk.Button(self.button_frame, text="", font=("Arial", 12), 
                            command=lambda option=option: self.check_answer(self.answer_buttons[option].cget("text")))
            btn.grid(row=0, column=option, padx=10)  # Arrange buttons in a row
            self.answer_buttons.append(btn)  # Add button to the list

        # Create a label for displaying results
        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="white")
        self.result_label.pack(pady=20)  # Add padding around the result label

        self.show_question()  # Show the first question

    def show_question(self):
        if self.current_question < len(questions):  # Check if there are more questions
            question = questions[self.current_question]  # Get the current question
            self.question_label.config(text=question["question"])  # Update the question label
            for i, option in enumerate(question["options"]):  # Update the answer buttons with options
                self.answer_buttons[i].config(text=option, state=tk.NORMAL)  # Enable the buttons
            self.result_label.config(text="")  # Clear the result label
        else:
            self.show_final_score()  # Show the final score if all questions have been answered

    def check_answer(self, selected_option):
        correct_answer = questions[self.current_question]["answer"]  # Get the correct answer
        if selected_option == correct_answer:  # Check if the selected option is correct
            self.score += 1  # Increment the score
            self.result_label.config(text="Correct!", fg="green")  # Display correct message
        else:
            self.result_label.config(text=f"Wrong! The correct answer is: {correct_answer}", fg="red")  # Display wrong message

        self.current_question += 1  # Move to the next question
        for btn in self.answer_buttons:
            btn.config(state=tk.DISABLED)  # Disable the answer buttons
        self.master.after(2000, self.show_question)  # Show the next question after 2 seconds

    def record_score(self, score, percentage):
        with open("players.txt", "a") as f:  # Open the file in append mode
            f.write(f"\n-------\nSubject: Geography\nScore: {score}\nPercentage: {percentage:.2f}%\n-------\n")  # Record the score and percentage

    def show_final_score(self):
        percentage = (self.score / len(questions)) * 100  # Calculate the percentage score
        self.record_score(self.score, percentage)  # Record the final score

        self.question_label.config(text="Quiz complete!")  # Update the question label for completion
        for btn in self.answer_buttons:
            btn.pack_forget()  # Remove answer buttons from the display
        self.result_label.config(text=f"Your final score is: {self.score}/{len(questions)}")  # Display the final score

        self.master.after(5000, self.master.destroy)  # Close the window after 5 seconds

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = QuizApp(root)  # Initialize the quiz application
    root.mainloop()  # Start the Tkinter main loop
