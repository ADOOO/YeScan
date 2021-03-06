#!/usr/bin/env python

"""
Copyright (c) 2006-2016 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import base64

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOWEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Base64 all characters in a given payload

    >>> tamper("1' AND SLEEP(5)#")
    'MScgQU5EIFNMRUVQKDUpIw=='
    """

    #return base64.b64encode('6990'+payload.encode(UNICODE_ENCODING)) if payload else payload


    return payload.replace('SELECT','SelEc<i>t').replace('union','unio<i>n').replace('AND','aN<i>d').replace('from','fro<i>m') if payload else payload
