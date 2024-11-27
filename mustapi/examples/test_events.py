from mustapi.client.client import MustAPIClient

# Initialize the client
client = MustAPIClient(api_key='your_api_key')

# List events
events = client.events.list_events()
for event in events:
    print(event.title)