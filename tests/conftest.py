import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_product():
    return Product("Laptop", "High-end gaming laptop", 1500.00, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Electronics", "Gadgets and devices", [sample_product])


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield
