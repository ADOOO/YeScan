#!/usr/bin/env python
# -*- coding: utf-8 -*-

import libs.pymysql as pymysql
from common import *
from conf.config import *

# Sqlconn search/update data
# def sqli(method, dataid):
def sqli(**kwargs):


	method,dataid,host = kwargs['method'],kwargs['dataid'],kwargs['host']

	if method == 'check':
		sql = 'select * from burpsuiteHistory where host like "%{}%" and state = 0'.format(host)
	if method == 'update':
		sql = 'update burpsuiteHistory set state=1 where id={}'.format(dataid)
	if method == 'checksql':
		sql = 'select sqlmapState from burpsuiteHistory where id={}'.format(dataid)
	if method == 'updatesql':
		sql = 'update burpsuiteHistory set sqlmapState=1 where id={}'.format(dataid)

	try:
		conn = pymysql.connect(host = ip, db = db, port = port, user = user, passwd = pwd, charset = 'utf8')
		cus = conn.cursor()
		# sql = 'select * from burpsuiteHistory where host like "%{}%" and state = 0'.format(self.host)
		cus.execute(sql)
		result = cus.fetchall()
		conn.commit()
		cus.close()
		conn.close()
		return result
	except Exception,e:
		# print e.__doc__
		print e