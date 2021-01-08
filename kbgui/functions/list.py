# -*- encoding: utf-8 -*-
# kb-gui v0.1.0
# A GUI for "kb" - a knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-GUI list module (destination generic)
:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict
import functions.local.list as lcl
import functions.remote.list as rmt

def list_categories(config: Dict[str, str], KB_DETAILS: Dict[str,str]):
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
        return rmt.list_cats(config, KB_DETAILS)
    
    switcher = {
        'local': local,
        'remote': remote
    }
    
    fn = switcher.get(str(KB_DETAILS['location']), lambda: "Invalid destination")
    
    # Execute the function
    results = fn()

    return results["Categories"]
