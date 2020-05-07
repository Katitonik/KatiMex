from collections import namedtuple
from tkinter import Tk
from tkinter import ttk

#The dish is the 'main'namedtuple of the program
Dish = namedtuple('Dish', ['name', 'spicyness', 'size'])

from enum import IntEnum
class spicyness(IntEnum):
    Mild = 0
    Hot = 1
    Very_Hot = 2
    Why = 3
class size(IntEnum):
    S = 0
    M = 1
    L = 2
    How = 3

Nachos = Dish("Nachos", spicyness.Mild, size.S)
Hard_Shell_Tacos = Dish("Hard_shell_tacos", spicyness.Hot, size.M)
Soft_Shell_Tacos = Dish("Soft_shell_tacos", spicyness.Why, size.How)
Chiles_Rellenos = Dish("Chiles_Rellenos", spicyness.Why, size.S)
Chimichangas = Dish("Chimichangas", spicyness.Hot, size.M)
Chilato_de_Pollo  = Dish("Chilato_de_Pollo", spicyness.Mild, size.S)
Sopa_de_Cameron = Dish("Sopa_de_Cameron", spicyness.Very_Hot, size.L)
Cochnita_pibli = Dish("Cochnita_pibli", spicyness.Hot, size.M)
Mole = Dish("Mole", spicyness.Hot, size.How)
Aguachile = Dish("Aguachile", spicyness.Why, size.How)
Enchiladas = Dish("Enchiladas", spicyness.Mild, size.L)

menu = ["Nachos", 
"Hard_Shell_Tacos", 
"Soft_Shell_Tacos", 
"Chiles_Rellenos", 
"Chimichangas",
"Chilato_de_Pollo",
"Sopa_de_Cameron",
"Cochnita_pibli", 
"Mole",
"Aguachile", 
"Enchiladas"
]

#I want the menu displayed from A - Z thus i use .sort
menu.sort()

app = Tk()
app.geometry("690x690")

labelTop = ttk.Label(app, text = "El Fuego Cucoracha")
labelTop.grid(column=0, row=0)

drop_down_menu = ttk.Combobox(app, values=["Nachos", 
"Hard Shell Tacos", 
"Soft Shell Tacos", 
"Chiles Rellenos", 
"Chimichangas",
"Chilato de Pollo",
"Sopa de Cameron",
"Cochnita pibli", 
"Mole",
"Aguachile", 
"Enchiladas"])

print(dict(drop_down_menu))
drop_down_menu.grid(column=0, row=1)
drop_down_menu.current(1)
print(drop_down_menu.current(), drop_down_menu.get())


#The sides that can be added to the dish
Side = namedtuple("Side", ["option", "Amount"])

from enum import IntEnum
class Amount(IntEnum):
    S = 0
    M = 1
    L = 2

Guakamole = Side("Guakamole", Amount.L)
Chips = Side("Chips", Amount.S)
Salad = Side("Salad", Amount.M)
Salsa = Side("Salsa", Amount.S)

extra = [Chips, Salad, Salsa]

print(extra)

drop_down_extra = ttk.Combobox(app, values=["Chips","Salad", "Salsa"])
print(dict(drop_down_extra))
drop_down_extra.grid(column=4, row=1)
drop_down_extra.current(0)
print(drop_down_extra.current(), drop_down_extra.get())

#The information of the employee
Employee = namedtuple("Employee", ("ID", "name", "Role", "psswdhash"))
#psswdhash (password) = hash which returns the hash value of the given option, this gives a good 'randomized' 
# password
Alex = Employee("101", "Alex", "Cashier", psswdhash=hash("I cant remember!"))
Sam = Employee("102", "Sam", "Delivery driver", psswdhash=hash("do you know?"))
Jo = Employee("103", "Jo", "Clerk", psswdhash=hash("i dont know!"))

employees = [Alex, Sam, Jo]

print(employees)

from enum import IntEnum

class suburb(IntEnum):
    Long_Bay = 0
    Browns_bay = 1
    Torbay = 2
    Albany = 3
    Silverdale = 4

drop_down_suburb = ttk.Combobox(app, values=["Long Bay", "Browns Bay", "Torbay", "Albany", "Silverdale"])
print(dict(drop_down_suburb))
drop_down_suburb.grid(column=6, row=1)
drop_down_suburb.current(1)
print(drop_down_suburb.current(), drop_down_suburb.get())
customer = namedtuple('Customer', ('name', 'phonenumber', 'address', 'suburb'))

Emile_Matthews = customer('Emile_Matthews', '0789121980', '4c_Pongola_Rd', suburb.Torbay)
Marissa_Moore = customer('Marissa_Moore', '0783456236', '2b_Capecod_Rd', suburb.Long_Bay)
Sandra_Koen = customer('Sandra_Koen', '0201457836', '30_Tui_Rd', suburb.Browns_bay)
Koos_Koombuis = customer('Koos_Kombuis', '0208963773', '777_Kiwi_Ln', suburb.Albany)
Jan_Blauukaas = customer('Jan_Blauukaas', '0220982454', '776_Kiwi_Ln', suburb.Albany)
Pieter_Pan = customer('Pieter_Pan', '02215568903', '9_Pamela_Cres', suburb.Silverdale)

Custmers = [Emile_Matthews, Marissa_Moore, Sandra_Koen, Koos_Koombuis, Jan_Blauukaas, Pieter_Pan]

print(Custmers)

app.mainloop()

#WRONG SHIZ

#root = Tk()
#root.geometry("1000x690")

#def show():
#    myLabel = Label(root, text=clicked.get()).pack()

#clicked = StringVar()
#clicked.set("Menu")

#drop = OptionMenu(root, clicked, menu)
#drop.pack()

#myButton = Button(root, text="Selected_orders", command=show).pack()
#root.mainloop()