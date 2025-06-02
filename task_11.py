class Dessert:
    def __init__(self, name="Nothing", calories=0):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True


icecream = Dessert("Icecream", 250)
print(icecream.get_name())
print(icecream.get_calories())
print(icecream.is_healthy())
print(icecream.is_delicious())

cookie = Dessert()
cookie.set_name("Cookie")
cookie.set_calories(150)
print(cookie.is_healthy())
print(cookie.is_delicious())
