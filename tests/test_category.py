import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def sample_product():
    return Product("Laptop", "High-end gaming laptop", 1500.00, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Electronics", "Gadgets and devices", [sample_product])


def test_category_initialization(sample_category):
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


def test_products_getter(sample_category, sample_product):
    expected_output = "Laptop, 1500.0 руб. Остаток: 10 шт."
    assert sample_category.products == expected_output


def test_category_count(sample_category):
    assert Category.category_count == 1


def test_product_count(sample_category):
    assert Category.product_count == 1
