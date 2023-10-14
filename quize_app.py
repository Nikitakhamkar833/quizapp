import tkinter as tk
from tkinter import messagebox

# Define a list of questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["7", "8", "10", "6"],
        "answer": "8"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Mars"
    }
]

# Track the current question index
current_question = 0

# Function to check the answer
def check_answer():
    global current_question
    user_answer = var.get()
    if user_answer == questions[current_question]["answer"]:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror("Result", f"Wrong answer. Correct answer is: {questions[current_question]['answer']}")
    
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Complete", "Quiz completed!")
        root.destroy()

# Function to display the question and options
def display_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        option_buttons[i].config(text=questions[current_question]["options"][i])

# Create the main application window
root = tk.Tk()
root.title("Quiz App")

# Create and configure the label for displaying the question
question_label = tk.Label(root, text="")
question_label.pack(pady=10)

# Create a list to hold the radio buttons for options
option_buttons = []

# Create and place the radio buttons for options
var = tk.StringVar()
for i in range(4):
    option_button = tk.Radiobutton(root, text="", variable=var, value=questions[current_question]["options"][i])
    option_button.pack(pady=5)
    option_buttons.append(option_button)

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Display the first question
display_question()

# Run the main event loop
root.mainloop()