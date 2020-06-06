import sys, getopt
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
    pass

if __name__ == '__main__':
    go(sys.argv[1:])