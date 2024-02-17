class Reservations:
    ''' This class is about the reservation '''
    def __init__(self) -> None:
        self.reservations= []
    
    def add_reservation(self,resrvations):
        if self.is_reserved(resrvations.vin):
            return print(f'already reserved')
        else : 
            self.reservations.append(resrvations)
            return print(f'Reservation is successfull')
    
    def is_reserved(self,vin):    
        for vehicle in self.reservations:
            if vehicle.vin == vin : return True
        return False
    
    def get_vin_reservation(self,credit_card):
        return [reservation.vin for reservation in self.reservations if credit_card == reservation.credit_card]

    def cancel_reservation (self,credit_card):
        reservation  = [reservation for reservation in self.reservations if credit_card==reservation.credit_card]
        if len(reservation) == 0 : print(f'reservation is not done with this credit card')
        else :
            self.reservations.remove(reservation[0])
            print(f'reservatioin is cancelled')
    
    