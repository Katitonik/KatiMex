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

menu = [Nachos, Hard_Shell_Tacos, Soft_Shell_Tacos, Chiles_Rellenos,
        Chimichangas, Chilato_de_Pollo, Sopa_de_Cameron, Cochnita_pibli,
        Mole, Aguachile, Enchiladas]

menu.sort()

print(menu)
