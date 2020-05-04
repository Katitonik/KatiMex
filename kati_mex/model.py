from typing import NamedTuple
from typing import Set
from enum import IntEnum


class Spicyness(IntEnum):
    """ How hot is the dish? """
    Undefined = 0
    Mild = 10
    Hot = 20
    Flaming = 50
    Hell = 100


class Size(IntEnum):
    """ How big is the dish? """
    Undefined = 0
    Small = 10
    Medium = 20
    Large = 30


class Dish(NamedTuple):
    name: str
    spyciness: Spicyness = Spicyness.Undefined
    size: Size = Size.Undefined


class Side(NamedTuple):
    name: str
    quantity: int
    size: Size = Size.Undefined


class Role(IntEnum):
    Undefined = 0
    Chef = 10
    Server = 20
    Driver = 30
    Cashier = 40
    Boss = 50


class Employee(NamedTuple):
    number: int
    name: str
    role: Role = Role.Undefined


def menu() -> Set[str]:
    result = {
        "Nachos",
        "Hard shell tacos",
        "Soft shell tacos",
        "Chiles Rellenos",
        "Chimichangas",
        "Chilato de Pollo",
        "Sopa de Cameron",
        "Cochnita pibli",
        "Mole",
        "Aguachile",
        "Enchiladas",
    }
    return result
