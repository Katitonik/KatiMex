import pytest
from decimal import Decimal
import kati_mex.model as model


def test_single_small_dish_order_item():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 1, model.Size.Small)
    lhs = Decimal('11.50')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_small_dish_order_items():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 3, model.Size.Small)
    lhs = Decimal('34.50')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_medium_dish_order_items():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 3, model.Size.Medium)
    lhs = Decimal('41.40')
    rhs = item.item_price

    assert lhs == rhs


def test_delivery_order_header():
    header = model.new_order_header(
        deliver=True,
        client_name="Jo",
        client_contact="+64 12 345 6789",
        client_street="101 Some Street",
        client_suburb="Long Bay"
    )

    assert header


def test_delivery_order_header_failure():
    with pytest.raises(ValueError):
        model.new_order_header(
            deliver=True,
            client_name="Jo",
            client_contact="+64 12 345 6789",
            client_street="",
            client_suburb=""
        )


def test_collect_order_footer():
    import kati_mex.model as model
    from decimal import Decimal

    order_header = model.new_order_header(
        deliver=False,
        client_name="",
        client_contact="",
        client_street="",
        client_suburb=""
    )

    nachos = model.new_dish('Nachos', model.Spicyness.Hot)
    chimichangas = model.new_dish('Chimichangas', model.Spicyness.Hot)
    mole = model.new_dish('Mole', model.Spicyness.Hell)
    aguachile = model.new_dish('Aguachile', model.Spicyness.Flaming)
    enchiladas = model.new_dish('Enchiladas', model.Spicyness.Mild)
    order_items = [
        model.new_order_item(nachos, 1, model.Size.Small),
        model.new_order_item(chimichangas, 1, model.Size.Small),
        model.new_order_item(mole, 1, model.Size.Small),
        model.new_order_item(aguachile, 1, model.Size.Small),
        model.new_order_item(enchiladas, 1, model.Size.Small),
    ]

    footer = model.new_order_footer(order_header, order_items)

    subtotal = order_items[0].item_price + \
        order_items[1].item_price + \
        order_items[2].item_price + \
        order_items[3].item_price + \
        order_items[4].item_price
    assert footer.subtotal == subtotal

    tax = subtotal * Decimal('0.14')
    assert footer.tax == tax

    total = subtotal + tax
    assert footer.total == total


def test_delivery_order_footer():
    import kati_mex.model as model
    from decimal import Decimal

    order_header = model.new_order_header(
        deliver=True,
        client_name="Alex",
        client_contact="+64 12 345 6789",
        client_street="Some Street",
        client_suburb="Long Bay"
    )

    nachos = model.new_dish('Nachos', model.Spicyness.Hot)
    chimichangas = model.new_dish('Chimichangas', model.Spicyness.Hot)
    mole = model.new_dish('Mole', model.Spicyness.Hell)
    aguachile = model.new_dish('Aguachile', model.Spicyness.Flaming)
    enchiladas = model.new_dish('Enchiladas', model.Spicyness.Mild)
    order_items = [
        model.new_order_item(nachos, 1, model.Size.Small),
        model.new_order_item(chimichangas, 1, model.Size.Small),
        model.new_order_item(mole, 1, model.Size.Small),
        model.new_order_item(aguachile, 1, model.Size.Small),
        model.new_order_item(enchiladas, 1, model.Size.Small),
    ]

    footer = model.new_order_footer(order_header, order_items)

    delivery_charge = Decimal('3.00')
    assert footer.delivery_charge == delivery_charge

    subtotal = order_items[0].item_price + \
        order_items[1].item_price + \
        order_items[2].item_price + \
        order_items[3].item_price + \
        order_items[4].item_price
    assert footer.subtotal == subtotal

    tax = subtotal * Decimal('0.14')
    assert footer.tax == tax

    total = delivery_charge + subtotal + tax
    assert footer.total == total
