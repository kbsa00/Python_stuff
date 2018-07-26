from vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self, VIN, weight, manufacturer, seats):
        self.vin_number = VIN
        self.weight = weight
        self.seats = seats
        self.manufacturer = manufacturer
    

    def NumberOfSeats(self):
        return self.seats


    def getManufacturer(self):
        return self.manufacturer  

    def VehicleType(self):
        return 'CAR'

    
        
