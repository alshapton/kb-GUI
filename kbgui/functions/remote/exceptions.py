"""Exceptions module
This module contains the exceptions which the remote calls to the API generate:
This file is imported as a module and contains the following

Exceptions:
    * KBAPIReadTimeOut - if a call to the API times out.
        The timeout respects the timeOut parameter on all functions
"""


class KBAPIReadTimeOut(Exception):
    pass
