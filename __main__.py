import sys
import getopt
import click
import modules.parse_json as pj
import modules.parse_key_file as pk
import modules.send_request as sr
import modules.query_builder as qb
from typing import List

API_URL = "https://api.edamam.com/search"


@click.command()
@click.option('--ingredients', '-i', help='Ingredients you have available to create your dish', required = True)
@click.option('--from', 'f', help='Begin listing recipes at this index', default=-1)
@click.option('--to', 't', help='Maximum number of recipes to display', default=-1)
@click.option('--diet', 'd', help='Diet label: choose from “balanced”, “high-protein”, “high-fiber”, “low-fat”, “low-carb”, “low-sodium”')
@click.option('--health', '-h', help='Health label: choose from “vegan”, “vegetarian”, “paleo”, “dairy-free”, “gluten-free”, “wheat-free”, “fat-free”, “low-sugar”, “egg-free”, “peanut-free”, “tree-nut-free”, “soy-free”, “fish-free”, “shellfish-free”')
@click.option('--cuisine-type', '-c', help='Cuisine Type: choose from “American”, “Asian”, “British”, “Caribbean”, “Central Europe”, “Chinese”, “Eastern Europe”, “French”, “Indian”, “Japanese”, “Kosher”, “Mediterranean”, “Mexican”, “Middle Eastern”, “Nordic”, “South American”, “South East Asian”')
@click.option('--meal-type', '-m', help='The type of meal a recipe belongs to: choose from “breakfast”, “lunch”, “dinner”, snack”, “teatime”')
@click.option('--dish-type', '-d', help='The dish type a recipe belongs to: choose from “biscuits and cookies”, “bread”, “cereals”, “condiments and sauces”, “drinks”, “desserts”, “main course”, “pancake”, “preps”, “preserve”, “salad”, “sandwiches”, “side dish”, “soup”, “starter”, “sweets”,')
def go(args: List[str]):
    """The main runner of the DISH program

    Args:
        args (List[str]): the list of arguments 
                            passed from the command line
    """

    id, key = pk.extract_auth_keys("key.txt")
    params = qb.build_query_params(
        to=3, health="alcohol-free", calories="591-722")
    params["q"] = "chicken"
    params["app_id"] = id
    params["app_key"] = key
    r = sr.send_request(API_URL, params=params)
    cb = pj.extract_recipes(r)
    for dish in cb:
        pj.display_recipes(dish)


if __name__ == '__main__':
    go(sys.argv[1:])
