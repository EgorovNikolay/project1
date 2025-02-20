from src.category import Category
from src.utils import load_data_from_json
from unittest.mock import mock_open, patch


def test_load_data_from_json(sample_json_data):
    with patch("builtins.open", mock_open(read_data=sample_json_data)):
        categories = load_data_from_json("mock.json")
        assert len(categories) == 2
        assert categories[0].name == "Смартфоны"
        assert len(categories[0].products) == 3
        assert categories[1].name == "Телевизоры"
        assert len(categories[1].products) == 1
        assert Category.category_count >= 2
        assert Category.product_count >= 4
