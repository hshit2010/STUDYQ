import tkinter as tk
from API import get_amount

# --- Game State Variables ---
quiz = []
current_q_index = 0
score = 1
player_name = ""

# --- Game Logic Functions ---
def start_game():
    global quiz, player_name
    
    # 1. Grab the name and fetch data
    player_name = name_entry.get()
    main_label.config(text="Loading questions from the internet...")
    root.update() 
    quiz = get_amount(5)
    
    # 2. Hide the name entry and show the answer entry
    name_entry.pack_forget()
    start_btn.pack_forget()
    answer_entry.pack(pady=5)
    submit_btn.pack(pady=5)
    
    # 3. Load the first question
    show_question()

def show_question():
    global current_q_index
    
    if current_q_index < len(quiz):
        q = quiz[current_q_index]
        
        # Build the question and options into one block of text
        display_text = q["question"] + "\n\n"
        for opt in q["options"]:
            display_text += f"- {opt}\n"
            
        main_label.config(text=display_text)
        feedback_label.config(text=f"Score: {score} | Type exact answer or 'skip'")
        answer_entry.delete(0, tk.END)
    else:
        # Game Over state
        main_label.config(text=f"Game Over!\n\nHI {player_name}\nYour total is {score}")
        answer_entry.pack_forget()
        submit_btn.pack_forget()
        feedback_label.config(text="")

def submit_answer():
    global current_q_index, score
    
    q = quiz[current_q_index]
    answer = answer_entry.get().lower().strip()
    correct_answer = q["answer"].lower()
    
    # --- Your Exact Game Logic ---
    if answer == "skip":
        if score <= 1:
            feedback_label.config(text="Score too low cant let this happen!")
            return # Stops the function early so the question doesn't change
        else:
            score -= 2
    elif answer == correct_answer:
        score += 4
    else:
        score -= 1
        
    # Move to the next question
    current_q_index += 1
    show_question()

# --- The Simplest UI Setup ---
root = tk.Tk()
root.title("StudyQ")
root.geometry("500x400")
root.configure(bg="white") # Set background to white

# Main display area for questions (white background, black text)
main_label = tk.Label(root, text="please enter your sweet name:", bg="white", fg="black", font=("Arial", 12), wraplength=450)
main_label.pack(pady=20)

# The name input box
name_entry = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
name_entry.pack(pady=5)

# The start button
start_btn = tk.Button(root, text="Start", command=start_game, bg="white", fg="black")
start_btn.pack(pady=5)

# The answer input box (Created now, but hidden until the game starts)
answer_entry = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
submit_btn = tk.Button(root, text="Submit Answer", command=submit_answer, bg="white", fg="black")

# Feedback label at the bottom for errors or score
feedback_label = tk.Label(root, text="", bg="white", fg="black", font=("Arial", 10))
feedback_label.pack(pady=20)

root.mainloop()