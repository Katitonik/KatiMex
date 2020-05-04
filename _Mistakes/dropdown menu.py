from tkinter import *

root = Tk()
root.title('El Fuego Cocoracha orders')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get).pack()

clicked = StringVar()
clicked.set("Mole")

drop = OptionMenu(root, clicked, "Mole", "Nachos")
drop.pack

myButton = Button(root, text="Show menu items", command=show).pack()

root.mainloop()