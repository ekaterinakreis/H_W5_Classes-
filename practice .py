def add(x, y):
    return x + y

class Animal:
    def __init__(self, name, place, food):
        self.name = name
        self.place = place
        self.food = food

    def get_name(self):
        print(f'Animal: {self.name}')

    def get_place(self):
        print(f'Place: {self.place}')

    def get_food(self):
        print(f'Food: {self.food}')

an1 = Animal("Cat", "world", "milk")
print(an1.__dict__)
print(an1.get_name())
print(an1.get_place())
print(an1.get_food())
