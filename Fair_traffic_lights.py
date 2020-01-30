# Design an algorithm for fair traffic lights that prioritize lanes that have the most traffic in order to clear a traffic jam.
# The lanes that have the most traffic are the ones that have more cars travelling in total in either, but opposite, direction.
# The traffic lights either have green light for traffic travelling north/south or east/west.
 
# The traffic light let drivers pass in a batch of 5 cars travelling either direction (i.e., maximum of 10 cars going each opposite direction simultaneously).
# When there are an equal number of cars travelling north/south and east/west, then the north/south lane has priority to clear traffic from the capital center.
 
# Example:
# Number of cars travelling north: 10
# Number of cars travelling south: 10
# Number of cars travelling east: 5
# Number of cars travelling west: 10
 
# Green light on N/S
# Green light on E/W
# Green light on N/S
# Green light on E/W
# No cars waiting, the traffic jam has been solved!
# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.
 
north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))
