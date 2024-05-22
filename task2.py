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
    def __init__(self, restaurant_name, cuisine_type, initial_rating, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type, initial_rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_flavors(self):
        print(f'Список сортов мороженого в кафе-мороженом {self.restaurant_name}: ')
        for flavor in self.flavors:
            print(flavor)
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f'Добавлен новый вкус мороженого {new_flavor}')
    def delete_flavor(self, remove_flavor):
        if remove_flavor in self.flavors:
            self.flavors.remove(remove_flavor)
            print(f'Вкуса мороженого {remove_flavor} больше нет')
        else:
            print(f'Вкус мороженого {remove_flavor} не найден')
    def serve_in_cone(self):
        print(f'Подается в рожке в кафе-мороженом {self.restaurant_name}')

    def serve_on_stick(self):
        print(f'Подается на палочке в кафе-мороженом {self.restaurant_name}')

    def serve_in_cup(self):
        print(f'Подается в стаканчике в кафе-мороженом {self.restaurant_name}')

ice_cream_stand = IceCreamStand('Lucky sweet', 'кафе-мороженое', '4.8', ['ваниль','клубника','шоколад','крем-брюле','лимонный пирог'],
                                'Санкт-Петербург, Ударников д.29', 'С 10:00 До 20:00 Ежедневно')

print(f'Кафе-мороженое {ice_cream_stand.restaurant_name} c рейтингом {ice_cream_stand.rating} работает {ice_cream_stand.working_hours} по адресу: {ice_cream_stand.location}')

ice_cream_stand.add_flavor('карамель')
ice_cream_stand.delete_flavor('лимонный пирог')
ice_cream_stand.display_flavors()

ice_cream_stand.serve_in_cone()
ice_cream_stand.serve_in_cup()
ice_cream_stand.serve_on_stick()