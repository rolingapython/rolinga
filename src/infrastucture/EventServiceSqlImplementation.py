# src/domain/services/event_service.py
from domain.interfaces import EventService
from domain.entities import Event

class EventServiceImpl(EventService):
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def create_event(self, name: str, location: str, description: str, image: str) -> Event:
        event_id = self.event_repository.generate_event_id()
        event = Event(event_id, name, location, description, image)
        self.event_repository.save(event)
        return event
