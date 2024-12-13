"""CP1404 Prac 09 Silver Service Taxi Test"""

from silver_service_taxi import SilverServiceTaxi
TEST_1_DISTANCE = 18
Test_1_FARE = 48.80

TEST_2_DISTANCE = 50
Test_2_FARE = 127.50


my_silver_service_taxi = SilverServiceTaxi("Fancy Car", 100, 2)
my_silver_service_taxi.drive(TEST_1_DISTANCE)
print(f"${my_silver_service_taxi.get_fare():.2f}")
assert my_silver_service_taxi.current_fare_distance == TEST_1_DISTANCE
assert my_silver_service_taxi.get_fare() == Test_1_FARE
print(my_silver_service_taxi)

my_silver_service_taxi.start_fare()

my_silver_service_taxi.drive(TEST_2_DISTANCE)
print(f"${my_silver_service_taxi.get_fare():.2f}")
assert my_silver_service_taxi.current_fare_distance == TEST_2_DISTANCE
assert my_silver_service_taxi.get_fare() == Test_2_FARE
print(my_silver_service_taxi)
