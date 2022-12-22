class Airport:
    name: str
    code: str
    lat: float
    long: float
    
    def __init__(self) -> None:
        return None
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_code(self) -> str:
        return self.code
        
    def set_code(self, code: str) -> None:
        self.code = code
        
    def get_lat(self) -> float:
        return self.lat
        
    def set_lat(self, lat: float) -> None:
        self.lat = lat
        
    def get_long(self) -> float:
        return self.long
        
    def set_long(self, long: float) -> None:
        self.long = long
    