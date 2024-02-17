from Vehicle import Vehicle


class Car(Vehicle):
    ''' This  class is about Car Model'''

    def __init__(self,make_model, mpg, vin,num_passengers,num_doors):
        super().__init__(make_model, mpg, vin)
        self.__num_passengers = num_passengers
        self.__num_doors = num_doors
    
    def get_desciption(self):
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__num_passengers} , Number of Doors : {self.__num_doors}'
    
    def __str__(self) -> str:
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__num_passengers} , Number of Doors : {self.__num_doors}'
    
