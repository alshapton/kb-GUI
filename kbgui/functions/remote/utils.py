# -*- encoding: utf-8 -*-
# kb-gui v0.1.0
# A GUI for "kb" - a knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-GUI utilities module (specifically for remote kb's)
:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""
import json
import requests
import requests.exceptions as re

def jsonParameters(parameters):
    """
    :type parameters: str
    converts a JSON document into a URL parameter string
    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing the list
        of parameters to add to the API call
    Returns
    -------
    params
        a string which can be appended to the URL
    """
    if (parameters == ''):
        return ''
    else:
        jsonObject = json.loads(parameters)
        params = '?'
        for key in jsonObject:
            value = jsonObject[key]
            params = params + key + '=' + value + '&'
        return params[:-1]


def makeRequest(requestUrl, user:str, pwd:str, timeOut=1, parameters=''):

    """
    :param requestUrl: str
    :param timeOut: Optional[str]
    :param parameters: Optional[str]
    :return: object:
    Sends a request to the API
    Parameters
    ----------
    requestURL : str
        string to pass into the REST API
    timeOut : int
        optional - API call timeout
    parameters : str
        optional parameters to append to URL as query modifiers
    Returns
    -------
    response
        a string which is a JSON document returned from the API
    Exceptions
    ----------
    SpaceXReadTimeOut
        raised when the API call breaches the timeout limit
    """

    try:
        url_response = requests.get(url=str(requestUrl)
                                    + jsonParameters(parameters),
                                    timeout=timeOut,
                                    auth=(user,pwd))
    except (re.ConnectionError,requests.exceptions.ReadTimeout):
        raise re.ConnectionError    
    else:
        response = url_response.json()
    return response 