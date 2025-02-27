from src.product import Product


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
