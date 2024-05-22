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

restaurant1 = Restaurant("La Trattoria", "итальянская", 4.5)

restaurant1.describe_restaurant()

restaurant1.update_rating(4.8)
restaurant1.describe_restaurant()
