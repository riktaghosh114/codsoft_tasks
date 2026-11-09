import tkinter as tk
import random

# Scores
user_score = 0
comp_score = 0

# Computer choice
def gen_comp_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)


# Update message
def draw_game():
    msg.config(
        text="Game Draw! Play Again",
        bg="#ade8f4",
        fg="#111827"
    )


# Show winner
def show_winner(user_win, user_choice, comp_choice):
    global user_score, comp_score

    if user_win:
        user_score += 1
        user_score_label.config(text=str(user_score))

        msg.config(
            text=f"You Win! {user_choice} beats {comp_choice}",
            bg="#95D5B2",
            fg="#111827"
        )

    else:
        comp_score += 1
        comp_score_label.config(text=str(comp_score))

        msg.config(
            text=f"You Lose! {comp_choice} beats {user_choice}",
            bg="#ffc2d1",
            fg="#111827"
        )


# Main game logic
def play_game(user_choice):

    comp_choice = gen_comp_choice()

    if user_choice == comp_choice:
        draw_game()
        return

    user_win = False

    if user_choice == "Rock":
        user_win = comp_choice == "Scissors"

    elif user_choice == "Paper":
        user_win = comp_choice == "Rock"

    elif user_choice == "Scissors":
        user_win = comp_choice == "Paper"

    show_winner(user_win, user_choice, comp_choice)


# Reset game
def reset_game():
    global user_score, comp_score

    user_score = 0
    comp_score = 0

    user_score_label.config(text="0")
    comp_score_label.config(text="0")

    msg.config(
        text="Play Your Move",
        bg="#1e293b",
        fg="white"
    )


# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x650")
root.configure(bg="#0f172a")
root.resizable(False, False)


# Title
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 28, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=35)


# Choice section
choice_frame = tk.Frame(root, bg="#0f172a")
choice_frame.pack(pady=35)


# Choice buttons
button_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#1e293b",
    "fg": "white",
    "activebackground": "#2563eb",
    "activeforeground": "white",
    "width": 13,
    "height": 3,
    "bd": 0,
    "cursor": "hand2"
}

rock_btn = tk.Button(
    choice_frame,
    text="✊ ROCK",
    command=lambda: play_game("Rock"),
    **button_style
)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(
    choice_frame,
    text="✋ PAPER",
    command=lambda: play_game("Paper"),
    **button_style
)
paper_btn.grid(row=0, column=1, padx=15)

scissor_btn = tk.Button(
    choice_frame,
    text="✌ SCISSORS",
    command=lambda: play_game("Scissors"),
    **button_style
)
scissor_btn.grid(row=0, column=2, padx=15)


# Scoreboard
score_frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=50,
    pady=25
)
score_frame.pack(pady=30)

user_score_label = tk.Label(
    score_frame,
    text="0",
    font=("Arial", 45, "bold"),
    bg="#1e293b",
    fg="white"
)
user_score_label.grid(row=0, column=0, padx=40)

comp_score_label = tk.Label(
    score_frame,
    text="0",
    font=("Arial", 45, "bold"),
    bg="#1e293b",
    fg="white"
)
comp_score_label.grid(row=0, column=1, padx=40)


# Score labels
tk.Label(
    score_frame,
    text="YOU",
    font=("Arial", 14),
    bg="#1e293b",
    fg="#94a3b8"
).grid(row=1, column=0)

tk.Label(
    score_frame,
    text="COMPUTER",
    font=("Arial", 14),
    bg="#1e293b",
    fg="#94a3b8"
).grid(row=1, column=1)


# Result message
msg = tk.Label(
    root,
    text="Play Your Move",
    font=("Arial", 17, "bold"),
    bg="#1e293b",
    fg="white",
    padx=25,
    pady=15
)
msg.pack(pady=15)


# Reset button
reset_btn = tk.Button(
    root,
    text="RESET GAME",
    font=("Arial", 14, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#4f46e5",
    activeforeground="white",
    bd=0,
    padx=30,
    pady=12,
    cursor="hand2",
    command=reset_game
)
reset_btn.pack(pady=20)


# Run application
root.mainloop()