import requests
class FlightSearch:
    def __init__(self,FLY_FROM,FLY_TO,FROM_DATE,TO_DATE) -> None:
        self.journey_dict ={
        "fly_from" : FLY_FROM,
        "fly_to ": FLY_TO,
        "date_from ": FROM_DATE,
        "date_to ":TO_DATE,
        'curr':'INR'} 
    def search(self):
        api_key = {"apikey":"xm44mZXeSlwUrwhpzedbqraXXRCzQ22z"}
        data = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=api_key, params=self.journey_dict).json()
        print(data['data'][0]['cityFrom'])
        print(data['data'][0]['cityTo'])
        print(data['data'][0]['price'])
        print(data['data'][0]['route'][0]['cityFrom'])
        print(data['data'][0]['route'][0]['cityTo'])
        print((data['data'][0]['route'][0]['local_departure']).split("T"))
        print((data['data'][0]['route'][0]['local_arrival']).split("T"))        
    