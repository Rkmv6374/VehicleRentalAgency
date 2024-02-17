class VehicleCosts:
    
    def __init__(self):
        self.vehicle_costs = {}
    
    def add_vehicle_cost(self,vehicle_type,vehicle_cost):
        self.vehicle_costs[vehicle_type.__name__] = vehicle_cost
    
    def get_vehicle_cost(self,vehicle_type):
        return self.vehicle_costs.get(vehicle_type)
    
    def cal_rental_cost(self,vehicle_type,rental_period,want_insurance,miles_driving):
        if vehicle_type not in self.vehicle_costs.keys(): return None
        vehicle_cost  = self.vehicle_costs[vehicle_type]
        if rental_period == 'daily': return vehicle_cost.daily_rates
        elif rental_period == 'weekly': return vehicle_cost.weekly_rates
        else:
            total_cost = vehicle_cost.weekend_rates
            if miles_driving > vehicle_cost.free_daily_miles:
                total_cost += (miles_driving-vehicle_cost.free_daily_miles)*vehicle_cost.per_miles_chrgs
            if want_insurance:
                total_cost += vehicle_cost.insur_rates
            return total_cost 
