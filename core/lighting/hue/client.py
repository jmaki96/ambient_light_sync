from http import HTTPMethod
import requests
from typing import Optional


class HueClient:

    def __init__(self, bridge_ip_address: str, api_version: Optional[str] = 'v2'):
        """Constructor.

        Args:
            bridge_ip_address (str): The IP address of the Hue bridge we're trying to connect too
            api_version (Optional[str]): The version of the Hue API to use. Defaults to v2.
        """

        self.bridge_ip_address = bridge_ip_address
        self.api_version = api_version
    
    @property
    def resource_endpoint(self) -> str:
        """Construct the resource endpoint for the Hue API to hit."""

        return f'https://{self.bridge_ip_address}/clip/{self.api_version}/resource'

    
    def request_resource(self, http_method: HTTPMethod, resource_name: str) -> requests.Response:
        """ Construct and send an HTTP request for specified resource

        Args:
            http_method (HTTPMethod): What method to use for the request
            resource_name (str): The name of the resource requested

        Returns:
            requests.Response: the HTTP response
        """

        endpoint = self.resource_endpoint + '/' + resource_name

        # This feels awful hacky - think about alternatives
        if http_method == HTTPMethod.GET:
            return requests.get(endpoint)
            
    
    def test(self):
        """ Tests connection to local Hue bridge.
        
        Raises:
            ConnectionException: If the client is unable to connect to bridge.
        """
        
        try:
            response = self.request_resource(HTTPMethod.GET, 'device')
        except Exception as e:
            raise e
