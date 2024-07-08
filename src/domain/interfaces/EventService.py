# src/ports/event_service.py
from abc import ABC, abstractmethod
from domain.entities import Event

class EventService(ABC):
    @abstractmethod
    def create_event(self, name: str, location: str, description: str, image: str) -> Event:
        pass
