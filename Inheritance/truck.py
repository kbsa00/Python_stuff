from vehicle import Vehicle

class Truck:
     
    def __init__(self, VIN, weight, manufacturer, capacity):
        self.vin_number = VIN
        self.weight = weight
        self.capacity = capacity
        self.manufacturer = manufacturer
    

    def transportCapacity(self):
        return self.capacity
    
    
    def getManufacturer(self):
        return self.manufacturer

    def VehicleType(self):
        return 'TRUCK'

    