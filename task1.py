class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"В Ресторане {self.restaurant_name} предлагается {self.cuisine_type} кухня.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


newRestaurant = Restaurant("La Trattoria", "итальянская")

print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
