from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
import pytest


def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High-end gaming laptop"
    assert sample_product.price == 1500.00
    assert sample_product.quantity == 10


def test_new_product():
    product_data = {"name": "Keyboard", "description": "Mechanical keyboard", "price": 100.00, "quantity": 5}
    product = Product.new_product(product_data)
    assert product.name == "Keyboard"
    assert product.description == "Mechanical keyboard"
    assert product.price == 100.00
    assert product.quantity == 5


def test_price_setter_positive(sample_product):
    sample_product.price = 2000.00
    assert sample_product.price == 2000.00


def test_price_setter_negative(sample_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = -100
    assert sample_product.price == 1500.00


def test_price_setter_zero(sample_product):
    sample_product.price = 0
    assert sample_product.price == 1500.00


def test_price_setter_confirmation(sample_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 1000.00
    assert sample_product.price == 1000.00

    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 800.00
    assert sample_product.price == 1000.00

def test_product_str():
    product = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    expected_output = "Laptop, 1500.0 руб. Остаток: 10 шт."
    assert str(product) == expected_output

def test_product_addition():
    product1 = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    product2 = Product("Mouse", "Wireless mouse", 50.00, 20)
    total_value = product1 + product2
    expected_value = (1500.00 * 10) + (50.00 * 20)
    assert total_value == expected_value

def test_add_product_valid():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")
    category = Category("Смартфоны", "Высокотехнологичные смартфоны", [])
    category.add_product(smartphone)
    assert len(category._Category__products) == 1


def test_add_product_invalid():
    category = Category("Смартфоны", "Высокотехнологичные смартфоны", [])
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников."):
        category.add_product("Not a product")

def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_valid_quantity():
    product = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    assert product.name == "Laptop"
    assert product.quantity == 10