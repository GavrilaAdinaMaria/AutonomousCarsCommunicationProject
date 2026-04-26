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


car1 = AutonomousCarsCommunication("Audi", "Q5", 76767)
car2 = AutonomousCarsCommunication("Hyunday", "Kona", 75777)

car1.set_car_speed(100)
car1.x = 100
car1.y = 100
car1.add_car()
car1.send_car_information()






