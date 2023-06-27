from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)
# my_label.place(x=100, y=200)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.config(padx=10, pady=10)
# button.pack()

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# new_button.config(padx=10, pady=10)

# Entry
input = Entry(width=10)
# input.config(padx=10, pady=10)
input.grid(column=3, row=2)
# input.pack()


window.mainloop()
