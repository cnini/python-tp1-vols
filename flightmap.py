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
            self.list_flights = set(self.list_flights)
                
        return None
    
    def flights(self) -> List[Flight]:
        '''
        Retourne la liste complète des vols.
        '''
        return self.list_flights
    