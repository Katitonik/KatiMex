import tkinter as Tk
from tkinter import ttk

app = Tk.Tk()
app.title("El Fuego Cochoracha")
app.geometry("690x690")

labelTop = Tk.Label(app, text = "El Fuego Cocoracha")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, values=["Nachos", "Mole", "Enchiladas"])

print(dict(comboExample))
comboExample.grid(column=0, row=1)
comboExample.current(1)
print(comboExample.current(), comboExample.get())

def show():
    myLabel = Label(app, text=clicked.get).pack()

clicked=StringVar()
clicked.set("Mole")

app.mainloop()