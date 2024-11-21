import requests
from typing import Dict, Any, Optional
from .exceptions import MustAPIError, AuthenticationError, ResourceNotFoundError
from .services.events import EventService
from .services.authentication_services import APIKeyManager

class MustAPIClient:
    """
    Main client for interacting with the MustAPI backend.
    
    Args:
        api_key (str): Your API authentication key
        base_url (str, optional): Base URL for the API. Defaults to 'https://api.mustapi.com/v1'
        timeout (int, optional): Request timeout. Defaults to 30 seconds
    """
    def __init__(
        self, 
        api_key: str, 
        base_url: str = 'https://api.mustapi.com/v1', 
        timeout: int = 30
    ):
        validation_result = APIKeyManager.validate_api_key(api_key)

        if not validation_result['valid']:
            raise AuthenticationError(
                f"API key Validation failed: {validation_result.get('reason','unknown error')}"

            )
        
        self.developer_id = validation_result.get('developer_id')
        self.application_name = validation_result.get('application_name')


        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout

        
        
        self._headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Developer-ID': self.developer_id,
            'X-Application-Name': self.application_name
        }
        
        
        # Initialize service modules
        self.events = EventService(self)
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict] = None, 
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Internal method to make HTTP requests.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (dict, optional): Request payload
            params (dict, optional): Query parameters
        
        Returns:
            dict: Parsed JSON response
        
        Raises:
            MustAPIError: For general API errors
            AuthenticationError: For authentication-related issues
            ResourceNotFoundError: When requested resource is not found
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self._headers,
                json=data,
                params=params,
                timeout=self.timeout
            )
            
            # Raise exceptions for specific HTTP status codes
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key or authentication failed")
            elif response.status_code == 404:
                raise ResourceNotFoundError(f"Endpoint {endpoint} not found")
            
            response.raise_for_status()
            return response.json() if response.content else {}
        
        except requests.exceptions.RequestException as e:
            raise MustAPIError(f"Request failed: {str(e)}")
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Convenience method for GET requests."""
        return self._request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        """Convenience method for POST requests."""
        return self._request('POST', endpoint, data=data)
    
    def put(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        """Convenience method for PUT requests."""
        return self._request('PUT', endpoint, data=data)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Convenience method for DELETE requests."""
        return self._request('DELETE', endpoint)