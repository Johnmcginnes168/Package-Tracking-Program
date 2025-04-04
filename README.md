
# WGUPS Package Delivery Tracking System

This Python program simulates a package delivery tracking system for a logistics company, "WGUPS." It manages the delivery of 40 packages across three trucks, using a nearest neighbor algorithm to optimize the route and minimize delivery time. The solution includes a hash table-based data structure to store and retrieve package data efficiently.

## Project Overview

The goal of this project was to implement a package delivery tracking system that considers various delivery constraints, including special instructions and address corrections. The system assigns packages to three trucks, optimizing the route for each truck based on the nearest neighbor algorithm, a greedy approach that selects the closest unvisited location at each step.

### Key Features:
- **Nearest Neighbor Algorithm**: A greedy approach used to determine the shortest delivery route for each truck.
- **Hash Table**: Utilized for fast searching, inserting, and updating package information with package IDs as unique keys.
- **Truck Assignment**: Packages are dynamically assigned to three trucks, considering special instructions and package priorities.

## Data Structures
The primary data structure used is a **hash table**, where each package’s unique ID acts as the key. The hash table allows for efficient O(1) access, insertion, and updates, ensuring smooth operations as the trucks make deliveries. The program also utilizes a **Package class** to store attributes like package ID, delivery address, weight, status, and timestamps.

## Algorithm Breakdown:
1. **Initialize**: Set starting location for the trucks.
2. **Route Calculation**: Using the Nearest Neighbor algorithm, find the shortest route for each truck by continuously selecting the nearest package location.
3. **Update**: For each package delivered, update the package’s departure and arrival times, and calculate the truck’s total distance traveled.
4. **Repeat**: Continue until all packages are delivered.

### Time & Space Complexity:
- **Time Complexity**: The worst-case time complexity for the delivery process is O(n²) due to the nested loops for route calculations. However, operations involving data access are efficient with O(1) time complexity.
- **Space Complexity**: O(n), where n is the number of packages, as the program stores the data in lists and a hash table.

## Development Environment
- **Python Version**: 3.13.1
- **IDE**: PyCharm Community Edition 2024
- **Hardware**: Lenovo Legion laptop with a 13th Gen Intel Core i9 processor, 16GB RAM, and a 2TB SSD.

## Scalability & Adaptability
The program is designed to efficiently handle larger datasets due to the use of hash tables, which dynamically resize. While the nearest neighbor algorithm is suitable for smaller datasets, alternative algorithms like Dijkstra’s could improve scalability for larger data sets, optimizing performance to O(n log n).

## Possible Enhancements
- Implementing alternative routing algorithms such as Dijkstra’s or A* for improved performance with larger datasets.
- Modularizing the code by breaking down logic into additional helper methods.
- Using external libraries such as NumPy or pandas for more efficient sorting and distance calculations.

## How to Run
1. Clone this repository to your local machine.
2. Install the necessary dependencies (if any).
3. Run the program using Python 3.13.1.


