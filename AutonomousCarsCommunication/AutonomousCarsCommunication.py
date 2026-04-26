import math #needed to calculate the distance to other cars

class AutonomousCarsCommunication(object):
    cars_list = [] 

    def __init__(self, manufacturer, model, carID):
        # Set the current car information (manufacturer, model, unique ID, speed, location, events)
        self.manufacturer = manufacturer
        self.model = model
        self.carID = carID
        self.speed = 0
        self.x = 0
        self.y = 0
        self.events = []

        self.cars_information = []

    # Set the current speed of the car
    def set_car_speed(self, speed):
        self.speed = speed

    # Set the current location (in coordinates X and Y)
    def set_car_location(self, x, y):
        self.x = x    
        self.y = y 
    
    # Encountered events in the last 100km
    def set_car_events(self, event):
        self.events.append(event)

    # Add the current car to the car lists
    def add_car(self):
        self.cars_list.append(self)

    # Groupe all the related information for a car and send information to another car
    def send_car_information(self):
        current_car_info = {
            "manufacturer" : self.manufacturer,
            "model" : self.model,
            "carID" : self.carID,
            "speed" : self.speed,
            "location_x": self.x,
            "location_y": self.y,
            "events": self.events
        }

        for car in self.cars_list:
            if car.carID != self.carID:
                car.receive_car_information(current_car_info)

    # Receive information from other cars
    def receive_car_information(self, information):
        self.cars_information.append(information)

    # Calculate the distance  to another car using the Euclidean distance formula
    def calculate_distance(self, other_car):
        return math.sqrt((other_car.x - self.x)**2 + (other_car.y - self.y)**2)

    # Pick the closest car
    def pick_closest_car(self):
        closest_car = None
        min_dist = float('inf') # very big value

        for car in self.cars_list:
            if car.carID == self.carID:
                continue
            
            dist = self.calculate_distance(car)
            if dist < min_dist:
                min_dist = dist
                closest_car = car
        
        return closest_car


car1 = AutonomousCarsCommunication("Audi", "Q5", 76767)
car2 = AutonomousCarsCommunication("Hyunday", "Kona", 75777)
car3 = AutonomousCarsCommunication("Opel", "Astra", 75888)

car1.set_car_speed(100)
car1.x = 100
car1.y = 100
car1.add_car()
car1.send_car_information()

car2.set_car_speed(180)
car2.x = 500
car2.y = 500
car2.add_car()
car2.send_car_information()

car3.set_car_speed(120)
car3.x = 200
car3.y = 200
car3.add_car()
car3.send_car_information()

closest_car_from_car1 = car1.pick_closest_car()
if closest_car_from_car1:
    print(f"The closest car to {car1.manufacturer} is the {closest_car_from_car1.manufacturer} {closest_car_from_car1.model}.The {closest_car_from_car1.manufacturer} {closest_car_from_car1.model} has {closest_car_from_car1.speed} kilometers per hour.")

closest_car_from_car2 = car2.pick_closest_car()
if closest_car_from_car2:
    print(f"The closest car to {car2.manufacturer} is the {closest_car_from_car2.manufacturer} {closest_car_from_car2.model}.The {closest_car_from_car2.manufacturer} {closest_car_from_car2.model} has {closest_car_from_car2.speed} kilometers per hour.")









