from mustapi.client.client import MustAPIClient
from datetime import datetime, timedelta
from typing import Optional

class EventDemoOperations:
    def __init__(self, api_key: str):
        """
        Initialize the MustAPI client for event demonstrations
        
        Args:
            api_key (str): API authentication key
        """
        self.client = MustAPIClient(api_key=api_key)
    
    # def list_events_example(self, limit: int = 10) -> None:
    #     """
    #     Demonstrate listing events with optional limit
        
    #     Args:
    #         limit (int, optional): Maximum number of events to retrieve. Defaults to 10.
    #     """
    #     print("\n--- Listing Events ---")
    #     try:
    #         events = self.client.events.list_events(limit=limit)
            
    #         if  events:
    #             print("No events found.")
    #             return
            
    #         print(f"Retrieved {len(events)} events:")
    #         for event in events:
    #             print(f"Event ID: {event.id}")
    #             print(f"Title: {event.title}")
    #             print(f"Description: {event.description or 'No description'}")
    #             print("---")
        
    #     except Exception as e:
    #         print(f"Error listing events: {str(e)}")


    def list_events_example(self) -> None:
        """
        Demonstrate listing events with optional limit
        
        Args:
            limit (int, optional): Maximum number of events to retrieve. Defaults to 10.
        """
        print("\n--- Listing Events ---")
        try:
            events = self.client.events.list_events()
            
            if not  events:
                print("No events found.")
                return
            
            print(f"Retrieved {len(events)} events:")
            for event in events:
                print(f"Event ID: {event.id}")
                print(f"Title: {event.title}")
                print(f"Description: {event.description or 'No description'}")
                print("---")
        
        except Exception as e:
            print(f"Error listing events: {str(e)}")
    
    def create_event_example(self, title: Optional[str] = None) -> str:
        """
        Demonstrate creating a new event
        
        Args:
            title (str, optional): Custom event title. Defaults to None.
        
        Returns:
            str: ID of the created event
        """
        print("\n--- Creating a New Event ---")
        
        # Generate event details
        default_title = title or "Tech Innovation Summit"
        event_data = {
            'title': default_title,
            'description': 'Annual technology and innovation conference',
            'start_time': (datetime.now() + timedelta(days=30)).isoformat(),
            'end_time': (datetime.now() + timedelta(days=31)).isoformat(),
            'location': 'San Francisco Convention Center'
        }
        
        try:
            new_event = self.client.events.create_event(event_data)
            
            print(f"Event Created Successfully!")
            print(f"Event ID: {new_event.id}")
            print(f"Title: {new_event.title}")
            print(f"Location: {new_event.location}")
            
            return new_event.id
        
        except Exception as e:
            print(f"Error creating event: {e}")
            return ""
    
    def get_event_example(self, event_id: Optional[str] = None) -> None:
        """
        Demonstrate retrieving a specific event
        
        Args:
            event_id (str, optional): ID of the event to retrieve. 
                                      If None, creates a new event first.
        """
        print("\n--- Retrieving a Specific Event ---")
        
        try:
            # If no event_id provided, create a new event
            # if not event_id:
            #     event_id = self.create_event_example()
            
            if not event_id:
                print("Could not retrieve event: No event ID available")
                return
            
            retrieved_event = self.client.events.get_event(event_id)
            
            print(f"Event Retrieved Successfully!")
            print(f"ID: {retrieved_event.id}")
            print(f"Title: {retrieved_event.title}")
            print(f"Description: {retrieved_event.description or 'No description'}")
            print(f"Start Time: {retrieved_event.date or 'Not specified'}")
            print(f"Location: {retrieved_event.location or 'No location specified'}")
        
        except Exception as e:
            print(f"Error retrieving event: {e}")
    
    def update_event_example(self, event_id: Optional[str] = None) -> None:
        """
        Demonstrate updating an existing event
        
        Args:
            event_id (str, optional): ID of the event to update. 
                                      If None, creates a new event first.
        """
        print("\n--- Updating an Event ---")
        
        try:
            # If no event_id provided, create a new event
            if not event_id:
                event_id = self.create_event_example()
            
            if not event_id:
                print("Could not update event: No event ID available")
                return
            
            update_data = {
                'title': 'Updated Tech Innovation Summit',
                'description': 'Expanded technology and innovation conference with more workshops',
                'location': 'San Jose Convention Center'
            }
            
            updated_event = self.client.events.update_event(event_id, update_data)
            
            print(f"Event Updated Successfully!")
            print(f"ID: {updated_event.id}")
            print(f"New Title: {updated_event.title}")
            print(f"New Description: {updated_event.description}")
            print(f"New Location: {updated_event.location}")
        
        except Exception as e:
            print(f"Error updating event: {e}")
    
    def delete_event_example(self, event_id: Optional[str] = None) -> None:
        """
        Demonstrate deleting an event
        
        Args:
            event_id (str, optional): ID of the event to delete. 
                                      If None, creates a new event first.
        """
        print("\n--- Deleting an Event ---")
        
        try:
            # If no event_id provided, create a new event
            if not event_id:
                event_id = self.create_event_example()
            
            if not event_id:
                print("Could not delete event: No event ID available")
                return
            
            delete_response = self.client.events.delete_event(event_id)
            
            print(f"Event Deletion Response: {delete_response}")
            print("Event deleted successfully!")
        
        except Exception as e:
            print(f"Error deleting event: {e}")
    
    def filtered_events_example(self, 
                                start_date: Optional[datetime] = None, 
                                category: Optional[str] = None) -> None:
        """
        Demonstrate listing events with advanced filtering
        
        Args:
            start_date (datetime, optional): Filter events starting after this date
            category (str, optional): Filter events by category
        """
        print("\n--- Listing Events with Advanced Filters ---")
        
        try:
            # Prepare filters
            filters = {}
            if start_date:
                filters['start_date_after'] = start_date.isoformat()
            if category:
                filters['category'] = category
            
            # Retrieve filtered events
            filtered_events = self.client.events.list_events(
                limit=5, 
                offset=0, 
                filters=filters
            )
            
            if not filtered_events:
                print("No events found matching the filters.")
                return
            
            print(f"Found {len(filtered_events)} events matching filters:")
            for event in filtered_events:
                print(f"Event ID: {event.id}")
                print(f"Title: {event.title}")
                print(f"Start Time: {event.start_time or 'Not specified'}")
                print("---")
        
        except Exception as e:
            print(f"Error retrieving filtered events: {e}")

def main():
    # Replace with your actual API key
    # API_KEY = 'your_api_key_here'
    API_KEY = ''
    
    # Initialize event operations
    event_ops = EventDemoOperations(api_key=API_KEY)
    
    # Demonstrate various event operations
    print("🚀 MustAPI Event Operations Demonstration 🚀")
    
    # List base example
    # event_ops.list_events_example()
    
    # # Create an event
    # created_event_id = event_ops.create_event_example()
    
    # Retrieve the created event
    event_ops.get_event_example("1")  #this is working well
    
    # # Update the event
    # event_ops.update_event_example(created_event_id)
    
    # # Advanced filtering example
    # event_ops.filtered_events_example(
    #     start_date=datetime.now(), 
    #     category='technology'
    # )
    
    # # Delete the event
    # event_ops.delete_event_example(created_event_id)

if __name__ == '__main__':
    main()