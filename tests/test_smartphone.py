import pytest
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.product import Product

def test_add_same_type_smartphone():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    result = smartphone1 + smartphone2
    expected_result = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
    assert result == expected_result, f"Ожидалось {expected_result}, но получено {result}"


def test_add_different_type_smartphone():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        result = smartphone + grass


def test_add_non_product_smartphone():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")

    with pytest.raises(TypeError):
        result = smartphone + "Not a product"

def test_smartphone_initialization():
    smartphone = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_smartphone_inheritance():
    smartphone = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )
    assert isinstance(smartphone, Product)