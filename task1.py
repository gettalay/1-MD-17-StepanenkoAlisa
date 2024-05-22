class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"В ресторане {self.restaurant_name} предлагается {self.cuisine_type} кухня. Его рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, initial_rating, flavors):
        super().__init__(restaurant_name, cuisine_type, initial_rating)
        self.flavors = flavors

    def display_flavors(self):
        print(f'Список сортов мороженого в кафе-мороженом {self.restaurant_name}: ')
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand('Lucky sweet', 'кафе-мороженое', '4.8', ['ваниль','клубника','шоколад','крем-брюле','лимонный пирог'])

print(f'Кафе-мороженое {ice_cream_stand.restaurant_name} c рейтингом {ice_cream_stand.rating}')


ice_cream_stand.display_flavors()

