from typing import Dict, Union
from requests import Response
import typing
import requests


def send_request(url: str, params: Dict[str, Union[str, int]]) -> Response:
    """Sends an API request to the Edamam API"""
    return requests.get(url, params=params)
