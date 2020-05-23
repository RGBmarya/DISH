import requests
import typing
from typing import Dict, List

def build_query(**kwargs) -> Dict[str, str]:
    """Creates the dictionary of parameters needed to query the Edamam API"""
    params={}
    for name, value in kwargs.items():
        if name=="from" and type(value) is int and value >= 0:
            params[name]=value
        elif name=="to" and type(value) is int and value >= 0:
            params[name]=value
        elif name=="ingr":
            pass
        elif name=="diet":
            pass
    return params


def send_query(ingredients: List[str], *args) -> str:
    """Sends an API request to the Edamam API"""
    pass
