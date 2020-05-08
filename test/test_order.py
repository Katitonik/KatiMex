from decimal import Decimal
import kati_mex.model as model


def test_single_small_dish_order_item():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 1, model.Size.Small)
    lhs = Decimal('10.00')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_small_dish_order_item():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 3, model.Size.Small)
    lhs = Decimal('30.00')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_medium_dish_order_item():
    dish = model.new_dish('Mole', model.Spicyness.Hot)
    item = model.new_order_item(dish, 3, model.Size.Medium)
    lhs = Decimal('36.00')
    rhs = item.item_price

    assert lhs == rhs


def test_single_small_side_order_item():
    side = model.new_side('Chips')
    item = model.new_order_item(side, 1, model.Size.Small)
    lhs = Decimal('3.00')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_small_side_order_item():
    side = model.new_side('Chips')
    item = model.new_order_item(side, 3, model.Size.Small)
    lhs = Decimal('9.00')
    rhs = item.item_price

    assert lhs == rhs


def test_multiple_large_side_order_item():
    side = model.new_side('Chips')
    item = model.new_order_item(side, 3, model.Size.Large)
    lhs = Decimal('11.70')
    rhs = item.item_price

    assert lhs == rhs


def test_order_header():
    taker = model.new_employee("E0000", "Jo", model.Role.Cashier)
    header = model.new_order_header(
        taker=taker,
        deliver=True,
        address=["10 First Street", "Long Bay"])

    assert header


def test_order_footer():
    import kati_mex.model as model
    from decimal import Decimal

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

    footer = model.new_order_footer(order_items)

    sub_total = order_items[0].item_price + \
        order_items[1].item_price + \
        order_items[2].item_price + \
        order_items[3].item_price + \
        order_items[4].item_price
    assert footer.sub_total == sub_total

    tax = sub_total * Decimal('0.14')
    assert footer.tax == tax

    total = sub_total + tax
    assert footer.total == total
