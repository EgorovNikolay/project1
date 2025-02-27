import pytest
from unittest.mock import mock_open, patch
import json

from src.utils import load_data_from_json


def test_load_data_from_json():
    """Проверка загрузки данных из JSON-файла и создания объектов."""
    # Мок данных JSON
    json_data = """
    [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55\\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    """

    # Мок для open и json.load
    with patch("builtins.open", mock_open(read_data=json_data)):
        categories = load_data_from_json("dummy_path.json")

        # Проверки
        assert len(categories) == 2  # Должно быть 2 категории

        # Проверка первой категории (Смартфоны)
        assert categories[0].name == "Смартфоны"
        assert (
            categories[0].description
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
        )
        assert len(categories[0]._Category__products) == 2  # 2 товара в категории
        assert categories[0]._Category__products[0].name == "Samsung Galaxy C23 Ultra"
        assert categories[0]._Category__products[1].name == "Iphone 15"

        # Проверка второй категории (Телевизоры)
        assert categories[1].name == "Телевизоры"
        assert (
            categories[1].description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        )
        assert len(categories[1]._Category__products) == 1  # 1 товар в категории
        assert categories[1]._Category__products[0].name == '55" QLED 4K'


def test_load_data_from_json_file_not_found():
    """Проверка обработки ошибки, если файл не существует."""
    with patch("builtins.open", side_effect=FileNotFoundError("Файл не найден")):
        with pytest.raises(FileNotFoundError):
            load_data_from_json("non_existent_file.json")


def test_load_data_from_json_invalid_format():
    """Проверка обработки ошибки, если файл имеет неверный формат."""
    invalid_json_data = "invalid json data"
    with patch("builtins.open", mock_open(read_data=invalid_json_data)):
        with pytest.raises(json.JSONDecodeError):
            load_data_from_json("invalid_file.json")
