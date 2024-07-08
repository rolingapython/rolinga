# src/application/use_cases/create_event_use_case.py
from domain.entities import Event
from application.dto.EventDTO import EventDTO
from src.domain.interfaces.EventService import EventService

class CreateEventUseCase:
    def __init__(self, event_service: EventService):
        self.event_service = event_service

    def execute(self, dto: EventDTO):
        return self.event_service.create_event(dto.name, dto.location, dto.description, dto.image)
