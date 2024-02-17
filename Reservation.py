class Reservation:
    ''' This class about reservation '''
    def __init__(self,name,address,credit_card,vin):
        self.__name = name 
        self.__address = address
        self.__credit_card = credit_card
        self.__vin = vin 
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,address):
        self.__address = address
    
    @property
    def credit_card(self):
        return self.__credit_card
    
    @credit_card.setter
    def credit_card(self,credit_card):
        self.__credit_card = credit_card
    
    @property
    def vin(self):
        return self.__vin
    
    @vin.setter
    def vin(self,vin):
        self.__vin = vin
    
