from tkinter import *

FONT = ('Arial', 16, 'normal')
PADDING = 30

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609344
    converted_value["text"] = km


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=50)
window.config(padx=PADDING, pady=PADDING)

miles_input = Entry()
miles_input.config(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_text = Label(text="is equal to", font=FONT)
is_equal_text.grid(column=0, row=1)

converted_value = Label(text="0", font=FONT)
converted_value.grid(column=1, row=1)

miles_label = Label(text="Km", font=FONT)
miles_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()