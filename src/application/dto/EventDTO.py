from dataclasses import dataclass

@dataclass
class EventDTO:
    id : int
    name: str
    location: str
    description: str
    image: str
    link: str