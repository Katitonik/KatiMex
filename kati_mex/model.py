from enum import IntEnum
from datetime import datetime
from numbers import Decimal
from typing import NamedTuple
from typing import List
from typing import Set


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
    price: Decimal


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


class OrderHeader(NamedTuple):
    date: datetime
    taker: Employee
    deliver: bool
    address: List[str]


class OrderItem(NamedTuple):
    dish: Dish
    quantity: int
    price: Decimal


class OrderFooter(NamedTuple):
    sub_total: Decimal
    tax: Decimal
    total: Decimal


class Order(NamedTuple):
    header: OrderHeader
    items: List[OrderItem]
    footer: OrderFooter


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
