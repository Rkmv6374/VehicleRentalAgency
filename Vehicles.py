

class Vehicles:
     ''' This class will manages all the vehicles for this agency '''

     def __init__(self):
          self.vehicles = []
        
     def add_vehicle(self,vehicle):
          self.vehicles.append(vehicle)
     
     def get_vehicle(self,vin):
          for vehicle in self.vehicles:
               if vin == vehicle.vin: return vehicle
          return None
     
     def num_avail_vehicles(self,vehicle_type):
          sum = 0
          for vehicle in self.vehicles:
               if vehicle.__class__.__name__==vehicle_type and not vehicle.is_reserved(): sum+=1
          return sum
     
     def get_avail_vehicles(self,vehicle_type):
          return [vehicle for vehicle in self.vehicles if vehicle.__class__.__name__ == vehicle_type and not vehicle.is_reserved()]
     

     def unreserve_vehicle(self,vin):
          vehicle = self.get_vehicle(vin)
          if vehicle != None:
               vehicle.set_reserved(False)
     
     
