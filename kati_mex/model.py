from datetime import datetime
from decimal import Decimal
from enum import IntEnum
from typing import NamedTuple
from typing import List
from typing import Set
from typing import Union


class Spicyness(IntEnum):
    """ How hot is the dish? """
    Undefined = 0
    Mild = 10
    Hot = 20
    Flaming = 50
    Hell = 100


class Dish(NamedTuple):
    name: str
    spicyness: Spicyness


def new_dish(name: str, spicyness: Spicyness) -> Dish:
    result = Dish(name=name, spicyness=spicyness)
    return result


class Side(NamedTuple):
    name: str


def new_side(name: str) -> Side:
    result = Side(name=name)
    return result


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


def new_empoloyee(number: int, name: str, role: Role) -> Employee:
    result = Employee(number=number, name=name, role=role)
    return result


class OrderHeader(NamedTuple):
    date: datetime
    taker: Employee
    deliver: bool
    address: List[str]


def new_order_header(
    taker: Employee,
    deliver: bool,
    address: List[str]
) -> OrderHeader:
    result = OrderHeader(
        date=datetime.now(), taker=taker, deliver=deliver, address=address
    )
    return result


class Size(IntEnum):
    """ How big is the dish? """
    Undefined = 0
    Small = 10
    Medium = 20
    Large = 30


class OrderItem(NamedTuple):
    item: Union[Dish, Side]
    quantity: int
    size: Size
    unit_price: Decimal
    item_price: Decimal


def _lookup_price(item: Union[Dish, Side], size: Size) -> Decimal:
    price_list = {
        # Dishes
        'Nachos': Decimal('10.00'),
        'Hard shell tacos': Decimal('12.00'),
        'Soft shell tacos': Decimal('11.50'),
        'Chiles Rellenos': Decimal('12.50'),
        'Chimichangas': Decimal('12.00'),
        'Chilato de Pollo': Decimal('14.00'),
        'Sopa de Cameron': Decimal('13.50'),
        'Cochnita pibli': Decimal('11.00'),
        'Mole': Decimal('10.00'),
        'Aguachile': Decimal('15.00'),
        'Enchiladas': Decimal('9.00'),
        # Sides
        'Guakamole': Decimal('4.50'),
        'Sour Cream': Decimal('3.50'),
        'Chips': Decimal('3.00'),
        'Soft Drink': Decimal('2.50')
    }
    scale_factor = {
        Size.Small: Decimal('1.00'),
        Size.Medium: Decimal('1.20'),
        Size.Large: Decimal('1.30')
    }
    price = price_list.get(item.name, Decimal(0))
    scale = scale_factor.get(size, Decimal(0))
    result = price * scale
    return result


def new_order_item(
    item: Union[Dish, Side],
    quantity: int,
    size: Size
) -> OrderItem:
    unit_price = _lookup_price(item, size)
    item_price = unit_price * Decimal(quantity)
    result = OrderItem(
        item=item,
        quantity=quantity,
        size=size,
        unit_price=unit_price,
        item_price=item_price
    )
    return result


class OrderFooter(NamedTuple):
    sub_total: Decimal
    tax: Decimal
    total: Decimal


def new_order_footer(items: List[OrderItem]) -> OrderFooter:
    sub_total = Decimal('0.00')
    for item in items:
        sub_total += item.item_price
    tax = sub_total * Decimal('0.14')
    total = sub_total + tax

    result = OrderFooter(sub_total=sub_total, tax=tax, total=total)
    return result


class Order(NamedTuple):
    header: OrderHeader
    items: List[OrderItem]
    footer: OrderFooter


def new_order(
    header: OrderHeader,
    items: List[OrderItem],
    footer: OrderFooter
) -> Order:
    result = Order(header=header, items=items, footer=footer)
    return result


def menu() -> Set[str]:
    result = {
        'Nachos',
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
