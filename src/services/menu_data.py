from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.items = self.__read_file(source_path)
        self.dishes = self.__create_menu()

    def __read_file(self, path: str):
        with open(path, "r") as file:
            menu = csv.DictReader(file)

            return list(menu)

    def __create_menu(self):
        menu_dict = {}

        for item in self.items:
            dish = Dish(item["dish"], float(item["price"]))
            ingredient = Ingredient(item["ingredient"])
            amount = int(item["recipe_amount"])

            if dish not in menu_dict:
                menu_dict[dish] = dish

            menu_dict[dish].add_ingredient_dependency(
                ingredient, amount
            )

        return {value for value in menu_dict.values()}
