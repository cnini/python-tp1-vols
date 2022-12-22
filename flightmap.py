import csv
from typing import List
from airport import Airport

class FlightMap:
    list_airports: List[Airport] = []
    
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
                airport.code = eval(row[1]).split()[0]
                
                self.list_airports.append(airport)
                
        return None

    def airports(self) -> List[Airport]:
        '''
        Retourne la liste des aéroports.
        '''
        return self.list_airports
    
    