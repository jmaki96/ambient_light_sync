from http import HTTPMethod
import json
import os
import requests
from typing import Optional

from core.exceptions import HueError
from core.settings import APP_NAME, CACHE_DIRECTORY


class HueClient:

    _HUE_APPLICATION_KEY = os.path.join(CACHE_DIRECTORY, 'hue_application.key')

    def __init__(self, bridge_ip_address: str, bridge_certificate_path: Optional[str] = None, api_version: Optional[str] = 'v2'):
        """Constructor.

        Args:
            bridge_ip_address (str): The IP address of the Hue bridge we're trying to connect too
            bride_certificate_path (Optional[str]): Many Hue bridges use self-signed certificates for SSL,
                so it may be necessary to provide the public key. If not provided, default certificates are used.
                Defaults to None.
            api_version (Optional[str]): The version of the Hue API to use. Defaults to v2.
        """

        self.bridge_ip_address = bridge_ip_address
        self.bridge_certificate_path = bridge_certificate_path
        self.api_version = api_version

        # Check to see if a keyfile exists, and load it if it does - otherwise, run through basic authorization
        # https://developers.meethue.com/develop/hue-api-v2/getting-started/

        if os.path.exists(self.__class__._HUE_APPLICATION_KEY):
            with open(self.__class__._HUE_APPLICATION_KEY, 'r') as key_file:
                self._hue_application_key = key_file.read().strip()
        else:
            self.request_application_key()

    
    @property
    def resource_endpoint(self) -> str:
        """Construct the resource endpoint for the Hue API to hit."""

        return f'https://{self.bridge_ip_address}/clip/{self.api_version}/resource'

    def _parse_hue_api_response(self, response: requests.Response, raise_errors: bool) -> dict:
        """Parses a Response from the Hue API.

        Args:
            response (requests.Response): Response from the Hua API Request
            raise_errors (bool, optional): If true, raises a HueException for any errors and then calls the raise_for_status() method.
        
        Returns:
            dict: JSON-style python dict from the Response.json() method
        """

        try:
            response_json = response.json()[0]  # Some endpoints wrap the actual response in an array of size 1, unclear why
        except KeyError:
            response_json = response.json()

        # Error handling
        if raise_errors:
            hue_error = response_json.get('error')
            if hue_error:
                raise HueError(hue_error['description'], hue_error['type'])

            response.raise_for_status()
        
        return response_json

    def request_application_key(self, cache: bool = True):
        """Requests an application key from the bridge, stores it on the client.
            Optionally, saves it in the app cache.

        NOTE: Hue Bridge requires a human to physically press a button on the bridge before the request is sent.
        
        Args:
            cache (bool): If True, saves request application key to cache. Defaults to True.
        """

        response = requests.post(
            f'https://{self.bridge_ip_address}/api',
            data=json.dumps({
                'devicetype': f'{APP_NAME}#HueClient',
                'generateclientkey': True
            }),
            verify=False  # Frustratingly, my version of the Hue bridge does not support SSL
        )
        
        parsed_response = self._parse_hue_api_response(response, True)

        # This method returns a username and a clientkey but puzzlingly, the client key is not required for authentication
        username = parsed_response['success']['username']

        self._hue_application_key = username
        if cache:
            with open(self.__class__._HUE_APPLICATION_KEY, 'w') as key_file:
                key_file.write(self._hue_application_key)

    def request_resource(self, http_method: HTTPMethod, resource_name: str) -> dict:
        """ Construct and send an HTTP request for specified resource

        Args:
            http_method (HTTPMethod): What method to use for the request
            resource_name (str): The name of the resource requested

        Returns:
            requests.Response: the HTTP response
        """

        endpoint = self.resource_endpoint + '/' + resource_name

        kwargs = {}

        if self.bridge_certificate_path:
            kwargs['verify'] = self.bridge_certificate_path

        # This feels awful hacky - think about alternatives
        if http_method == HTTPMethod.GET:
            return self._parse_hue_api_response(
                requests.get(
                    endpoint,
                    headers={
                        'hue-application-key': self._hue_application_key
                    },
                    verify=False  # Frustratingly, my version of the Hue bridge does not support SSL
                ),
                True
            )
            
    
    def test(self):
        """ Tests connection to local Hue bridge. Raises Exceptions if a failure occurs."""
        
        response = self.request_resource(HTTPMethod.GET, 'device')
