from random import choice
from tkinter import *

root = Tk()
root.minsize(height = 50, width = 200)
root.title('Password')

chars = ('abcdefghijklmnoprstuvqxyz')
num = ('0123456789')
up = chars.upper()
special = '____?!%.____'

all = num+chars+up+special

password = ''.join(choice(all)for i in range(8))

label = Label(text = 'Your password is '+password, font = 'comic',fg = 'red')


label.pack()
root.mainloop()
