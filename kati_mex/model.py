from datetime import datetime
from decimal import Decimal
from enum import IntEnum
from typing import NamedTuple
from typing import List
from typing import Set
from typing import Union


class Spicyness(IntEnum):
    """ An indicator of how spycy a dish is. """
    # TODO: remove `Undefined` eunmeration?
    Undefined = 0
    Mild = 10
    Hot = 20
    Flaming = 50
    Hell = 100


class Dish(NamedTuple):
    """ A Mexican dish. ¡Por favor! """
    name: str
    spicyness: Spicyness


def new_dish(name: str, spicyness: Spicyness) -> Dish:
    """ Create a new dish.

    Args:
        name: The name of this dish.
        spicyness: See Spicyness.

    Returns:
        A new dish.
    """
    if name == "" or is None:
        raise ValueError('Dish name cannot be empty or None.')

    result = Dish(name=name, spicyness=spicyness)
    return result


class Side(NamedTuple):
    """ A side dish. ¡Ay!. """
    name: str


def new_side(name: str) -> Side:
    """ Create a side dish.

    Args:
        name: The name of the side dish.

    Returns:
        A new side dish.
    """
    if name == "" or is None:
        raise ValueError('Dish name cannot be empty or None.')

    result = Side(name=name)
    return result


class Role(IntEnum):
    """ The role of an employee. ¡Ole! """
    # TODO: remove `Undefined` eunmeration?
    Undefined = 0
    Chef = 10
    Server = 20
    Driver = 30
    Cashier = 40
    Boss = 50


class Employee(NamedTuple):
    """ An employee of KatiMex. ¡Ándele, ándele! """
    number: str
    name: str
    role: Role = Role.Undefined


def new_employee(name: str, role: Role) -> Employee:
    """ Create a new employee.

    Args:
        name: The employee's name.
        role: The role of the employee.

    Returns:
        A new employee.
    """
    # TODO: number should be auto-generated
    result = Employee(number=number, name=name, role=role)
    return result


class OrderHeader(NamedTuple):
    """ Order header to identify the order. """
    # TODO: there should be an auto-generated order number
    date: datetime
    taker: Employee
    deliver: bool
    address: List[str]


def new_order_header(
    taker: Employee,
    deliver: bool,
    address: List[str]
) -> OrderHeader:
    """ Create a new order header.

    Args:
        taker: Who took the order?
        deliver: Is this order for delivery?
        address: What is the delivery address?

    Returns:
        A new order header.
    """
    result = OrderHeader(
        date=datetime.now(), taker=taker, deliver=deliver, address=address
    )
    return result


class Size(IntEnum):
    """ How big is the dish or side dish? """
    # TODO: remove `Undefined` eunmeration?
    Undefined = 0
    Small = 10
    Medium = 20
    Large = 30


class OrderItem(NamedTuple):
    """ A order item.

    An order usually has multiple order items.
    """
    item: Union[Dish, Side]
    quantity: int
    size: Size
    unit_price: Decimal
    item_price: Decimal


def _lookup_price(item: Union[Dish, Side], size: Size) -> Decimal:
    # Look up a dish or side dish's price.
    #
    # Args:
    #     item: The dish or side dish for which the price will be looked up.
    #     size: The size the item.
    #
    # Returns:
    #     A price based on the dish/side dish and the size of the item.
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
    # A `Small` item has no scale factor, `Medium` items are 20% more
    # expensive than `Small`items and `Large` items are 30% more expensive.
    scale = scale_factor.get(size, Decimal(0))
    result = price * scale
    return result


def new_order_item(
    item: Union[Dish, Side],
    quantity: int,
    size: Size
) -> OrderItem:
    """ Create a new order item.

    Args:
        item: The line item.
        quantity: How many do you want?
        size: What size is the item?

    Returns:
        An order line.
    """
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
    """ Summary of an order. """
    sub_total: Decimal
    tax: Decimal
    total: Decimal


def new_order_footer(items: List[OrderItem]) -> OrderFooter:
    """  Create an order footer.

    Args:
        items: The line iems of the order.

    Returns:
        A order footer with calculated subtotal, tax and total.
    """
    sub_total = Decimal('0.00')
    for item in items:
        sub_total += item.item_price
    tax = sub_total * Decimal('0.14')
    total = sub_total + tax

    result = OrderFooter(sub_total=sub_total, tax=tax, total=total)
    return result


class Order(NamedTuple):
    """ An order.

    Has an order header, line items and an order footer.
    """
    header: OrderHeader
    items: List[OrderItem]
    footer: OrderFooter


def new_order(
    header: OrderHeader,
    items: List[OrderItem],
    footer: OrderFooter
) -> Order:
    """ Create an order.

    Args:
        header: Order header.
        items: Order line items.
        footer: Order footer.

    Returns:
        A newly created order.
    """
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
