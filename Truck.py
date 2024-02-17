from Vehicle import Vehicle

class Truck(Vehicle):
    ''' This  class is about Truck Model '''

    def __init__(self,make_model, mpg, vin,length,num_doors):
        super().__init__(make_model, mpg, vin)
        self.__length = length
        self.__num_doors = num_doors
    
    def get_desciption(self):
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__length} , Number of Doors : {self.__num_doors}'
    
    def __str__(self) -> str:
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__length} , Number of Doors : {self.__num_doors}'
    