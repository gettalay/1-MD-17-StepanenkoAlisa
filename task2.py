class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"В Ресторане {self.restaurant_name} предлагается {self.cuisine_type} кухня.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

restaurant1 = Restaurant("La Trattoria", "итальянская")
restaurant2 = Restaurant("Le Bistro", "французская")
restaurant3 = Restaurant("Taj Mahal", "индийская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
