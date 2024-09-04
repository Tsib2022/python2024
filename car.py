class car:
    def __init__(self,model,yop,capacity,price,mileage):
        self.model = model
        self.yop = yop
        self.capacity = capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4
    def discription(self):
        discription = (f'Автомобиль {self.model}, {self.yop} года выпуска, с объемом двигателя {self.capacity},стоимостью {self.price} руб., с пробегом {self.mileage} км.Количество колес - {self.wheels}')
        print(discription)
bmw = car(' BMW',2004,2200,2400000,210000)
bmw.discription()
class highCar(car):
    def __init__(self,model,yop,capacity,price,mileage):
        super().__init__(model,yop,capacity,price,mileage)
        self.wheels = 8
    def discription(self):
        discription = (f'Грузовик {self.model}, {self.yop} года выпуска, с объемом двигателя {self.capacity},стоимостью {self.price} руб., с пробегом {self.mileage} км.Количество колес - {self.wheels}')
        print(discription)
maz = highCar('MAZ', 1994,330,4500000,420000)
maz.discription()