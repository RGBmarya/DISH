import requests
import typing
from typing import Dict, List


def build_query(**kwargs) -> Dict[str, str]:
    """Creates the dictionary of parameters needed to query the Edamam API"""
    params = {}
    for name, value in kwargs.items():
        if name == "from" and type(value) is int and value >= 0:
            params[name] = value
        elif name == "to" and type(value) is int and value >= 0:
            params[name] = value
        elif name == "ingr" and type(value) is int and value >= 0:
            params[name] = value
        elif name == "diet" and type(value) is str and value >= 0:
            params[name] = value
        elif name == "health" and type(value) is str and value >= 0:
            params[name] = value
        elif name == "cuisineType" and type(value) is str and value >= 0:
            params[name] = value
        elif name == "mealType" and type(value) is str and value >= 0:
            params[name] = value
        elif name == "dishType" and type(value) is str and value >= 0:
            params[name] = value
        elif name == "calories" and type(value) is range(minCal, maxCal) and value >= 0:
            params[name] = value
    #create minCal and maxCal variables if code is correct
        elif name == "time" and type(value) is range(minTime, maxTime) and value >= 0:
            params[name] = value
    #create minTime and maxTime variables if code is correct
        elif name == "excluded" and type(value) is str and value >= 0:
            pass
        elif name == "callback" and type(value) is str and value >=0:
            pass
    return params


def send_query(ingredients: List[str], *args) -> str:
    """Sends an API request to the Edamam API"""
    pass
