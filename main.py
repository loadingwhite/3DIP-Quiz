import tkinter as tk
from tkinter import ttk
import geography_quiz  # Import the geography quiz module
import history_quiz    # Import the history quiz module

# Function to open the geography quiz in a new window
def open_geography_quiz():
    new_window = tk.Toplevel(root)  # Create a new window using Toplevel
    geography_quiz.QuizApp(new_window)  # Instantiate the geography quiz app

# Function to open the history quiz in a new window
def open_history_quiz():
    new_window = tk.Toplevel(root)  # Create a new window using Toplevel
    history_quiz.QuizApp(new_window)  # Instantiate the history quiz app

# Function to handle quiz selection based on user choice
def on_quiz_selected(choice):
    if choice == "Geography":
        open_geography_quiz()  # Open geography quiz if selected
    elif choice == "History":
        open_history_quiz()  # Open history quiz if selected

# Function to get player information (name and age)
def get_player_info():
    name = name_entry.get()  # Get name from input
    age = age_entry.get()    # Get age from input

    # Validate name input
    if not name:
        result_label.config(text="Please enter your name.", fg="red")  # Show error message
        return
    
    # Validate age input
    if not age.isdigit():
        result_label.config(text="Please enter a valid age (numbers only).", fg="red")  # Show error message
        return

    age = int(age)  # Convert age to integer

    # Check age eligibility
    if 12 <= age <= 20:
        result_label.config(text=f"Welcome, {name}!", fg="green")  # Welcome message
        hide_login_inputs()  # Hide input fields
        show_quiz_options()  # Show quiz options
    elif age > 20:
        result_label.config(text="Sorry, you're too old to play this game.", fg="blue")  # Age too high
    else:
        result_label.config(text="Sorry, you must be at least 12 years old to play.", fg="blue")  # Age too low
    
    # Record player's information
    record_player_info(name, age)

# Write player's information into a text file
def record_player_info(name, age):
    try:
        with open("players.txt", "a") as f:
            f.write(f"---------------\nName: {name}\nAge: {age}\n")
    except Exception as e:
        result_label.config(text="Error saving player information.", fg="red")

# Function to hide login input fields
def hide_login_inputs():
    name_label.pack_forget()  # Hide name label
    name_entry.pack_forget()  # Hide name entry
    age_label.pack_forget()   # Hide age label
    age_entry.pack_forget()   # Hide age entry
    submit_button.pack_forget()  # Hide submit button

# Function to show quiz options for the user
def show_quiz_options():
    quiz_label = tk.Label(root, text="Choose a quiz type:", font=("Arial", 14), bg="lightblue")
    quiz_label.pack(pady=20)  # Show quiz selection label

    # Button to select geography quiz
    geography_button = tk.Button(root, text="Geography", command=lambda: on_quiz_selected("Geography"), bg="lightgreen")
    geography_button.pack(pady=10)  # Show geography button

    # Button to select history quiz
    history_button = tk.Button(root, text="History", command=lambda: on_quiz_selected("History"), bg="lightgreen")
    history_button.pack(pady=10)  # Show history button

    # Ensure exit button is always at the bottom
    exit_button.pack(side=tk.BOTTOM, pady=20)  # Show exit button at the bottom

# Function to exit the game
def exit_game():
    with open("players.txt", "a") as f:
        f.write("---------------\n")  # Record separator line
    root.quit()  # Close the main window

# Set up the main application window
root = tk.Tk()
root.title("Quiz")  # Window title
root.geometry("400x400")  # Set window size
root.config(bg="lightblue")  # Set background color of the main window

# Input for player name
name_label = tk.Label(root, text='Please enter your name:', bg="lightblue")
name_label.pack(pady=10)  # Show name label
name_entry = tk.Entry(root)
name_entry.pack(pady=10)  # Show name entry

# Input for player age
age_label = tk.Label(root, text='Please enter your age:', bg="lightblue")
age_label.pack(pady=10)  # Show age label
age_entry = tk.Entry(root)
age_entry.pack(pady=10)  # Show age entry

# Button to submit player info
submit_button = ttk.Button(root, text="Enter", command=get_player_info)
submit_button.pack(pady=20)  # Show submit button

# Label to display results
result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)  # Show result label

# Add exit button at the bottom
exit_button = ttk.Button(root, text="Exit", command=exit_game)
exit_button.pack(side=tk.BOTTOM, pady=20)  # Show exit button at the bottom

# Start the main loop
root.mainloop()  # Run the application
