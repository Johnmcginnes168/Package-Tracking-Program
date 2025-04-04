# The package class contains the package attributes (id, address, city, etc.) for each package.
# Code below is for building the package class.
class Package:
    # Constructor to initialize the class attributes.
    # Time Complexity = O(1)
    def __init__(self, pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_notes, status, depart, arrive):
        self.pkg_id = pkg_id
        self.pkg_address = pkg_address
        self.pkg_city = pkg_city
        self.pkg_state = pkg_state
        self.pkg_zip = pkg_zip
        self.pkg_deadline = pkg_deadline
        self.pkg_weight = pkg_weight
        self.pkg_notes = pkg_notes
        self.status = status
        self.depart = depart
        self.arrive = arrive

    # Updates the package status based on the time, comparing the current time with the departure and arrival times.
    # Time Complexity = O(1)
    def set_pkg_status(self, current_time):
        if self.arrive < current_time:
            self.status = 'Delivered to Location'
        elif self.depart < current_time:
            self.status = 'En Route to Location'
        else:
            self.status = 'At the WGUPS Hub'

    # Function to create a string representing the combined package attributes.
    #Time Complexity = O(1)
    def __str__(self):
        return f'{self.pkg_id}, {self.pkg_address}, {self.pkg_city}, {self.pkg_state}, {self.pkg_zip}, {self.pkg_deadline}, {self.pkg_weight}, {self.pkg_notes}, {self.status}, {self.depart}, {self.arrive}'