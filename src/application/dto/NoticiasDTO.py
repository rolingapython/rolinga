from dataclasses import dataclass

@dataclass
class NoticiasDTO:
    title: str
    image: str
    description: str
    link: str
    publisher:str