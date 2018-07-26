from car import Car
from truck import Truck


a = Car('ABC1', 1000, 'BMW', 4)
b = Truck('BCD2', 1000, 'MAN', 10000)
c = Car('Def2', 1200, 'FORD', 4)
d = Truck('EFG4', 11000, 'MERCEDES', 15000)

for v in [a,b,c,d]:
    print(v.getManufacturer(), v.VehicleType())

print(a.getWeight(), b.getManufacturer(), c.NumberOfSeats(), d.transportCapacity())
