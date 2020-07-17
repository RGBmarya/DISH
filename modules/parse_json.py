import requests
import typing
from requests import Response
from typing import List, Union, Dict, Any

def extract_recipes(r: Response) -> List[Dict[str, Union[str, List[Any], int]]]:
    """Provided a response object, separate the individual elements of the json for display

    Arguments:
        r {Response} -- The Response object received from the API request

    Returns:
        Dict[str, Union[str, List[Any], int]] -- The elements stripped from the json body 
    """
    js = r.json()
    cookbook = []
    for group in js["hits"]:
        value = group["recipe"]
        cookbook.append(value)
    return cookbook

def display_recipes(recipe: Dict[str, Union[str, List[Any], int]]) -> None:
    """Print the necessary elements from the parsed json request to the user

    Arguments:
        recipe {Dict[str, Union[str, List[Any], int]]} -- The parsed json from the API request
    """
    label = recipe["label"]
    image = recipe["image"]
    ingredients = recipe["ingredientLines"]
    calories = int(recipe["calories"])
    time = recipe["totalTime"]
    if time == 0.0:
         print(f'\nLabel: {label}\nImage: {image}\nIngredients: \
             {ingredients}\nCalories: {calories}')
    else:
         print(f'\nLabel: {label}\nImage: {image}\nIngredients: \
             {ingredients}\nCalories: {calories}\nTotal Time: \
             {time}')