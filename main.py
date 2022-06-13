from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
timer = None



# ---------------------------- FLIP THE CARDS------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

    global reps
    reps = 0




# ---------------------------- CARD FLIPPING MECHANISM ------------------------------- # 
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas= Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 40, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command= next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()