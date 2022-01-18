class Car:
    def __init__(self, year, color, model):
        self.year = year
        self.color = color
        self. model = model
        return {self.year}, {self.color}, {self.model}

class Garage:
    def __init__(self):
        self.cars_added = []
        self.car_info = {}
        self.spots = 10
        self.bill = 0
    
    def spots_open(self):
        return self.spots
    
    def add_car(self, year, color, car):
        self.car = car
        self.tickets = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if self.spots >= 0:
            self.cars_added.append(str(car).split(' '))
            self.spots -= 1
            self.car_info = {'list':[], 'year': [], 'color': [], 'model':[]}
            for index, m in enumerate(self.cars_added):
                self.car_info['year'].append(self.tickets[index])
                self.car_info['color'].append(m[1])
                self.car_info['model'].append(m[2])
            return "Thank you, car successfully added to parking"
        else:
            print(f"We have {self.spots} spots open.")
            
    def remove_car(self):
        def __init__(self, my_list, bill_hours):
            self.bill_hours = bill_hours
            my_list = len(self.car_info['list'])
            if my_list not in self.car_info['list']:
                print("Sorry we could not find your car. Wanna check again?")
                pass
            for index, i in enumerate(self.car_info['list']):
                            if i == my_list:
                                print("Your car year is:", self.car_info['year'][index])
                                print("Your car color is:", self.car_info['color'][index])
                                print("Your car model is:", self.car_info['model'][index])
                                remove_car_index = self.car_info['list'].pop([i])
                                self.car_info['model'].pop([i])
                                self.spots += 1
                            if len(self.car_ifo['list']) < my_list:
                                while True:
                                    return"You have 15 minutes"

    def cars_in_garage(self):
        for m in self.car_info.items():
            print(m)
                                
                            
                                
my_parking_lot = Garage()
print(my_parking_lot.spots_open())
my_parking_lot.add_car('2015', 'black', 'pathfinder')