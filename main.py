
# Total Time Complexity Worst Case = O(n^2) with 'n' as the number of packages. This is due to the nested loops in the
# add_packages_to_trucks() and deliver_packages() methods. This was the lowest complexity I could achieve without
# importing external libraries for additional functionality.
# The Total Time Complexity Best Case = O(n) if all packages are sorted already and everything is easily assigned.
# The Total Time Complexity Average Case = O(n^2)

import csv
import datetime
from Package_Class import Package
from Truck_Class import Truck
from Hash_Table_Class import HashTable

# Parsing data from the address csv file into a list of address information.
with open("CSV_Data_Files/addresses_csv") as address_csv:
    address_info = csv.reader(address_csv)
    address_info = list(address_info)

# Function to retrieve address info from the csv by matching the package address.
# Time Complexity = O(n)
def get_address_info(package_address):
    for line in address_info:
        if package_address in line[2]:
            return int(line[0])

#  Parsing data from the distance csv file containing the distances between addresses.
with open("CSV_Data_Files/distances_csv") as distances_csv:
    distance_info = csv.reader(distances_csv)
    distance_info = list(distance_info)

# Function to determine the distance between two addresses.
def get_distances_info(addr, dist):
    addr_id = get_address_info(addr)
    dist_id = get_address_info(dist)

    distance_miles = distance_info[addr_id][dist_id]
    if distance_miles == '': # If the distance is empty.
        distance_miles = distance_info[dist_id][addr_id]

    return float(distance_miles)

# Function to add packages to the hash table using the packages csv data.
def add_packages(pkg_hash_table):
    with open("CSV_Data_Files/packages_csv") as package_csv:
        packages_info = csv.reader(package_csv)

        # Looping through each package and adding to the hash table.
        # Time Complexity = O(n) (n = number of packages)
        for package_row in packages_info:
            package_id = int(package_row[0])
            package_address = package_row[1]
            package_city = package_row[2]
            package_state = package_row[3]
            package_zip = package_row[4]
            package_deadline = package_row[5]
            package_weight = package_row[6]
            package_notes = package_row[7]
            package_status = "At The WGUPS Hub"
            package_departure_time = ""
            package_arrival_time = ""

            package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline,
                              package_weight, package_notes, package_status, package_departure_time, package_arrival_time)

            pkg_hash_table.table_insert(package_id, package) # Time Complexity = O(1)

# Initialize the hash table and add packages.
package_hash_table = HashTable()
add_packages(package_hash_table)

# Function to add packages to trucks based on the package notes.
def add_packages_to_trucks():
    truck1_pkg_list = []
    truck2_pkg_list = []
    truck3_pkg_list = []
    # Retrieving packages
    packages = [package_hash_table.table_search(package_id) for package_id in range(1, 41)]
    low_priority_packages = []

    # Sorting the packages based on the specifications.
    # Time Complexity = O(n) (n = number of packages)
    for package_tmp in packages:

        if package_tmp.pkg_notes == 'TRUCK2_DELAYED':  # Truck 2 will handle all packages delayed until 9:05
            truck2_pkg_list.append(package_tmp)
        elif package_tmp.pkg_notes == 'TRUCK3_DELAYED':  # Truck 3 will handle all packages delayed until 10:20
            truck3_pkg_list.append(package_tmp)
        elif package_tmp.pkg_notes == 'PART_OF_GROUP':  # Any packages that are part of a group are delivered together
            truck1_pkg_list.append(package_tmp)
        elif package_tmp.pkg_deadline != 'EARLY_DEADLINE':  # All packages with an early deadline go to Truck 1
            truck1_pkg_list.append(package_tmp)
        elif package_tmp.pkg_notes == 'TRUCK2_ONLY':  # Packages required to shp via Truck 2
            truck2_pkg_list.append(package_tmp)
        else:
            low_priority_packages.append(package_tmp)

    # Adding standard (low) priority packages to Truck 1 based on the distance.
    # Time Complexity = O(n^2) (due to nested loops)
    for package_tmp in low_priority_packages:
        for pkgs_assigned_to_truck in truck1_pkg_list: # Time Complexity = O(n)
            if get_distances_info(pkgs_assigned_to_truck.pkg_address, package_tmp.pkg_address) < 2.0 and len(
                    truck1_pkg_list) < 16: # Time Complexity = O(1)
                truck1_pkg_list.append(package_tmp)
                low_priority_packages.remove(package_tmp) # Time Complexity = O(n)
                break

    # Adding standard (low) priority packages to Truck 2 based on the distance.
    # Time Complexity = O(n^2) (due to nested loops)
    for package_tmp in low_priority_packages:
        for pkgs_assigned_to_truck in truck2_pkg_list: # Time Complexity = O(n)
            if get_distances_info(pkgs_assigned_to_truck.pkg_address, package_tmp.pkg_address) < 2.0 and len(
                    truck2_pkg_list) < 16: # Time Complexity = O(1)
                truck2_pkg_list.append(package_tmp)
                low_priority_packages.remove(package_tmp) # Time Complexity = O(n)
                break

    # All remaining packages are added to Truck 3
    # Time Complexity = O(n)
    for package_tmp in low_priority_packages:
        truck3_pkg_list.append(package_tmp)

    return truck1_pkg_list, truck2_pkg_list, truck3_pkg_list


# Using the Nearest-Neighbor algorithm to load packages into trucks
# Time Complexity = O(N^2) due to the nested loop required to search for the nearest package.
def deliver_packages(truck):
    tmp_pkg_queue = []

    # Initializing the package queue.
    # Time Complexity = O(n) (n = number of packages)
    for package in truck.packages:
        tmp_pkg_queue.append(package)

    truck.packages.clear() # Time Complexity = O(1)

    # Nearest-Neighbor algorithm.
    # Time Complexity = O(n^2) (n = number of packages)
    while len(tmp_pkg_queue) > 0: # Time Complexity = O(n)
        nearest_address = 999
        nearest_package = None

        for package in tmp_pkg_queue: # Time Complexity = O(n) (n = number of packages)

            package_distance = get_distances_info(truck.current_address, package.pkg_address) # Time Complexity = O(n) (n = number of packages)

            if package_distance <= nearest_address: # Time Complexity = O(1)
                nearest_address = package_distance
                nearest_package = package

        truck.packages.append(nearest_package.pkg_id) # Time Complexity = O(1)
        tmp_pkg_queue.remove(nearest_package) # Time Complexity = O(n) (n = number of packages)

        nearest_package.depart = truck.last_departure

        truck.current_address = nearest_package.pkg_address
        truck.total_distance += nearest_address # Time Complexity = O(1)

        truck.last_departure += datetime.timedelta(hours=nearest_address / 18) # Time Complexity = O(1)
        nearest_package.arrive = truck.last_departure


def user_interface():
    print()
    print('WGUPS PARCEL TRACKING SERVICE')
    print('=' * 60)
    print('1. VIEW PACKAGE STATUSES FOR ALL TRUCKS')
    print('2. VIEW PACKAGE STATUS BY TIME')
    print('3. VIEW ALL PACKAGE STATUSES AT A SPECIFIC TIME')
    print('4. VIEW TOTAL MILEAGE FOR ALL TRUCKS')
    print('5. CLOSE PROGRAM')
    print('=' * 60)

# Printing package display header.
def pkg_disp_header():
    print('PACKAGE ID, ADDRESS, CITY, STATE, ZIP CODE, DEADLINE, WEIGHT, PACKAGE NOTES, STATUS, DEPARTURE TIME, ARRIVAL TIME')
    print('=' * 115)


# Function to find a package by the ID number and print the current status.
def package_search(package_id, current_time=datetime.timedelta(hours=17)):
    package = package_hash_table.table_search(package_id) # Time Complexity = O(1)
    if package is None: # Time Complexity = O(1)
        print(f"ERROR PACKAGE ID {package_id} INVALID.")
        return

        # For package #9, check the time and set the correct address
    if package.pkg_id == 9:
        # Time comparison: Package address is incorrect before 10:20
        time_threshold = datetime.timedelta(hours=10, minutes=20)
        if current_time < time_threshold:
            package.pkg_address = "300 State St"  # Incorrect address before 10:20
            package.pkg_zip = "84103"  # Incorrect ZIP code
        else:
            package.pkg_address = "410 S State St"  # Correct address after 10:20
            package.pkg_zip = "84111"  # Correct ZIP code

    package.set_pkg_status(current_time) # Time Complexity = O(1)
    print(str(package)) # Time Complexity = O(1)


class Main:
    # Initializing the trucks with a starting location and time.
    truck1 = Truck(1, [], 0, '4001 South 700 East', datetime.timedelta(hours=8))
    truck2 = Truck(2, [], 0, '4001 South 700 East', datetime.timedelta(hours=9, minutes=5))
    truck3 = Truck(3, [], 0, '4001 South 700 East', datetime.timedelta(hours=10, minutes=30))

    # Adding packages to each truck.
    truck1.packages, truck2.packages, truck3.packages = add_packages_to_trucks()

    # Calling method to deliver packages for each truck.
    deliver_packages(truck1)
    deliver_packages(truck2)
    deliver_packages(truck3)

    # Main loop for command line user interface.
    while True:
        user_interface()

        selection = input('SELECT OPTION 1-5: ')

        if selection == '1': # View all package statuses after deliveries have been completed.
            print()
            print('ALL PACKAGE STATUSES:  ')
            print('TRUCK 1: ' + str(truck1.total_distance) + ' TOTAL MILES. ')
            pkg_disp_header()

            # Display package statuses for Truck 1.
            for package_id in truck1.packages:
                package_search(package_id, datetime.timedelta(hours=17))

            print()
            print('TRUCK 2: ' + str(truck2.total_distance) + ' TOTAL MILES. ')
            pkg_disp_header()

            # Display package statuses for Truck 2.
            for package_id in truck2.packages:
                package_search(package_id, datetime.timedelta(hours=17))

            print()
            print('TRUCK 3: ' + str(truck3.total_distance) + ' TOTAL MILES. ')
            pkg_disp_header()

            # Display package statuses for Truck 3.
            for package_id in truck3.packages:
                package_search(package_id, datetime.timedelta(hours=17))

        elif selection == '2': # View the status of one package at a designated time.
            try:
                print()
                package_id = int(input('ENTER PACKAGE ID: '))
                package = package_hash_table.table_search(selection) # Time Complexity = O(1)
            except ValueError:
                print("INVALID PACKAGE ID.")
                continue

            # Retrieve and display package status for a given time.
            selection = input('ENTER TIME (HH:MM:SS) : ')
            try:
                (h, m, s) = selection.split(':') # Time Complexity = O(1)
                print()
                print(f'PACKAGE STATUS OF ID {package_id} AT ({h}:{m}:{s})')
                pkg_disp_header()
                package_search(package_id, datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))) # Time Complexity = O(1)
            except ValueError:
                print("INVALID TIME FORMAT.")

        elif selection == '3': # View the status for all packages at a designated time.
            try:
                print()
                selection = input('ENTER TIME (HH:MM:SS) : ')
                (h, m, s) = selection.split(':') # Time Complexity = O(1)
                print()
                print(f'DISPLAYING ALL PACKAGE STATUSES AT ({h}:{m}:{s})')
                print()
                print('TRUCK 1: ' + str(truck1.total_distance) + ' TOTAL MILES. ')
                pkg_disp_header()

                # Display all package statuses for Truck 1 at the specified time.
                for package_id in truck1.packages:
                    package_search(package_id, datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)))

                print()
                print('TRUCK 2: ' + str(truck2.total_distance) + ' TOTAL MILES. ')
                pkg_disp_header()

                # Display all package statuses for Truck 2 at the specified time.
                for package_id in truck2.packages:
                    package_search(package_id, datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)))

                print()
                print('TRUCK 3: ' + str(truck3.total_distance) + ' TOTAL MILES. ')
                pkg_disp_header()

                # Display all package statuses for Truck 3 at the specified time.
                for package_id in truck3.packages:
                    package_search(package_id, datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)))
            except ValueError:
                print("INVALID TIME FORMAT.")

        elif selection == '4': # View total mileage for all the trucks.
            miles_combined = truck1.total_distance + truck2.total_distance + truck3.total_distance
            print()
            print('TOTAL MILEAGE OF ALL TRUCK COMBINED: ' + str(miles_combined) + ' TOTAL MILES. ')


        elif selection == '5': # Quit program and end loop.
            print("EXITING PROGRAM...")
            exit()