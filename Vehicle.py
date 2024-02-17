class Vehicle:
    def __init__(self,make_model,mpg,vin):
        self.__mpg = mpg
        self.__vin = vin
        self.__make_model = make_model
        self.__reserved = False

    @property
    def vin(self):
        return self.__vin
    
    @vin.setter
    def vin(self,vin):
        self.__vin = vin
    
    @property
    def mpg(self):
        return self.__mpg
    
    @mpg.setter
    def mpg(self,mpg):
        self.__mpg = mpg
    
    def is_reserved(self):
        return self.__reserved 
    
    def set_reserved(self,reserve):
        self.is_reserved=reserve
    
    def get_desciption(self):
        return f'make_model : {self.__make_model} , VIN : {self.__vin}'
    
    def __str__(self) -> str:
        return f'make_model : {self.__make_model} , VIN : {self.__vin}'
    

  




