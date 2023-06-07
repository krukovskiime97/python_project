class Compucter:

    def __init__(self):
        self.price = 900

    def get_price(self):
        print(f"Price {self.price}")

    def set_price(self, price):
        if price > 1500:
            price('invalid price')
        else:
             self.price = price


comp = Compucter()
comp.get_price()

comp.set_price(1000)
comp.get_price()
