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
    requestUrl = KB_DETAILS['server'] + '/' + url.Domain.list_categories
    try:
        results = utl.makeRequest(requestUrl,KB_DETAILS['user'],KB_DETAILS['pwd'], 1 )
    except Exception as e:
        raise e
    return results["Categories"]

def list_bases(config: Dict[str, str],KB_DETAILS: Dict[str,str]):
    """
    List the available knowledge bases.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    requestUrl = KB_DETAILS['server'] + '/' + url.Domain.list_bases
    try:
        results = utl.makeRequest(requestUrl,KB_DETAILS['user'],KB_DETAILS['pwd'], 1 )
    except Exception as e:
        raise e
    return results
