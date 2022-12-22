import csv
from typing import List
from airport import Airport

class FlightMap:
    list_airports: List[Airport] = []
    
    def __init__(self) -> None:
        return None
    
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, newline='') as csvfile:
            content = csv.reader(csvfile)
            
            for row in content:
                airport = Airport()
                airport.name = row[0]
                airport.code = eval(row[1]).split()[0]
                
                self.list_airports.append(airport)
                
        return None

    def airports(self) -> List[Airport]:
        return self.list_airports