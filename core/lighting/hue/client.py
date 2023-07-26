from dataclasses import dataclass
import json
import logging
import os
import pprint
from typing import Dict, List, Optional

import requests
from dataclasses_json import DataClassJsonMixin

from core.exceptions import HueError
from core.lighting.hue.enums import ResourceType
from core.lighting.hue.objects.resource import Resource
from core.lighting.hue.objects.device import Device
from core.lighting.hue.objects.light import Light
from core.lighting.hue.objects.entertainment_configuration import EntertainmentConfiguration
from core.settings import APP_NAME, CACHE_DIRECTORY

_logger = logging.getLogger(__name__)


@dataclass
class HueApplicationCredential(DataClassJsonMixin):
    username: str
    clientkey: str


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
                self._hue_application_key = HueApplicationCredential.from_json(key_file.read().strip())
        else:
            self.request_application_key()

    
    @property
    def resource_endpoint(self) -> str:
        """Construct the resource endpoint for the Hue API to hit."""

        return f'https://{self.bridge_ip_address}/clip/{self.api_version}/resource'

    def _camel_to_snake(self, s: str) -> str:
        """Utility function to convert Python class names to snake_case url paths.

        Stolen from: https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/

        Args:
            s (str): String to convert from CamelCase to snake_case

        Returns:
            str: snake_case string
        """

        def cameltosnake(camel_string: str) -> str:
            # If the input string is empty, return an empty string
            if not camel_string:
                return ""
            # If the first character of the input string is uppercase,
            # add an underscore before it and make it lowercase
            elif camel_string[0].isupper():
                return f"_{camel_string[0].lower()}{cameltosnake(camel_string[1:])}"
            # If the first character of the input string is lowercase,
            # simply return it and call the function recursively on the remaining string
            else:
                return f"{camel_string[0]}{cameltosnake(camel_string[1:])}"

        if len(s) <= 1:
            return s.lower()
        # Changing the first character of the input string to lowercase
        # and calling the recursive function on the modified string
        return cameltosnake(s[0].lower()+s[1:])

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

            # The name depends on whether or not there is more then 1 error
            hue_errors = response_json.get('errors')
            if hue_errors:
                hue_error = hue_errors[0]
            else:
                hue_error = response_json.get('error')
            
            if hue_error:
                _logger.debug(pprint.PrettyPrinter().pformat(response_json))
                raise HueError(hue_error.get('description'), hue_error.get('type'))

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

        self._hue_application_key = HueApplicationCredential.from_json(json.dumps(parsed_response['success']))

        if cache:
            with open(self.__class__._HUE_APPLICATION_KEY, 'w') as key_file:
                key_file.write(self._hue_application_key.to_json())

    def get_resource(self, resource_name: str) -> dict:
        """ Construct and send an HTTP GET request for specified resource

        Args:
            resource_name (str): The name of the resource requested

        Returns:
            requests.Response: the HTTP response
        """

        endpoint = self.resource_endpoint + '/' + resource_name

        return self._parse_hue_api_response(
            requests.get(
                endpoint,
                headers={
                    'hue-application-key': self._hue_application_key.username
                },
                verify=False  # Frustratingly, my version of the Hue bridge does not support SSL
            ),
            True
        )
    
    def put_resource(self, resource_name: str, body: object) -> dict:
        """ Construct and send an HTTP PUT request for specified resource

        Args:
            resource_name (str): The name of the resource requested
            body (object): JSON-style object to send as the body of the PUT request

        Returns:
            requests.Response: the HTTP response
        """

        endpoint = self.resource_endpoint + '/' + resource_name
        
        return self._parse_hue_api_response(
            requests.put(
                endpoint,
                headers={
                    'hue-application-key': self._hue_application_key.username
                },
                data=body,
                verify=False  # Frustratingly, my version of the Hue bridge does not support SSL
            ),
            True
        )
    

    def list(self, resource_class: DataClassJsonMixin) -> List[object]:
        """Retrieves all resources of specified dataclass type. 
        
        Args:
            resource_class (DataClassJsonMixin): the Dataclass for the specified resource to retrieve.
        """

        response = self.get_resource(self._camel_to_snake(resource_class.__name__))

        resources = []
        try:
            for get_json in response['data']:
                resources.append(resource_class.from_json(json.dumps(get_json)))
        except KeyError as e:
            _logger.info('Unable to load response because of missing required fields. See debug log for details')
            _logger.debug(pprint.PrettyPrinter().pformat(response))
            raise e
        
        return resources
    
    def put_light(self, light: Light):
        """Takes data in Light dataclass and puts it to the bridge to update it.
        
        NOTE: https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_light__id__put
        """

        _logger.info(light.to_put())

        self.put_resource(f'light/{light.id}', light.to_put())

    def test(self):
        """ Tests connection to local Hue bridge. Raises Exceptions if a failure occurs."""

        lights: List[Light] = self.list(Light)
        light_index: Dict[str, Light] = {}  # Index Lights by their ID
        for light in lights:
            light_index[light.id] = light
        
        devices: List[Device] = self.list(Device)

        for device in devices:
            device_lights = device.get_resources_by_type(ResourceType.LIGHT)

            for idx, light_service in enumerate(device_lights):
                light = light_index.get(light_service.rid)

                _logger.info(f'{device.metadata.name} - light_service {idx} {light.id} on: {light.on.on}')

                if device.metadata.name == 'Desk Lamp':
                    light.on.on = True
                    self.put_light(light)
        
        configurations: List[EntertainmentConfiguration] = self.list(EntertainmentConfiguration)
        _logger.debug(configurations)
        for configuration in configurations:
            _logger.info(f'{configuration.metadata.name}')
            for service_location in configuration.locations.service_locations:
                light = light_index.get(service_location.service.rid)

                if light:
                    _logger.info(f'{configuration.metadata.name} configuration - light_service {idx} {light.id} on: {light.on.on}')