import sys
import click
import os
import modules.parse_json as pj
import modules.parse_key_file as pk
import modules.send_request as sr
import modules.query_builder as qb
from dotenv import load_dotenv 

API_URL = "https://api.edamam.com/search"


@click.command()
@click.option('--ingredients', '-i',
              help='Ingredients you have available to create your dish')
@click.option('-f', help='Begin listing recipes at this index', default=-1)
@click.option('--to', '-t',
              help='Maximum number of recipes to display', default=-1)
@click.option('--diet', '-d', help='Diet label: choose from "balanced", \
             "high-protein", "low-fat", "low-carb"')
@click.option('--health', help='Health label: choose from "vegan", \
             "vegetarian", "sugar-conscious", "peanut-free", \
             "tree-nut-free", "fat-free", "alcohol-free"')
@click.option('--meal-type', '-m', help='The type of meal a recipe belongs \
              to: choose from "breakfast", "lunch", "dinner", "snack", \
              "teatime"')
def go(ingredients, f, to, diet, health, meal_type):
    """The main runner of the DISH program

    Args:
        args (List[str]): the list of arguments
                            passed from the command line
    """
    if ingredients is None:
        load_dotenv()
        ingredients = os.getenv("INGREDIENTS")

    id, key = pk.extract_auth_keys("key.txt")
    params = qb.build_query_params(
        f=f,
        to=to,
        diet=diet,
        health=health,
        mealType=meal_type
    )
    params["q"] = ingredients
    params["app_id"] = id
    params["app_key"] = key
    r = sr.send_request(API_URL, params=params)
    if r.status_code != 200:
        print("invalid request")
        print(r.content)
        sys.exit()
    cb = pj.extract_recipes(r)
    for dish in cb:
        pj.display_recipes(dish)


if __name__ == '__main__':
    go()
