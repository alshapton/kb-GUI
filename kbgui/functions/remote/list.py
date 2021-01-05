from typing import Dict
import functions.remote.utils as utl 
import functions.remote.urldata as url

def list_cats(config: Dict[str, str]):
    """
    List the categories.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    requestUrl = url.Domain.base + url.Domain.categories
    return utl.makeRequest(requestUrl, 1)
    
