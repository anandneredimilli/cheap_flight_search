import requests

class DataManager:
    
    #This class contains from,to and other parameters
    

        
    def get_journey_details(self):
        api_key = {"apikey":"xm44mZXeSlwUrwhpzedbqraXXRCzQ22z"}
        FLY_FROM = input('from: ')
        FLY_TO = input("to: ")
        journey_dict= {
        'from':FLY_FROM,
        'to':FLY_TO,
        'from_iata':None,
        'to_iata':None
        }
    
        for i in range(2):
        
            if i==0:
                city_name = {'term':FLY_FROM}
                journey_dict['from_iata']=requests.get(url="https://api.tequila.kiwi.com/locations/query", headers=api_key,params=city_name).json()["locations"][0]['code']
            else:
                city_name = {'term':FLY_TO}
                journey_dict['to_iata']=requests.get(url="https://api.tequila.kiwi.com/locations/query", headers=api_key,params=city_name).json()["locations"][0]['code']
          
    
        return journey_dict
    