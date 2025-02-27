from src.product import Product
from src.category import Category
import json


def load_data_from_json(file_path: str):
    """Чтение данных из json - файла и получение из файла данных для экземпляров класса"""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        categories = []
        for category_data in data:
            products = [Product(**product) for product in category_data["products"]]
            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)
        return categories
