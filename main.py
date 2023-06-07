class Car:

    def __init__(self, name: object, make: object, model: object) -> object:
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    def start(self):
        print("Engine is running")

car_a = Car(name='Toyota', make= 'Corolla' , model = '2015')
car_a.start()
print(car_a.name)
print(car_a.car_count)
