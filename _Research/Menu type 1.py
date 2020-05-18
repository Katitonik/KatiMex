from enum import IntEnum
from collections import namedtuple

# The dish is the 'main'namedtuple of the program
Dish = namedtuple('Dish', ['name', 'spicyness', 'size'])


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

# Menu items will heve set size and spiciness (for now)


Nachos = Dish("Nachos", spicyness.Mild, size.S)
Hard_Shell_Tacos = Dish("Hard_shell_tacos", spicyness.Hot, size.M)
Soft_Shell_Tacos = Dish("Soft_shell_tacos", spicyness.Why, size.How)
Chiles_Rellenos = Dish("Chiles_Rellenos", spicyness.Why, size.S)
Chimichangas = Dish("Chimichangas", spicyness.Hot, size.M)
Chilato_de_Pollo = Dish("Chilato_de_Pollo", spicyness.Mild, size.S)
Sopa_de_Cameron = Dish("Sopa_de_Cameron", spicyness.Very_Hot, size.L)
Cochnita_pibli = Dish("Cochnita_pibli", spicyness.Hot, size.M)
Mole = Dish("Mole", spicyness.Hot, size.How)
Aguachile = Dish("Aguachile", spicyness.Why, size.How)
Enchiladas = Dish("Enchiladas", spicyness.Mild, size.L)

menu = [Nachos, Hard_Shell_Tacos, Soft_Shell_Tacos, Chiles_Rellenos, Chimichangas,
        Chilato_de_Pollo, Sopa_de_Cameron, Cochnita_pibli, Mole, Aguachile, Enchiladas]

# I want the menu displayed from A - Z thus i use .sort
menu.sort()

print(menu)

# The sides that can be added to the dish
Side = namedtuple("Side", ["option", "Amount"])


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


# NOT PART OF MENU - SEPERATE STUFF:

# The information of the employee
Employee = namedtuple("Employee", ("ID", "name", "Role", "psswdhash"))
# psswdhash (password) = hash which returns the hash value of the given option, this gives a good 'randomized'
# password
Alex = Employee("101", "Alex", "Cashier", psswdhash=hash("I cant remember!"))
Sam = Employee("102", "Sam", "Delivery driver", psswdhash=hash("do you know?"))
Jo = Employee("103", "Jo", "Clerk", psswdhash=hash("i dont know!"))

employees = [Alex, Sam, Jo]

print(employees)


class suburb(IntEnum):
    Long_Bay = 0
    Browns_bay = 1
    Torbay = 2
    Albany = 3
    Silverdale = 4


customer = namedtuple('Customer', ('name', 'phonenumber', 'address', 'suburb'))

Emile_Matthews = customer('Emile_Matthews', '0789121980',
                          '4c_Pongola_Rd', suburb.Torbay)
Marissa_Moore = customer('Marissa_Moore', '0783456236',
                         '2b_Capecod_Rd', suburb.Long_Bay)
Sandra_Koen = customer('Sandra_Koen', '0201457836',
                       '30_Tui_Rd', suburb.Browns_bay)
Koos_Koombuis = customer('Koos_Kombuis', '0208963773',
                         '777_Kiwi_Ln', suburb.Albany)
Jan_Blauukaas = customer('Jan_Blauukaas', '0220982454',
                         '776_Kiwi_Ln', suburb.Albany)
Pieter_Pan = customer('Pieter_Pan', '02215568903',
                      '9_Pamela_Cres', suburb.Silverdale)

Custmers = [Emile_Matthews, Marissa_Moore, Sandra_Koen,
            Koos_Koombuis, Jan_Blauukaas, Pieter_Pan]

print(Custmers)
