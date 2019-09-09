class Chef:

    def make_chicken(self):
        print("Chicken")

    def make_salad(self):
        print("Salad")

    def make_special_dish(self):
        print("Dish")

class ChineseChef(Chef):

    def make_rice(self):
        print("Rice")

    def make_pasta(self):
        print("Pasta")

myChef = ChineseChef()
myChef.make_chicken()