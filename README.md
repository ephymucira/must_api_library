# must_api_library

# MustAPI Python Client

## Overview
MustAPI is a Python library for interacting with the MustAPI backend services, providing a simple and intuitive way to manage events and resources.

## Installation
```bash
pip install mustapi
```

## Quick Start
```python
from mustapi import MustAPIClient

# Initialize the client
client = MustAPIClient(api_key='your_api_key')

# List events
events = client.events.list_events()
for event in events:
    print(event.title)

# Create an event
new_event = client.events.create_event({
    'title': 'My Event',
    'start_time': '2024-01-15T10:00:00Z'
})
```

## Features
- Easy event management
- Flexible API key authentication
- Robust error handling

## Requirements
- Python 3.8+
- requests library

## License
MIT License