class Car(object):
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels
        
    def get_CarMake(self):
        return self.make

mustang = Car('Ford', 'Mustang', 8)
print('The car make is {} and is model {} with {} wheels '.format( mustang.make,  mustang.model, mustang.wheels))
print(mustang.get_CarMake())