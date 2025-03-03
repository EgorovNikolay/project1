import pytest
from src.category import Category
from src.product import Product


def test_category_initialization(sample_category):
    """Проверка корректности инициализации категории."""
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Gadgets and devices"
    assert len(sample_category._Category__products) == 1
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product(sample_category, sample_product):
    new_product = Product("Mouse", "Wireless mouse", 50.00, 20)
    sample_category.add_product(new_product)
    assert len(sample_category._Category__products) == 2
    assert Category.product_count == 2


def test_add_product_invalid_type(sample_category):
    invalid_product = {"name": "Invalid", "price": 100, "quantity": 1}
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников."):
        sample_category.add_product(invalid_product)


def test_products_getter(sample_category, sample_product):
    expected_output = "Laptop, 1500.0 руб. Остаток: 10 шт."
    assert sample_category.products == expected_output


def test_category_count(sample_category):
    assert Category.category_count == 1


def test_product_count(sample_category):
    assert Category.product_count == 1


def test_category_str():
    product1 = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    product2 = Product("Mouse", "Wireless mouse", 50.00, 20)
    category = Category("Electronics", "Gadgets and devices", [product1, product2])
    expected_output = "Electronics, количество продуктов: 30 шт."
    assert str(category) == expected_output


def test_category_products():
    product1 = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    product2 = Product("Mouse", "Wireless mouse", 50.00, 20)
    category = Category("Electronics", "Gadgets and devices", [product1, product2])
    expected_output = "Laptop, 1500.0 руб. Остаток: 10 шт.\nMouse, 50.0 руб. Остаток: 20 шт."
    assert category.products == expected_output


def test_add_product_to_category():
    product1 = Product("Laptop", "High-end gaming laptop", 1500.00, 10)
    category = Category("Electronics", "Gadgets and devices", [product1])
    product2 = Product("Mouse", "Wireless mouse", 50.00, 20)
    category.add_product(product2)
    assert len(category._Category__products) == 2
    assert str(category) == "Electronics, количество продуктов: 30 шт."
