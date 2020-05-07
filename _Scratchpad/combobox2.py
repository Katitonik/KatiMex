import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('El Fuego Cocoracha')
window.geometry('600x400')

ttk.Label(window,
        text = "El Fuego Cocoracha phone orders").grid(column = 0, row  = 1)

ttk.Label(window, text = "Order : ").grid(column = 0, row = 5)

n =tk.StringVar()
menuitem = ttk.Combobox(window, width = 27, textvariable = n)

menuitem['values'] = ('Nachos',
                    'Hard shell Tacos',
                    'Soft shell tacos',
                    'Chimichangas',
                    'Chiles Rellenos',
                    'Chilato de Pollo',
                    'Sopa de Cameron',
                    'Cochnita pibli',
                    'Mole',
                    'Aguachile',
                    'Enchiladas')

menuitem.grid(column = 1, row = 5)
menuitem.current()
window.mainloop()


