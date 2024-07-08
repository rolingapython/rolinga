from dataclasses import dataclass

@dataclass
class EventDTO:
    name: str
    location: str
    description: str
    image: str
    link: str