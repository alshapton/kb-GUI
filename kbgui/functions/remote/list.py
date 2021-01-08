from typing import Dict
import functions.remote.utils as utl 
import functions.remote.urldata as url

def list_cats(config: Dict[str, str],KB_DETAILS: Dict[str,str]):
    """
    List the categories.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    requestUrl = KB_DETAILS['server'] + '/' + url.Domain.categories
    return utl.makeRequest(requestUrl,KB_DETAILS['user'],KB_DETAILS['pwd'], 1 )
    
