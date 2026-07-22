#2 types of products shoes, and slides

#ticket 1
class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Shoes(name={self.name!r}, price={self.price})"

    # ticket 3
    def set_price(self, new_price):
        if new_price < 0:
            print("no")
        else:
            self.price = new_price

    # ticket 5
    def deliver(self):
        print("Shipping your sneakers!")


#ticket2 two items
item1 = Shoes("Airforce1", 120)
item2 = Shoes("Airjordan4", 240)
print(item1.name)
#it will likely say Airforce1,120

#ticket 4
class Slide(Shoes):
    def deliver(self):
        print("Sneaks OTW!")

slide1 = Slide("YZY Slides", 20)
print(slide1.name)
print(slide1.price)

# ticket 5
item1.deliver()
slide1.deliver()
# EXPLAIN: Shoes and Slide both have a deliver methods but each has it's own way due to the class making it neccessary to split up

# ticket 6 + 9 (Cart, combined into one class)
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total += item.price
        print("Total: $" + str(total))


#ticket 7
menu = {"1": item1, "2": item2}
cart = Cart()

#ticket 8
while True:
    choice = input("Pick 1, 2, or 'done': ")
    if choice == "done":
        break
    else:
        cart.add(menu[choice])
        print(menu[choice].name + " added!")

#ticket 9
cart.checkout()