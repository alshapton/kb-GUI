
"""urldata module

This is a module defines the endpoints for the REST KB API
as well as some global data
"""


class Domain(object):
    """ Base URL from which to assemble request URLs """
    protocol = "http"
    host = "localhost"
    port = "5000"

    base = protocol + "://" + host + ":" + port + "/"


    # Declaration of the endpoints

    # Categories    
    list_categories = "categories"

    #   Bases
    list_bases = "base/list"
