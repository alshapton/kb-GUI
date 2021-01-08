import kb.actions.list as ls
from typing import Dict

def list_cats(config: Dict[str, str]):
    """
    List the categories.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """

    return ls.list_categories(config)
