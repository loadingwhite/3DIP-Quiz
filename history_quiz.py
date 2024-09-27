import tkinter as tk
from PIL import Image, ImageTk  # Importing the Pillow module for image handling

# List of questions and answers
questions = [
    {
        "question": "What year did World War II end?",
        "options": ["1945", "1944", "1939", "1950"],
        "answer": "1945"
    },
    {
        "question": "Which empire was known for its road system and trade?",
        "options": ["Roman Empire", "Ottoman Empire", "Mongol Empire", "British Empire"],
        "answer": "Roman Empire"
    },
    {
        "question": "Who was the first Emperor of Rome?",
        "options": ["Julius Caesar", "Augustus", "Nero", "Caligula"],
        "answer": "Augustus"
    },
    {
        "question": "Who was the British Prime Minister during World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Anthony Eden"],
        "answer": "Winston Churchill"
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1915", "1920", "1905"],
        "answer": "1912"
    },
    {
        "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
        "options": ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Jacqueline Cochran"],
        "answer": "Amelia Earhart"
    },
    {
        "question": "What was the main cause of the American Civil War?",
        "options": ["Slavery", "States' rights", "Taxation", "Territorial expansion"],
        "answer": "Slavery"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Joseph Lister"],
        "answer": "Alexander Fleming"
    },
    {
        "question": "Which ancient civilization built the pyramids?",
        "options": ["Maya", "Greek", "Egyptian", "Roman"],
        "answer": "Egyptian"
    },
    {
        "question": "What event triggered World War I?",
        "options": ["Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Attack on Pearl Harbor", "Signing of the Treaty of Versailles"],
        "answer": "Assassination of Archduke Franz Ferdinand"
    },
    {
        "question": "What was the primary language spoken in Ancient Rome?",
        "options": ["Greek", "Latin", "Italian", "Spanish"],
        "answer": "Latin"
    },
    {
        "question": "Who led the Indian independence movement against British rule?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "B. R. Ambedkar"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "What is the name of the ship that carried the Pilgrims to America in 1620?",
        "options": ["Mayflower", "Nina", "Pinta", "Santa Maria"],
        "answer": "Mayflower"
    }
]

class QuizApp:
    def __init__(self, master):
        self.master = master  # Initialize the main window
        self.master.title("History Quiz")  # Set the title of the window
        self.master.geometry("700x300")  # Set the window size
        self.current_question = 0  # Track the current question index
        self.score = 0  # Initialize the score

        # Load and resize the background image
        self.background_image = Image.open("E:/DIP/y13/91907/version - 4/image/history.png")  # Replace with your background image path
        self.background_image = self.background_image.resize((700, 300), Image.LANCZOS)  # Resize image for the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)  # Convert to a format usable by Tkinter

        # Create a label for the background image
        background_label = tk.Label(master, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)  # Place the background label to fill the window

        # Create a label for the question text
        self.question_label = tk.Label(master, text="", font=("Arial", 14), bg="white")  # You can choose a suitable color for the background
        self.question_label.pack(pady=20)  # Add some padding

        # Create a frame for the answer buttons
        self.button_frame = tk.Frame(master, bg="white")  # Create a frame as a container for the buttons
        self.button_frame.pack(pady=20)  # Add some padding

        self.answer_buttons = []  # List to hold the answer buttons
        for option in range(4):
            # Create buttons for answer options
            btn = tk.Button(self.button_frame, text="", font=("Arial", 12),
                            command=lambda option=option: self.check_answer(self.answer_buttons[option].cget("text")))
            btn.grid(row=0, column=option, padx=10)  # Arrange buttons horizontally
            self.answer_buttons.append(btn)  # Add the button to the list

        # Create a label for displaying the result
        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="white")  # Result label
        self.result_label.pack(pady=20)  # Add some padding

        self.show_question()  # Show the first question

    def show_question(self):
        if self.current_question < len(questions):
            # Get the current question
            question = questions[self.current_question]
            self.question_label.config(text=question["question"])  # Update the question label
            for i, option in enumerate(question["options"]):
                self.answer_buttons[i].config(text=option, state=tk.NORMAL)  # Set button text and enable them
            self.result_label.config(text="")  # Clear the result label
        else:
            self.show_final_score()  # Show final score if all questions are answered

    def check_answer(self, selected_option):
        correct_answer = questions[self.current_question]["answer"]  # Get the correct answer
        if selected_option == correct_answer:
            self.score += 1  # Increase score if the answer is correct
            self.result_label.config(text="Correct!", fg="green")  # Update result label to show correct answer
        else:
            self.result_label.config(text=f"Wrong! The correct answer is: {correct_answer}", fg="red")  # Show the correct answer

        self.current_question += 1  # Move to the next question
        for btn in self.answer_buttons:
            btn.config(state=tk.DISABLED)  # Disable buttons after an answer is selected
        self.master.after(2000, self.show_question)  # Show the next question after 2 seconds

    def record_score(self, score, percentage):
        with open("players.txt", "a") as f:
            # Record score and percentage in a text file
            f.write(f"\n-------\nSubject: History\nScore: {score}\nPercentage: {percentage:.2f}%\n-------\n")

    def show_final_score(self):
        percentage = (self.score / len(questions)) * 100  # Calculate the score percentage
        self.record_score(self.score, percentage)  # Record the score

        self.question_label.config(text="Quiz complete!")  # Update the question label to show completion message
        for btn in self.answer_buttons:
            btn.pack_forget()  # Remove buttons from the window
        self.result_label.config(text=f"Your final score is: {self.score}/{len(questions)}")  # Show the final score

        self.master.after(5000, self.master.destroy)  # Close the window after 5 seconds

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = QuizApp(root)  # Initialize the quiz application
    root.mainloop()  # Start the Tkinter event loop
