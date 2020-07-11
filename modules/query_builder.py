import requests
import typing
from typing import Dict, List


def build_query_params(**kwargs) -> Dict[str, str]:
    """Creates the dictionary of parameters needed to query the Edamam API"""
    params = {}
    for name, value in kwargs.items():
        if name == "from" and type(value) is int and value >= 0:
            params[name] = value
        elif name == "to" and type(value) is int and value >= 0:
            params[name] = value
        elif name == "diet" and type(value) is str and value != "":
            params[name] = value
        elif name == "health" and type(value) is str and value != "":
            params[name] = value
        elif name == "cuisineType" and type(value) is str and value != "":
            params[name] = value
        elif name == "mealType" and type(value) is str and value != "":
            params[name] = value
        elif name == "dishType" and type(value) is str and value != "":
            params[name] = value
        elif name == "calories" and type(value) is str and value !="" \
        and (len(value.split("-"))==2 and value.split("-")[0].isdigit() \
        and value.split("-")[1].isdigit() \
        and int(value.split("-")[0])<int(value.split("-")[1])):
            params[name] = value
        elif name == "time" and type(value) is str and value !="" \
        and (len(value.split("-"))==2 and value.split("-")[0].isdigit() \
        and value.split("-")[1].isdigit() \
        and int(value.split("-")[0])<int(value.split("-")[1])):
            params[name] = value
        elif name == "excluded" and type(value) is str and value != "":
            pass
        elif name == "callback" and type(value) is str and value != "":
            pass
    return params


