from enum import IntEnum
from collections import namedtuple
from tkinter import Tk
from tkinter import ttk

# The dish is the 'main'namedtuple of the program
Dish = namedtuple('Dish', ['name', 'spicyness', 'size'])

# The sides that can be added to the dish
Side = namedtuple("Side", ["option", "Amount"])


class Spicyness(IntEnum):
    Mild = 0
    Hot = 1
    VeryHot = 2
    Why = 3


class Size(IntEnum):
    S = 0
    M = 1
    L = 2
    How = 3


nachos = Dish("Nachos", Spicyness.Mild, Size.S)
hard_shell_tacos = Dish("Hard_shell_tacos", Spicyness.Hot, Size.M)
soft_shell_tacos = Dish("Soft_shell_tacos", Spicyness.Why, Size.How)
chiles_rellenos = Dish("Chiles_Rellenos", Spicyness.Why, Size.S)
chimichangas = Dish("Chimichangas", Spicyness.Hot, Size.M)
chilato_de_pollo = Dish("Chilato_de_Pollo", Spicyness.Mild, Size.S)
sopa_de_cameron = Dish("Sopa_de_Cameron", Spicyness.VeryHot, Size.L)
cochnita_pibli = Dish("Cochnita_pibli", Spicyness.Hot, Size.M)
mole = Dish("Mole", Spicyness.Hot, Size.How)
aguachile = Dish("Aguachile", Spicyness.Why, Size.How)
enchiladas = Dish("Enchiladas", Spicyness.Mild, Size.L)

app = Tk()
app.geometry("690x690")

labelTop = ttk.Label(app, text="El Fuego Cucoracha")
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


guakamole = Side("Guakamole", Size.L)
chips = Side("Chips", Size.S)
salad = Side("Salad", Size.M)
salsa = Side("Salsa", Size.S)

extra = [chips, salad, salsa]

print(extra)

drop_down_extra = ttk.Combobox(app, values=["Chips", "Salad", "Salsa"])
print(dict(drop_down_extra))
drop_down_extra.grid(column=4, row=1)
drop_down_extra.current(0)
print(drop_down_extra.current(), drop_down_extra.get())

# The information of the employee
Employee = namedtuple("Employee", ("ID", "name", "Role", "psswdhash"))
# psswdhash (password) = hash which returns the hash value of the given option,
# this gives a good 'randomized'
# password
alex = Employee("101", "Alex", "Cashier", psswdhash=hash("I cant remember!"))
sam = Employee("102", "Sam", "Delivery driver", psswdhash=hash("do you know?"))
jo = Employee("103", "Jo", "Clerk", psswdhash=hash("i dont know!"))

employees = [alex, sam, jo]

print(employees)


class Suburb(IntEnum):
    LongBay = 0
    BrownsBay = 1
    Torbay = 2
    Albany = 3
    Silverdale = 4


drop_down_suburb = ttk.Combobox(
    app, values=["Long Bay", "Browns Bay", "Torbay", "Albany", "Silverdale"])
print(dict(drop_down_suburb))
drop_down_suburb.grid(column=6, row=1)
drop_down_suburb.current(1)
print(drop_down_suburb.current(), drop_down_suburb.get())
customer = namedtuple('Customer', ('name', 'phonenumber', 'address', 'suburb'))

emile_matthews = customer('Emile_Matthews', '0789121980',
                          '4c_Pongola_Rd', Suburb.Torbay)
marissa_moore = customer('Marissa_Moore', '0783456236',
                         '2b_Capecod_Rd', Suburb.LongBay)
sandra_koen = customer('Sandra_Koen', '0201457836',
                       '30_Tui_Rd', Suburb.BrownsBay)
koos_kombuis = customer('Koos_Kombuis', '0208963773',
                        '777_Kiwi_Ln', Suburb.Albany)
jan_blauukaas = customer('Jan_Blauukaas', '0220982454',
                         '776_Kiwi_Ln', Suburb.Albany)
peter_pan = customer('Pieter_Pan', '02215568903',
                     '9_Pamela_Cres', Suburb.Silverdale)

custmers = [emile_matthews, marissa_moore, sandra_koen,
            koos_kombuis, jan_blauukaas, peter_pan]

print(custmers)

app.mainloop()
