class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных типов (например, смартфон и траву).")
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                confirmation = input("Цена снижается. Подтвердите действие (y/n): ")
                if confirmation.lower() == "y":
                    self.__price = new_price
                else:
                    print("Изменение цены отменено.")
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
