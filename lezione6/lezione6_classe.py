class Food:

    

    def __init__(self, dish_name: str, price: float, available: bool = True):

        self.dish_name: str = dish_name.lower()

        self.price: float = price

        self.available: bool = available

        

    def change_price(self, new_price: float):

        self.price = new_price

    

    def switch_availability(self):

        self.available = not self.available

        

    def __str__(self) -> str:

        return f'Food(dish={self.dish_name}, price={self.price})'

        

class Menu:

    

    def __init__(self, foods: list[Food] = []):

        self.foods: list[Food] = foods

        

    def add_food(self, food: Food):

        if food.available:

            is_in: bool = False

            for food_in_menu in self.foods:

                if food_in_menu.dish_name == food.dish_name:

                    is_in = True

                    break

            if not is_in:

                self.foods.append(food)

        

    def remove_food(self, food: Food):

        self.foods.remove(food)

        

    def clean_menu(self):

        foods_temp: list[Food] = self.foods

        for food in foods_temp:

            if not food.available:

                self.remove_food(food)



class Restaurant:

    

    def __init__(self,

                 name: str,

                 cuisine_type: str,

                 number_served: int = 0,

                 open: bool = False):

        

        self.name: str = name

        self.cuisine_type: str = cuisine_type

        self.number_served: int = number_served

        self.open: bool = open

        self.menu: Menu = Menu()

        

    def open_restaurant(self):

        print(f'Il ristorante {self.name} è aperto')

        self.open = True

        

    def increment_number(self):

        if self.open:

            self.number_served += 1

        

    def close_restaurant(self):

        self.number_served = 0

        self.open = False

        

    def add_item(self, food: Food):

        self.menu.add_food(food)

        

    def remove_item(self, food: Food):

        self.menu.remove_food(food)

        

    def clean_menu(self):

        self.menu.clean_menu()

        

        

r1 = Restaurant(name="La Vecchia Roma", cuisine_type="Romana")

carbonara = Food(dish_name="Carbonara", price=10.5)

pizza_margherita = Food(dish_name="Pizza Margherita", price=8)

r1.add_item(carbonara)

r1.add_item(pizza_margherita)

print(r1.menu.foods)

carbonara.switch_availability()

r1.clean_menu()

print(r1.menu.foods)

r1.add_item(carbonara)

carbonara.switch_availability()

r1.add_item(carbonara)

print(r1.menu.foods)