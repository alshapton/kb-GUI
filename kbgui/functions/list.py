from typing import Dict
import functions.local.list as lcl
import functions.remote.list as rmt

def list_categories(config: Dict[str, str],destination:str):
    """
    List the categories.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    

    def local():
        results = lcl.list_cats(config)
        return results

    def remote():
        return rmt.list_cats(config)
    
    switcher = {
        'local': local,
        'remote': remote
    }

    fn = switcher.get(destination, lambda: "Invalid destination")
    
    # Execute the function
    results = fn()

    return results["Categories"]
