#import tkinter and ttk widgets to work with 
from tkinter import Tk
from tkinter import ttk

#define root as Tk() 
#and set the perameters (the length and width)
root = Tk()
root.geometry("1000x690")

label = ttk.Label(root, text="El Fuego Chucoracha")

def show():
    Label = ttk.Label(root, text=clicked.get()).pack()

clicked = Tk.StringVar()
clicked.set("Menu")

#option menu is a widget in the ttk import
drop = ttk.OptionMenu(root, clicked, "Nachos", "Mole", "Enchiladas")
drop.pack()

myButton = ttk.Button(root, text="Selected_orders", command=show).pack()
root.mainloop()