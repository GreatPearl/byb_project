

#To Calculate User's Total Holiday Cost
#User needs two return flights to destination, stay for 7 nights 
# and rent a car for 6 days
#Create variables for flight cost, number of nights 
# and number of rental days

flight_1 = int(input("Enter cost of first flight:"))
flight_2 = int(input("Enter cost of second flight:"))
cost_per_night = int(input("Enter cost per night of hotel:"))
rent_per_day = int(input("Enter cost of car rental per day:"))
flight_cost = flight_1 + flight_2
print("Total cost of flights:", flight_cost)
num_nights = int(input("Enter number of nights:"))
rental_days = int(input("Enter number of days car rental:"))

#Create the following function: hotel_cost, plane_cost, car_rental, and holiday_cost
def hotel_cost(num_nights, cost_per_night): #Create function to calculate hotel cost
    return num_nights * cost_per_night
hotel_cost = num_nights*cost_per_night
print("Total cost of hotel is:",hotel_cost)


def plane_cost(flight_1, flight_2): #Create function to calculate cost of flight
    return flight_1 + flight_2
plane_cost = flight_1 + flight_2
print("Total for flights is:",plane_cost)


def car_rental(rental_days, rent_per_day):  #create function to calculate cost of car rental
    return rental_days * rent_per_day
car_rental = rental_days*rent_per_day 
print("Total for car rental is:",car_rental)


def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental
holiday_cost = hotel_cost + plane_cost + car_rental

print("The total cost of this Holiday is:", holiday_cost)




# Enter cost of flight:80
# Enter cost of flight:150
# Enter cost per night of hotel:60
# Enter cost of car rental per day:40
# 230
# Enter number of nights:7
# Enter number of days car rental:7
# Total cost of hotel is: 420
# Total for flights is: 230
# Total for car rental is: 280
# The total cost of this Holliday is: 930





