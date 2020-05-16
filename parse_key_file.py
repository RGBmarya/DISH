import typing
from typing import Tuple


def extract_auth_keys(path: str) -> Tuple[str,str]:
    """Retrieve developer keys from the specified file"""
    with open (path) as file:
        text=file.readlines()        
        app_id=text[0].split(":")[1].strip()
        app_key=text[1].split(":")[1].strip()
        return(app_id,app_key)
