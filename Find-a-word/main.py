import random
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.ttk import Combobox
window = tk.Tk()
window.title('Tkinter Yes/No Dialog')
window.geometry("770x550")
window.config(bg="#2F4F4F")
window.title("Guess The Word")
window.resizable(width=False, height=False)
label = tk.Label(text='Enter Name',font=("Arial", 10), fg="White",bg="#2F4F4F")
label.place(x=150, y=100)
name = tk.Entry()
name.place(x=230, y=100)
var1 = tk.StringVar()
combo = Combobox(textvariable=var1)
combo['values'] = ('Beginner','Moderate','Expert')
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=230, y=130)
Guess = tk.Entry(window, font=("Arial", 11))
Textarea = tk.Text(height=2,width=80,font=("Arial", 12), )
# Here the user is asked to enter the name first
print("Good Luck ! ", name)
guesses = ""

def reverse_string(str):
    str1 = ""   # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1
    return str1    # It will return the reverse string to the caller function

def Find():
    global guesses
    global word
    # any number of turns can be used here
    global turns
    Textarea.delete('1.0', 'end')
    while turns > 0:
        # every input character will be stored in guesses
        guess = Guess.get()
        guesses += guess
        # counts the number of times a user fails
        failed = 0
        # all characters from the input
        # word taking one at a time.
        for char in reverse_string(word):
            # comparing that character with
            # the character in guesses
            if char in guesses:
                Textarea.insert(1.0, char+'\t')
            else:
                Textarea.insert(1.0, '-\t')
                # for every failure 1 will be
                # incremented in failure
                failed += 1
        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            messagebox.showinfo("Information", "Congrats You Win")
            # this print the correct word
            break
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        Guess.delete(0, 'end')
        if guess not in word:
            turns -= 1
            messagebox.showinfo("Information", "Wrong\n" 'You have ' + str(turns) + ' more guesses')
            if turns == 0:
                messagebox.showinfo("Information", "You Loose")
                messagebox.showinfo("Information", "The word is: "+ word)
        break
def PName():
    if name.get() != '':
        print(name.get())
        label1 = tk.Label(text='Welcome :   ' + name.get(),font=("Arial", 10), fg="White",bg="#2F4F4F")
        label1.place(x=200, y=200)
        label2 = tk.Label(text='Guess The Charatcter :',font=("Arial", 13), fg="White",bg="#2F4F4F")
        label2.place(x=230, y=230)
        Guess.place(x=230,y=260)
        Button = tk.Button(text="Check", command=Find)
        Button.place(x=400,y=260)
        giveup_btn = tk.Button(window, text="Give up", font=("Arial", 14), fg="BLACK", bg="#DCDCDC", command=lambda:[label1.destroy(), label2.destroy(), Guess.destroy(), Button.destroy(), giveup_btn.destroy(), exit_button.destroy(), Textarea.destroy()])
        giveup_btn.place(x=230, y=350)
        exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="BLACK", bg="#DCDCDC", command=exit)
        exit_button.place(x=320, y=350)
        Textarea.place(x=20, y=290)
        global turns
        global word
        global words
        if var1.get() == 'Beginner':
            words = ['eager','earth','ghost','cache','index','genre','inbox','large','laser','blend','brick'
    ]
            # Function will choose one random
            # word from this list of words
            word = random.choice(words)
            turns = 6
        elif var1.get() == 'Moderate':
            words = ['aspect','backed','casual','debate','estate','facing','ground','honest','luxury','market',
                     'Account','ability','academy','achieve','address','element','convert','control','gallery','general'
                     'absolute','swimming','syndrome']
            # Function will choose one random
            # word from this list of words
            word = random.choice(words)
            turns = 8
        elif var1.get() == 'Expert':
            words = ['chocolate','fireboard','beautiful','chocolate','happinessimportant','dangerous','elizabeth','macaronic','president','irregular']
            # Function will choose one random
            # word from this list of words
            word = random.choice(words)
            turns = 10

Button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="BLACK", bg="#DCDCDC", command=PName)
# Heading of our game
title = tk.Label(window, text="Find A Word", font=("Arial", 24), fg="White", bg="#2F4F4F")
Button.place(x=230, y=160)
# Place the labels
title.place(x=200, y=50)
window.mainloop()