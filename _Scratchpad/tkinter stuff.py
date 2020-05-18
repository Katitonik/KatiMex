import tkinter as Tk
from tkinter import ttk

app = Tk.Tk()
app.geometry("400x400")

labelTop = Tk.Label(app, text="El Fuego Cocoracha")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, values=["Nachos", "Mole", "Enchiladas"])

print(dict(comboExample))
comboExample.grid(column=0, row=1)
comboExample.current(1)
print(comboExample.current(), comboExample.get())

app.mainloop()
