class VehicleCost:
    def __init__(self,daily_rates,weekly_rates,weekend_rates,free_miles,per_miles_chrg,insur_rate) -> None:
        self.__daily_rates = daily_rates
        self.__weekly_rates = weekly_rates
        self.__weekend_rates = weekend_rates
        self.__free_miles = free_miles
        self.__per_miles_chrgs = per_miles_chrg
        self.__insur_rate = insur_rate

    @property
    def daily_rates(self):
        return  self.__daily_rates
    
    @property
    def weekly_rates(self):
        return self.__weekly_rates
    
    @property
    def weekend_rates(self):
        return self.__weekend_rates
    
    @property
    def free_daily_miles(self):
        return self.__free_miles
    
    @property
    def per_miles_chrgs(self):
        return self.__per_miles_chrgs
    
    @property
    def insur_rates(self):
        return self.__insur_rate
    

    def get_costs(self):
        return f'Daily Rates : {self.__daily_rates}, WeeklyRates :{self.__weekly_rates} , Weekend Rates : {self.__weekend_rates}, Free Miles : {self.__free_miles} , Per Mile charge : {self.__per_miles_chrgs} , Insurance Rate : {self.__insur_rate}'
    
    def __str__(self) -> str:
        return f'Daily Rates : {self.__daily_rates}, WeeklyRates :{self.__weekly_rates} , Weekend Rates : {self.__weekend_rates}, Free Miles : {self.__free_miles} , Per Mile charge : {self.__per_miles_chrgs} , Insurance Rate : {self.__insur_rate}'
    