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
import functions.local.list as list_lcl
import functions.remote.list as list_rmt



def list_categories(config: Dict[str, str], KB_DETAILS: Dict[str,str]):
    """
    List the categories.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    
    def local():
        results = list_lcl.list_cats(config)
        return results

    def remote():
        return list_rmt.list_cats(config, KB_DETAILS)
    
    api = {
    'local': local,
    'remote': remote
    }

    fn = api.get(str(KB_DETAILS['location']), lambda: "Invalid destination")
    
    # Execute the function
    try:
        results = fn()
    except Exception as e:
        raise e
    return results


def list_bases(config: Dict[str, str], KB_DETAILS: Dict[str,str]):
    """
    List the knowledge bases.
    Arguments:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DATA           - the main path of the DATA
    """
    
    def local():
        results = list_lcl.list_bases(config)
        return results

    def remote():
        # return list_lcl.list_bases(config, KB_DETAILS)
        results = list_lcl.list_bases(config)
        return results

    api = {
    'local': local,
    'remote': remote
    }
    
    fn = api.get(str(KB_DETAILS['location']), lambda: "Invalid destination")

    # Execute the function
    try:
        results = fn()
    except Exception as e:
        raise e

    return results