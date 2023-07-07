class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,flying_from,flying_to,date_of_journey,time_of_journey) -> None:
        self.price =  price
        self.flying_from = flying_from
        self.flying_to = flying_to
        self.flying_date = date_of_journey
        self.flying_time = time_of_journey
        