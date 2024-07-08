# src/ports/event_repository.py
from abc import ABC, abstractmethod
from domain.entities import Event

class EventRepository(ABC):
    @abstractmethod
    def generate_event_id(self) -> int:
        pass

    @abstractmethod
    def save(self, event: Event):
        pass

    @abstractmethod
    def get_by_id(self, event_id: int) -> Event:
        pass

    @abstractmethod
    def update(self, event: Event):
        pass

    @abstractmethod
    def delete(self, event_id: int):
        pass
