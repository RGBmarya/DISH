import requests
import typing
from requests import Response
from typing import List, Union, Dict


def extract_recipies(r: Response) -> Dict[str, Union[str, List[Any], int]]:
    """Provided a response object, separate the individual elements of the json for display

    Arguments:
        r {Response} -- The Response object received from the API request

    Returns:
        Dict[str, Union[str, List[Any], int]] -- The elements stripped from the json body 
    """
    pass


def display_recipies(recipie: Dict[str, Union[str, List[Any], int]]) -> None:
    """Print the necessary elements from the parsed json request to the user

    Arguments:
        recipie {Dict[str, Union[str, List[Any], int]]} -- The parsed json from the API request
    """
    pass
