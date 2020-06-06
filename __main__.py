import sys, getopt
from DISH import parse_json, parse_key_file, query_builder, send_request
from typing import List

API_URL = "https://api.edamam.com/search"

SHORT_ARGS = 'i:f:t:d:h:'
LONG_ARGS = ['help', 'ingredients=', 'from=',
             'to=', 'diet=', 'health=', 'cuisine-type=',
             'meal-type=', 'dish-type=']


def go(args: List[str]):
    """The main runner of the DISH program

    Args:
        args (List[str]): the list of arguments 
                            passed from the command line
    """
    id, key = DISH.extract_auth_keys("key.txt")
    params = DISH.build_query(to = 3, health = "alcohol-free", calories = "591-722")
    params["q"] = "chicken"
    params["app_id"] = id
    params["app_key"] = key
    r = DISH.send_request(API_URL, params = params)
    cb = DISH.extract_recipes(r)
    for dish in cb:
        DISH.display_recipes(dish)    

if __name__ == '__main__':
    go(sys.argv[1:])