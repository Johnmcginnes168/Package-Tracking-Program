# The Truck class is used to store attributes and data related to the three delivery trucks.

class Truck:
    # Constructor to initialize the attributes of the truck class.
    # Time Complexity = O(1)
    def __init__(self, truck_num, packages, total_distance, current_address, last_departure):
        self.truck_num = truck_num
        self.packages = packages
        self.total_distance = total_distance
        self.current_address = current_address
        self.last_departure = last_departure

    # Function to return a string representation of the Truck object.
    # Time Complexity = O(1)
    def __str__(self):
        return f'{self.truck_num}, {self.packages}, {self.total_distance}, {self.current_address}, {self.last_departure}'