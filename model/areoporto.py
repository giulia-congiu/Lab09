from dataclasses import dataclass


@dataclass
class Areoporto:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float

    def __hash__(self):
        return hash(self.ID) #delego alla hash della chiave primaria

    # def __eq__(self, other):
    #     return self.ID == other.ID #saranno uguali se hanno stessa chiave primaria

    def __str__(self):
        #metodo che uso per stampare l'oggetto
        return f"{self.AIRPORT} ({self.IATA_CODE}) -- {self.CITY}"