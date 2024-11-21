from typing import List, Dict, Any, Optional
from ..models.event import Event

class EventService:
    """
    Service for handling event-related API operations.
    """
    def __init__(self, client):
        """
        Initialize the EventService with the main API client.
        
        Args:
            client: Main MustAPIClient instance
        """
        self._client = client
    
    def list_events(
        self, 
        limit: int = 100, 
        offset: int = 0, 
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Event]:
        """
        Retrieve a list of events.
        
        Args:
            limit (int, optional): Maximum number of events to return. Defaults to 100.
            offset (int, optional): Pagination offset. Defaults to 0.
            filters (dict, optional): Additional filters for event retrieval.
        
        Returns:
            List[Event]: List of event objects
        """
        params = {
            'limit': limit,
            'offset': offset,
            **(filters or {})
        }
        
        response = self._client.get('events', params=params)
        return [Event.from_dict(event_data) for event_data in response.get('events', [])]
    
    def get_event(self, event_id: str) -> Event:
        """
        Retrieve a specific event by its ID.
        
        Args:
            event_id (str): Unique identifier for the event
        
        Returns:
            Event: Event object
        """
        response = self._client.get(f'events/{event_id}')
        return Event.from_dict(response)
    
    def create_event(self, event_data: Dict[str, Any]) -> Event:
        """
        Create a new event.
        
        Args:
            event_data (dict): Event details for creation
        
        Returns:
            Event: Created event object
        """
        response = self._client.post('events', data=event_data)
        return Event.from_dict(response)
    
    def update_event(self, event_id: str, event_data: Dict[str, Any]) -> Event:
        """
        Update an existing event.
        
        Args:
            event_id (str): Unique identifier for the event
            event_data (dict): Updated event details
        
        Returns:
            Event: Updated event object
        """
        response = self._client.put(f'events/{event_id}', data=event_data)
        return Event.from_dict(response)
    
    def delete_event(self, event_id: str) -> Dict[str, Any]:
        """
        Delete an event.
        
        Args:
            event_id (str): Unique identifier for the event
        
        Returns:
            dict: Deletion confirmation response
        """
        return self._client.delete(f'events/{event_id}')