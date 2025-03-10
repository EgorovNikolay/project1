import pytest
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone
from src.product import Product


def test_add_same_type_grass():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    result = grass1 + grass2
    expected_result = (grass1.price * grass1.quantity) + (grass2.price * grass2.quantity)
    assert result == expected_result, f"Ожидалось {expected_result}, но получено {result}"


def test_add_different_type_grass():
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")

    with pytest.raises(TypeError):
        result = grass + smartphone


def test_add_non_product_grass():
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        result = grass + "Not a product"

def test_lawn_grass_initialization():
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_lawn_grass_inheritance():
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    assert isinstance(grass, Product)