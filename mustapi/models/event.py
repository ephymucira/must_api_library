from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class Event:
    """
    Represents an event in the MustAPI system.
    
    Attributes:
        id (str): Unique identifier for the event
        title (str): Event title
        description (Optional[str]): Event description
        start_time (datetime): Event start time
        end_time (Optional[datetime]): Event end time
        location (Optional[str]): Event location
        created_at (datetime): Event creation timestamp
    """
    id: str
    title: str
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    created_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Event':
        """
        Create an Event instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing event data
        
        Returns:
            Event: Instantiated Event object
        """
        return cls(
            id=data.get('id', ''),
            title=data.get('title', ''),
            description=data.get('description'),
            start_time=datetime.fromisoformat(data['start_time']) if data.get('start_time') else None,
            end_time=datetime.fromisoformat(data['end_time']) if data.get('end_time') else None,
            location=data.get('location'),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        )