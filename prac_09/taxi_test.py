"""CP1404 Prac 09 Taxi Test"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(my_taxi)
print(my_taxi.current_fare_distance)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(my_taxi.current_fare_distance)
