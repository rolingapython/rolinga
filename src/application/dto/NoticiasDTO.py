from dataclasses import dataclass

@dataclass
class NoticiasDTO:
    id: int    
    title: str
    image: str
    description: str
    link: str
    publisher:str