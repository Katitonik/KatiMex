from datetime import datetime
from decimal import Decimal
from enum import IntEnum
from typing import NamedTuple
from typing import List
from typing import Set


class Spicyness(IntEnum):
    """ An indicator of how spycy a dish is. """
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
        name (str): The name of this dish.
        spicyness (Spicyness): See Spicyness.

    Returns:
        A new dish.
    """
    if (name == "") or (name is None):
        raise ValueError('Dish name cannot be empty or None.')

    result = Dish(name=name, spicyness=spicyness)
    return result


def _generate_id(now: datetime) -> str:
    tt = now.timetuple()
    ty = tt.tm_year
    td = tt.tm_yday
    tc = (tt.tm_hour * 3600) + (tt.tm_min * 60) + tt.tm_sec

    result = f'{ty}-{td}{tc}'
    return result


class OrderHeader(NamedTuple):
    """ Order header to identify the order. """
    number: str
    date: datetime
    deliver: bool
    client_name: str
    client_contact: str
    client_street: str
    client_suburb: str


def new_order_header(
    deliver: bool,
    client_name: str,
    client_contact: str,
    client_street: str,
    client_suburb: str
) -> OrderHeader:
    """ Create a new order header.

    Args:
        deliver (bool): Is this order for delivery?
        client_name (str): Client identifier.
        client_contact (str): Contact telephone nmber.
        client_street (str): Street name.
        client_suburb (str): Suburb name.

    Returns:
        A new order header.
    """
    if deliver:
        if (not client_street) and (not client_suburb):
            raise ValueError('Street and suburb required for deliveries.')

    now = datetime.now()
    result = OrderHeader(
        number=_generate_id(now),
        date=now,
        deliver=deliver,
        client_name=client_name,
        client_contact=client_contact,
        client_street=client_street,
        client_suburb=client_suburb
    )
    return result


class Size(IntEnum):
    """ How big is the dish or side dish? """
    Small = 10
    Medium = 20
    Large = 30


class OrderItem(NamedTuple):
    """ A order item.

    An order usually has multiple order items.
    """
    item: Dish
    quantity: int
    size: Size
    unit_price: Decimal
    item_price: Decimal


def _lookup_price(item: Dish, size: Size) -> Decimal:
    # Look up a dish or side dish's price.
    #
    # Args:
    #     item (Union[Dish, Side]): The dish or side dish for which the
    # price will be looked up.
    #     size (Size): The size the item.
    #
    # Returns:
    #     A price based on the dish/side dish and the size of the item.
    price_list = {
        # Dishes
        'Aguachile': Decimal('11.50'),
        'Chilato de Pollo': Decimal('08.50'),
        'Chiles Rellenos': Decimal('08.50'),
        'Chimichangas': Decimal('08.50'),
        'Cochnita pibli': Decimal('11.50'),
        'Enchiladas': Decimal('08.50'),
        'Hard Shell Tacos': Decimal('08.50'),
        'Mole': Decimal('11.50'),
        'Nachos': Decimal('08.50'),
        'Soft Shell Tacos': Decimal('08.50'),
        'Sopa de Cameron': Decimal('11.50'),
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
    item: Dish,
    quantity: int,
    size: Size
) -> OrderItem:
    """ Create a new order item.

    Args:
        item (Union[Dish, Side]): The line item.
        quantity (int): How many do you want?
        size (Size): What size is the item?

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
    delivery_charge: Decimal
    subtotal: Decimal
    tax: Decimal
    total: Decimal


def new_order_footer(
    header: OrderHeader,
    items: List[OrderItem]
) -> OrderFooter:
    """  Create an order footer.

    Args:
        header (OrderHeader): Order header to check fordelivery charge.
        items (List[OrderItem]): The line iems of the order.

    Returns:
        A order footer with calculated subtotal, tax and total.
    """
    delivery_charge = Decimal('0.00')
    if header.deliver:
        delivery_charge = Decimal('3.00')

    subtotal = Decimal('0.00')
    for item in items:
        subtotal += item.item_price

    tax = subtotal * Decimal('0.14')

    total = delivery_charge + subtotal + tax

    result = OrderFooter(
        delivery_charge=delivery_charge,
        subtotal=subtotal,
        tax=tax,
        total=total)
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
) -> Order:
    """ Create an order.

    Args:
        header (OrderHeader): Order header.
        items (List[OrderItem]): Order line items.
        footer (OrderFooter): Order footer.

    Returns:
        A newly created order.
    """
    footer = new_order_footer(header, items)
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
