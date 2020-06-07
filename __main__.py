import sys, getopt
import modules.parse_json as pj
import modules.parse_key_file as pk
import modules.send_request as sr
import modules.query_builder as qb
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
    id, key = pk.extract_auth_keys("key.txt")
    params = qb.build_query_params(to = 3, health = "alcohol-free", calories = "591-722")
    params["q"] = "chicken"
    params["app_id"] = id
    params["app_key"] = key
    r = sr.send_request(API_URL, params = params)
    cb = pj.extract_recipes(r)
    for dish in cb:
        pj.display_recipes(dish)    

if __name__ == '__main__':
    go(sys.argv[1:])