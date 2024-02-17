from Vehicle import Vehicle
class Van(Vehicle):
    ''' This  class is about Van Model'''

    def __init__(self,make_model, mpg, vin,num_passengers):
        super().__init__(make_model, mpg, vin)
        self.__num_passengers = num_passengers
       
    
    def get_desciption(self):
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__num_passengers} '
    
    def __str__(self) -> str:
        return super().get_desciption()+' '+ f', Number of Passenger : {self.__num_passengers} '
    