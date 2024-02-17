from Car import Car
from Truck import Truck
from Van import Van
from Vehicles import Vehicles
from VehicleCost import VehicleCost
from VehicleCosts import VehicleCosts
from SystemInterface import SystemInterface 
from Reservations import Reservations
from Reservation import Reservation
#self,make_model, mpg, vin,num_passengers,num_doors -> Car
#self,make_model, mpg, vin,length,num_doors -> Truck
#self,make_model, mpg, vin,num_passengers -> Van
# Creating instances of Car
car1 = Car("Toyota Camry", 30, "ABC123456789", 5, 4)
car2 = Car("Honda Accord", 28, "DEF987654321", 5, 4)
car3 = Car("Ford Mustang", 25, "GHI345678901", 4, 2)
car4 = Car("Chevrolet Malibu", 29, "JKL012345678", 5, 4)
car5 = Car("Nissan Altima", 27, "MNO567890123", 5, 4)
rental_cars = [car1,car2,car3,car3,car4,car5]

# Creating instances of Truck
truck1 = Truck("Ford F-150", 18, "PQR123456789", 6.5, 4)
truck2 = Truck("Chevrolet Silverado", 17, "STU987654321", 6.8, 4)
truck3 = Truck("Ram 1500", 16, "VWX345678901", 6.4, 4)
truck4 = Truck("Toyota Tundra", 15, "YZA012345678", 6.7, 4)
truck5 = Truck("Nissan Titan", 16, "BCD567890123", 6.6, 4)
rental_trucks = [truck1,truck2,truck3,truck4,truck5]

# Creating instances of Van
van1 = Van("Chrysler Pacifica", 22, "EFG123456789", 7)
van2 = Van("Toyota Sienna", 24, "HIJ987654321", 8)
van3 = Van("Honda Odyssey", 28, "KLM345678901", 7)
van4 = Van("Dodge Grand Caravan", 20, "NOP012345678", 7)
van5 = Van("Ford Transit", 18, "QRS567890123", 12)
rental_vans = [van1,van2,van3,van4,van5]

# add vehicles in agency
agency_vehicles = Vehicles()

def add_vehicles(vehicles_):
    for vehicle in vehicles_:
        agency_vehicles.add_vehicle(vehicle)

add_vehicles(rental_cars)
add_vehicles(rental_trucks)
add_vehicles(rental_vans)

# self,daily_rates,weekly_rates,weekend_rates,free_miles,per_miles_chrg,insur_rate
vehicle_cost1 = VehicleCost(50, 300, 80, 100, 0.25, 20)
vehicle_cost2 = VehicleCost(60, 350, 90, 120, 0.30, 25)
vehicle_cost3 = VehicleCost(115, 480, 100, 80, 0.10, 18)

agency_costs  = VehicleCosts()
agency_costs.add_vehicle_cost(Car,vehicle_cost1)
agency_costs.add_vehicle_cost(Van,vehicle_cost2)
agency_costs.add_vehicle_cost(Truck,vehicle_cost3)

agency_resrvations = Reservations()
# # user console 

interface = SystemInterface(agency_vehicles,agency_costs,agency_resrvations)

#3rd option function 
def option_3rd():
    vehicle_type = input('Enter the vehicle type ')
    reserved_vin = [reservation.vin for reservation in agency_resrvations.reservations]
    vehicle_avail = interface.get_avail_vehicles(vehicle_type)
    for vehicle in vehicle_avail:
        if vehicle.vin not in  reserved_vin: print(vehicle)
# 5th option function 
def option_5th ():
            name = input('Enter your name ')
            address = input('Enter you address ')
            credit_card = int(input('Enter your credit_card '))
            vin = input('Enter the vin number ')
            while True:
                flag = False
                for vehicle in agency_vehicles.vehicles:
                    if vehicle.vin == vin: 
                        flag = True; break
                if flag: break
                print(f'pls enter the valid vin')
                print(f'chooses among them { [vehicle.vin for vehicle in agency_vehicles.vehicles ]}')
                vin = input('Enter the vin number ')
            reservation = Reservation(name,address,credit_card,vin)
            agency_resrvations.add_reservation(reservation)

# 4rth option 
def option_4rth():
    # vehicle_type,rental_period,want_insurance,miles_driving
    print(f'These are available vehicle Types ')
    vehicle_type = interface.get_vehicle_type()
    for type in vehicle_type : print(type)
    vehicle_type = input(f'Choose the available type of vehicles ')
    rental_period  = input('Enter the rental period ')
    insurance = input('Do you want to take waranty insurance (y/n) ')
    want_insurance = False
    if insurance in ['Yes','yes','YES','y']: want_insurance = True
    miles_driving = int(input('Enter the miles driving '))
    interface.cal_rental_cost(vehicle_type,rental_period,want_insurance,miles_driving)
# # Console :


while True:
    print('''\n<<< MAIN MENU >>>\n
    1. Display Vehicle type
    2. Check Rental rates
    3. Check Available vehicles
    4. Get a cost of specific rental
    5. Make a reservation
    6. Cancel a reservation
    7. Quit\n''')
    
    try:
       choice  = int(input('Enter the choice : '))
    except Exception as e:
       print(e)
    else:
      if choice == 1: 
        vehicle_type = interface.get_vehicle_type()
        for type in vehicle_type : print(type)
      elif choice ==2:
        try:
           vehicle_type = input('Enter the vehicle type ')
           vehicle_cost = interface.get_vehicles_cost(vehicle_type)
           if vehicle_cost == None : print(f'\npls enter the available vehicle type ')
           else : print(vehicle_cost)
        except Exception as e:
            print(e)
      elif choice == 3:
        try:
            option_3rd()
        except Exception as e:
            print(e)
      elif choice == 4:
        try:
            option_4rth()
        except Exception as e:
            print(e)
      elif choice == 5:
        try:
            option_5th()
        except Exception as e:
            print(e)
      elif choice == 6:
        try:
            credit_card = int(input('Enter the credit card '))
            interface.cancel_reservation(credit_card)
        except Exception as e:
            print(e)
      else :
        quit = input('Do you want to exit (y/n) ')
        if quit in ['YES','yes','Y','y']: break






            


        


    