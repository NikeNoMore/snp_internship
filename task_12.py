class JellyBean:
    def __init__(self, name="Nothing", calories=0, flavor="bland"):
        self.name = name
        self.cals = calories
        self.flav = flavor

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.cals

    def get_flavor(self):
        return self.flav

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.cals = calories

    def set_flavor(self, flavor):
        self.flav = flavor

    def is_healthy(self):
        return self.cals < 200

    def is_delicious(self):
        return self.flav != "black licorice"


pink_jb = JellyBean("Pink jelly bean", 25, "strawberry")
print(pink_jb.get_name())
print(pink_jb.get_calories())
print(pink_jb.get_flavor())
print(pink_jb.is_healthy())
print(pink_jb.is_delicious())

black_jb = JellyBean()
black_jb.set_name("Black jelly bean")
black_jb.set_calories(25)
black_jb.set_flavor("black licorice")
print(black_jb.is_healthy())
print(black_jb.is_delicious())
