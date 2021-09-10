from tkinter import *
from random import randrange

root = Tk()
root.minsize(height = 200, width = 400)
root.title('Guesser')
entry = Entry(root, borderwidth = 3, width= 40, font = 'comic')
entry.pack()
label = Label(root, font = 'comic')

a = randrange(1000)
def guess():
    if (int(entry.get()) == a):
        label.config(text = 'You Win! Winning number is '+ str(a) +'.',fg = 'green')
        label.pack()
    if (int(entry.get()) > a):
        label.config(text='Smaller',fg = 'red')
        label.pack()
        entry.delete(0, END)
    if(a > int(entry.get())):
        label.config(text='Bigger',fg = 'red')
        label.pack()
        entry.delete(0, END)
button = Button(root, text='Guess', command = guess,font = 'comic' )
button.pack()

title = Label(root,font = 'comic')
title.config(text = 'I think number from 1 to 1000. Find it out!')
title.pack()

root.mainloop()