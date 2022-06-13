from tkinter import *

from numpy import pad

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0,)
logo_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.grid(row=1, rowspan=2, column=0, columnspan=2)


#Labels
title_label = Label(text="Title",font=(FONT_NAME, 60, "italic"), bg= "white", fg= "black")
title_label.grid(row=1, column=0, columnspan=2, sticky='S', pady=10)
word_label = Label(text="Word", font=(FONT_NAME, 40, "bold" ),  bg= "white", fg= "black")
word_label.grid(row=2,column=0, columnspan=2, sticky='N')


#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=3, column=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=3, column=0)

window.mainloop()