BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'ariel'
from tkinter import *
import pandas as pd
from random import choice

word_choice = {}

def new_word():
    global flip_timer, word_choice
    window.after_cancel(flip_timer)
    word_choice = choice(french_words_dict)
    canvas.itemconfig(canvas_image, image=cardfront_img)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=word_choice['French'])
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=cardback_img)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=word_choice['English'])


def is_know():
    global french_words_dict
    french_words_dict.remove(word_choice)
    data = pd.DataFrame(french_words_dict)
    data.to_csv("data/to_learn.csv", index=False)
    new_word()
    print(len(french_words_dict))
try:
    french_words = pd.read_csv('data/to_learn.csv')
    french_words_dict = french_words.to_dict(orient="records")
except:
    french_words = pd.read_csv('data/french_words.csv')
    french_words_dict = french_words.to_dict(orient="records")

french_words_dict = french_words.to_dict(orient="records")
print(french_words_dict)
# TK class
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func= flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardback_img = PhotoImage(file="images/card_back.png")
cardfront_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=cardfront_img)
canvas.grid(column=0, row=0, columnspan=2,sticky="EW")

language = canvas.create_text(400,150, text='title', fill="black", font=(FONT_NAME, 40 ,"italic"))
word = canvas.create_text(400,263, text='word', fill="black", font=(FONT_NAME, 60 ,"bold"))


# Button
my_left_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=my_left_image, highlightthickness=0,bg=BACKGROUND_COLOR , command =new_word)
left_button.grid(column=0, row=1)
my_right_image = PhotoImage(file="images/right.png")
right_button = Button(image=my_right_image, highlightthickness=0,bg=BACKGROUND_COLOR,
                      command = is_know)
right_button.grid(column=1, row=1)

# New word

new_word()

window.mainloop()