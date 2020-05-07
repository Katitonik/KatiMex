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
