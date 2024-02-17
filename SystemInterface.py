
class SystemInterface:
    def __init__(self,vehicles,vehicles_costs,reservations):
        self.__vehicles = vehicles
        self.__vehicles_costs = vehicles_costs
        self.__reservations = reservations
    
    def num_available_vehicles (self,vehicle_type):
        return self.__vehicles.num_avail_vehicles(vehicle_type)
    
    def get_vehicle(self,vin):
        for vehicle in self.__vehicles.vehicles:
            if vehicle.vin == vin:
                return vehicle.get_desciption()
        return None
    
    def get_vehicle_type(self):
        type = set()
        for vehicle in self.__vehicles.vehicles:
            type.add(vehicle.__class__.__name__)
        return type
    
    def get_vehicles_cost(self,vehicle_type):
        return self.__vehicles_costs.get_vehicle_cost(vehicle_type)
    
    def get_avail_vehicles(self,vehicle_type):
        return self.__vehicles.get_avail_vehicles(vehicle_type)
    
    def is_reserved(self,vin):
        return self.__reservations.is_reserved(vin)
    
    def find_reservations(self,credit_card):
        return self.__reservations.get_vin_reservation(credit_card)

    def add_reservations(self,reservation):
        self.__reservations.add_reservation(reservation)
    
    def cancel_reservation(self,credit_card):
        self.__reservations.cancel_reservation(credit_card)
    
    def cal_rental_cost(self,vehicle_type,rental_period,want_insurance,miles_driving):
        cost = self.__vehicles_costs.cal_rental_cost(vehicle_type,rental_period,want_insurance,miles_driving)
        if cost == None : print(f'kindly give correct vehicle type')
        else: print(f'The cost will be {cost}')
        