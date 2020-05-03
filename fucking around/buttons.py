from tkinter import Tk
from tkinter import ttk

root = Tk()

#Jsut had to add ttk. to the front of the Label widget
myLabel = ttk.Label(root, text="Idk man")
myLabel2 = ttk.Label(root, text="I finna kms")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()