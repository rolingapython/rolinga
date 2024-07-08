from domain.entities import Event

class DeleteEventUseCase:
    def __init__(self, event_service: EventService):
        self.event_service = event_service

    def execute(self, name: str, location: str, description: str, image: str):
        return self.event_service.create_event(name, location, description, image)