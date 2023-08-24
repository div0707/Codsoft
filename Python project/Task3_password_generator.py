from tkinter import *
import random, string

def selection():
    global password_strength
    password_strength = choice.get()

def callback():
    password = passgen()
    lsum.config(text=password)

def passgen():
    if password_strength == 1:
        characters = poor
    elif password_strength == 2:
        characters = average
    elif password_strength == 3:
        characters = advance
    else:
        characters = ""
    
    generated_password = "".join(random.sample(characters, val.get()))
    return generated_password

root = Tk()
root.geometry("400x380")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Select the strength of the password:")

choice = IntVar()
password_strength = 1  # Default password strength
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection).pack(anchor=CENTER)

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlength = Spinbox(root, from_=4, to_=24, textvariable=val, width=13).pack()

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, bg='lightblue')
passgenButton.pack()

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

root.mainloop()
