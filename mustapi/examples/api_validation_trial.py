import secrets
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import requests

class APIKeyManager:
    @staticmethod
    def validate_api_key(api_key: str, base_url: str) -> Dict[str, Any]:
        """
        Validate an API key by sending a request to an external API endpoint.
        Args:
            api_key_prefix (str): Prefix of the API key.
            base_url (str): Base URL of the external application (e.g., http://127.0.0.1:8000).
        Returns:
            dict: Validation result with key details or failure reason.
        """
        api_key_prefix = api_key[:8]
        # Construct the full URL
        url = f"{base_url}/devs/{api_key_prefix}"
        try:
            # Make a GET request to the external API
            response = requests.get(url, timeout=5)
            
            # Check for HTTP errors
            if response.status_code == 404:
                return {'valid': False, 'reason': 'API key not found'}
            elif response.status_code != 200:
                return {'valid': False, 'reason': f'Error from external service: {response.status_code}'}
            
            # Parse the response JSON
            data = response.json()
            
            
            # Validate the key details
            if not data.get('is_active', False):
                return {'valid': False, 'reason': 'API key is inactive'}
            if 'expires_at' in data and data['expires_at'] < datetime.utcnow().isoformat():
                return {'valid': False, 'reason': 'API key has expired'}
            
            # Return valid key details
            return {
                'valid': True,
                'details': data
            }
        except requests.exceptions.RequestException as e:
            return {'valid': False, 'reason': f'Failed to connect to external service: {str(e)}'}

# Test the API key and print the application name
result = APIKeyManager.validate_api_key('bT1ycZ1Uv23q6HKoSI1_xW-TiLSO_lUbSvWyOKiwJDk','http://127.0.0.1:8000')

if result['valid']:
    application_name = result['details'].get('application_name')
    print(f"Application Name: {application_name}.")
else:
    print(f"Validation failed: {result['reason']}")


#this is working mehn