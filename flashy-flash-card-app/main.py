from tkinter import *
import pandas, random, time

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"

card = {}
lang_list = []
words_to_learn_list = []


# ********** Get data from file **********

try:
    data = pandas.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


# *********** Handle right and wrong **********
def right_answer():
    data_dict.remove(card)
    print(len(data_dict))
    next_card()

def wrong_answer():
    words_to_learn_list.append(card)
    words_to_learn_df = pandas.DataFrame(words_to_learn_list)
    words_to_learn_df.to_csv(WORDS_TO_LEARN_FILE, index=False)
    next_card()

# ********** Generate flashcard **********
def next_card():
    global card, lang_list, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(data_dict)
    print(card)
    lang_list = list(card.keys())
    from_lang = lang_list[0]
    canvas.itemconfig(title, text=from_lang, fill="black")
    canvas.itemconfig(word, text=card[from_lang], fill="black")
    canvas.itemconfig(card_background, image=card_front_bg)
    flip_timer = window.after(ms=3000, func=flip_card)



def flip_card():
    global card, lang_list
    to_lang = lang_list[1]
    answer = card[to_lang]
    canvas.itemconfig(card_background, image=card_back_bg)
    canvas.itemconfig(title, text=to_lang, fill="white")
    canvas.itemconfig(word, text=answer, fill="white")


# ********** UI Setup **********

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(ms=3000, func=flip_card)

# Canvas with Words
card_front_bg = PhotoImage(file="images/card_front.png")
card_back_bg = PhotoImage(file="images/card_back.png")
canvas = Canvas()
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front_bg)

title = canvas.create_text(400, 150, text="Title", fill="black", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="word", fill="black", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
wrong_button_bg = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_bg, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                      command=wrong_answer)
wrong_button.grid(row=1, column=0)
correct_button_bg = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_bg, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                        borderwidth=0, command=right_answer)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()
