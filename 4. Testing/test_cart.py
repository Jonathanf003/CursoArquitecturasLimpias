import pytest
from cart import Cart


def test_add_product_and_calculate_total():
    cart = Cart()
    cart.add_product(Product("Product 1", 50))
    assert cart.calculate_total() == 50

def test_remove_product():
    cart = Cart()
    product = Product("Product 1", 50)
    cart.add_product(product)
    cart.remove_product(product)
    assert cart.calculate_total() == 0

def test_add_product_with_negative_price():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_product(Product("Product 1", -50))

from pytest_bdd import scenarios, given, when, then

scenarios("test_cart.feature")

@given("a cart with total price $total_price")
def cart_with_total(total_price):
    return Cart(total_price)

@when("I add a product with price $product_price")
def add_product_with_price(cart_with_total, product_price):
    cart_with_total.add_product(Product("Product 1", int(product_price)))

@then("the total price should be $expected_total")
def total_price_should_be(cart_with_total, expected_total):
    assert cart_with_total.calculate_total() == int(expected_total)