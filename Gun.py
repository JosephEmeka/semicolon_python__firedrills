
class Gun:
    def __init__(self, name: str):
        self.__name = name
        self.__bullet = 0

    def load(self, amount):
        if amount <= 0:
            raise ValueError("How do you want to add negative numbers?")
        else:
            self.__bullet += amount

    def unload_some_bullet(self, amount):
        if amount <= 0:
            raise ValueError("How do you want to unload negative numbers?")
        else:
            self.__bullet -= amount

    def unload_all_bullet(self):
        self.__bullet = 0

    def get_total_number_of_bullets(self):
        return self.__bullet

    def shoot(self):
        if self.__bullet > 0:
            print(f" {self.name} fired.")
            self.__bullet -= 1
        else:
            print("Click! Out of bullets.")
