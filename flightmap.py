import csv
from typing import List

from airport import Airport
from flight import Flight

class FlightMap:
    list_airports: List[Airport] = []
    list_flights: List[Flight] = []
    
    def __init__(self) -> None:
        return None
    
    def import_airports(self, csv_file: str) -> None:
        '''
        Charge le contenu du fichier CSV passé en paramètre, sous forme d'une collection de Airport correctement initialisée.
        '''
        with open(csv_file, newline='') as csvfile:
            content = csv.reader(csvfile)
            
            for row in content:
                airport = Airport()
                
                airport.name = row[0]
                
                # Retirer les guillemets et les espaces au début et à la fin d'une chaîne
                airport.code = eval(row[1]).split()[0]
                
                # Ajouter l'objet Airport créé en amont dans la liste des aéroports.
                self.list_airports.append(airport)
                
        return None

    def airports(self) -> List[Airport]:
        '''
        Retourne la liste des aéroports.
        '''
        return self.list_airports
    
    def airport_find(self, airport_code: str) -> Airport:
        '''
        Retourne un objet de type Airport en fonction du code passé en paramètre. S'il n'existe pas, la méthode retourne None.
        '''
        
        # Filtre la liste des aéroports en fonction du code passé en paramètre.
        airports_filtered = list(filter(lambda airport: airport.code == airport_code, self.airports()))
        
        return airports_filtered[0] if len(airports_filtered) > 0 else None
    
    def import_flights(self, csv_file: str) -> None:
        '''
        Charge le contenu du fichier CSV passé en paramètre, sous forme d'une collection de Flight correctement initialisée.
        '''
        with open(csv_file, newline='') as csvfile:
            content = csv.reader(csvfile)
            
            for row in content:
                flight = Flight()
                
                flight.src_code = row[0]
                
                flight.dst_code = eval(row[1]).split()[0]
                
                flight.duration = row[2].split()[0]
                
                self.list_flights.append(flight)
                
            # Supprime les doublons
            self.list_flights = list(set(self.list_flights))
                
        return None
    
    def flights(self) -> List[Flight]:
        '''
        Retourne la liste complète des vols.
        '''
        return self.list_flights
    
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        '''
        Retourne True s'il existe un vol direct entre l'aéroport de départ et l'aéroport d'arrivé, sinon cela retourne False.
        '''
        
        exists_flight = [flight for flight in self.flights() if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code]
        
        return True if len(exists_flight) > 0 else False
    
    def flights_where(self, airport_code: str) -> List[Flight]:
        '''
        Retourne les vols directs vers l'aéroport dont le code est passé en paramètre.
        '''
        direct_flights = [flight for flight in self.flights() if flight.dst_code == airport_code]
        
        return direct_flights if len(direct_flights) > 0 else []
    