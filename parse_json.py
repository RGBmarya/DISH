import requests
import typing
from requests import Response
from typing import List, Union, Dict


def extract_recipes(r: Response) -> Dict[str, Union[str, List[Any], int]]:
    """Provided a response object, separate the individual elements of the json for display

    Arguments:
        r {Response} -- The Response object received from the API request

    Returns:
        Dict[str, Union[str, List[Any], int]] -- The elements stripped from the json body 
    """
    js = r.json()
    cookbook = []
    for key, value in js["hits"].items():
        if key == "recipe":
            cookbook.append(value)
    return cookbook


def display_recipes(recipe: Dict[str, Union[str, List[Any], int]]) -> None:
    """Print the necessary elements from the parsed json request to the user

    Arguments:
        recipe {Dict[str, Union[str, List[Any], int]]} -- The parsed json from the API request
    """
    print(recipe)
