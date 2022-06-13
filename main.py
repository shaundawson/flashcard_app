from tkinter import *
from numpy import pad

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas= Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"), fill="black")
canvas.create_text(400, 263, text="word", font=(FONT_NAME, 40, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

window.mainloop()