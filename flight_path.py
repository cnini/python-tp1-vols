from typing import List

from airport import Airport
from flight import Flight

class FlightNotMaching(Exception):
    "L'aéroport renseigné ne correspond pas à l'aéroport d'arrivé du vol."
    pass

class FlightPathBroken(Exception):
    "Deux vols consécutifs n'ont pas d'aéroport en commun."
    pass

class FlightPathDuplicate(Exception):
    "Le chemin contient deux fois le même aéroport."
    pass

class FlightPath:
    path: List[Airport] = []
    old_airports: List[Airport] = []
    new_airports: List[Airport] = []
    
    def __init__(self, src_airport: Airport) -> None:
        '''
        Initialiser le chemin avec l'aéroport de départ.
        '''
        self.path.append(src_airport)
        self.old_airports.append(src_airport.code)
        return None
    
    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        '''
        Ajouter un vol au chemin.
        '''
        if via_flight.src_code == self.path[-1].code and via_flight.src_code not in self.old_airports:
            if via_flight.dst_code == dst_airport.code:
                self.path.append(dst_airport)
                self.old_airports.append(dst_airport.code)
                self.new_airports.append(via_flight.dst_code)
            else:
                raise FlightNotMaching(Exception)
        else:
            raise FlightPathBroken(Exception)
    
    def flights(self) -> List[Flight]:
        '''
        Retourne la liste des vols, dans l'ordre du chemin.
        '''
        return []
        
    def airports(self) -> List[Airport]:
        '''
        Retourne le nombre d'étapes du chemin, c'est-à-dire le nombre de vols entre les aéroports.
        '''
        return len(self.path) - 1
    
    def steps(self) -> int:
        '''
        Longueur du chemin, égale au nombre de vols entre le premier et le dernier aéroport.
        '''
        return len(self.path)
    
    def duration(self) -> float:
        '''
        Durée totale du chemin
        '''
        duration = 0
        
        for flights in self.flights():
            duration += flights.duration
        
        return duration