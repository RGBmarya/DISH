import typing
from requests import Session
from typing import Tuple


def extract_auth_keys(path: str) -> Tuple[str,str]:
    """Retrieves developer keys from the specified file"""
    with open (path) as file:
        text=file.readlines()        
        app_id=text[0].split(":")[1].strip()
        app_key=text[1].split(":")[1].strip()
        return(app_id,app_key)


def create_session(keys: Tuple[str, str]) -> Session:
    """Creates the session with which API information will be requested"""
    pass
