from tkinter import *
root = Tk()
root.minsize(height = 400, width = 800)
root.title('calculator')
entry = Entry(root)
entry.pack()
label = Label(root)
def cal():
    label.config(text=''+ str(eval(entry.get())))
    label.pack()
button = Button(root, text='calculate', command = cal )
button.pack()
root.mainloop()