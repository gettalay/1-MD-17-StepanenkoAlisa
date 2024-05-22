import tkinter as tk
from tkinter import *
from tkinter import messagebox


class IceCreamStand:
    def __init__(self, restaurant_name, cuisine_type, initial_rating, flavors, location, working_hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.initial_rating = initial_rating
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_flavors(self):
        flavor_info = f'Список сортов мороженого в кафе-мороженом {self.restaurant_name}:\n'
        for flavor in self.flavors:
            flavor_info += f'{flavor}\n'
        return flavor_info


flavors_list = ['ваниль', 'клубника', 'шоколад', 'крем-брюле', 'лимонный пирог']
ice_cream_stand = IceCreamStand('Lucky sweet', 'кафе-мороженое', '4.8', flavors_list,
                                'Санкт-Петербург, Ударников д.29', 'С 10:00 До 20:00 Ежедневно')

window = tk.Tk()
window.title(f'Информация о кафе-мороженом {ice_cream_stand.restaurant_name}')

label1 = tk.Label(window, text=f'Адрес : {ice_cream_stand.location}')
label1.pack()

label2 = tk.Label(window, text=f'Время работы: {ice_cream_stand.working_hours}')
label2.pack()

label3 = tk.Label(window, text=ice_cream_stand.display_flavors())
label3.pack()

window.mainloop()
