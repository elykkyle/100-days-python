from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += ([choice(letters) for x in range(nr_letters)])
    password_list += ([choice(symbols) for x in range(nr_symbols)])
    password_list += ([choice(numbers) for x in range(nr_numbers)])

    shuffle(password_list)

    password = "".join(password_list)

    return password

def fill_copy_password():
    new_password = generate_password()
    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Saves information to file and clears website & password entries"""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()


    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't leave any empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}")

        if is_ok:
            with open('passwords.txt', "a") as password_file:
                password_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "username@example.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=fill_copy_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
