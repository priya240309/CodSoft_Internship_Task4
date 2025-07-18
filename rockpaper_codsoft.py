import tkinter as tk
import random

options = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(options)

def find_winner(user_pick, computer_pick):
    if user_pick == computer_pick:
        return "Tie"
    elif(user_pick == "Rock" and computer_pick == "Scissors") or \
        (user_pick == "Paper" and computer_pick == "Rock") or \
        (user_pick == "Scissors" and computer_pick == "Paper"):
            return "user"
    else:
        return "Computer"
def play_game(user_pick):
    global user_score, computer_score
    
    computer_pick = get_computer_choice()
    winner = find_winner(user_pick, computer_pick)
    
    if winner == "User":
        result_msg = "You Win!"
        user_score += 1
    elif winner == "Computer":
        result_msg = "You Lose!"
        computer_score +=1
    else:
        result_msg = "It's a Tie!"
    result_text.set(f"Your Choice: {user_pick}\nComputer's Choice: {computer_pick}\nResult: {result_msg}")
    score_text.set(f"Your Score: {user_score} | Computer Score: {computer_score}")
#setup gui
win = tk.Tk()
win.title("Rock Paper Scissors Game")
win.geometry("400x350")
win.configure(bg="#f0f0f0")

title = tk.Label(win, text="Rock Paper Scissors", font=("Arial",18,"bold"), bg="#f0f0f0")
title.pack(pady=10)

instruction = tk.Label(win, text="Choose one:", font=("Arial",12), bg="#f0f0f0")
instruction.pack()

btn_frame = tk.Frame(win, bg= "#f0f0f0")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command= lambda: play_game("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command= lambda: play_game("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command= lambda: play_game("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

result_text = tk.StringVar()
result_label = tk.Label(win, textvariable=result_text, font=("Arial",12), bg= "#f0f0f0")
result_label.pack(pady=10)

score_text = tk.StringVar()
score_label = tk.Label(win, textvariable=score_text, font=("Arial", 12, "bold"),bg = "#f0f0f0")
score_label.pack(pady=10)

exit_btn = tk.Button(win,text= "Exit", width= 10, command= win.destroy)
exit_btn.pack(pady=5)

win.mainloop()

