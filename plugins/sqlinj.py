#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conf.config import *
# import libs.pymysql as pymysql
from common import *
import libs.gevent as gevent
from libs.gevent import monkey; monkey.patch_all()

from Queue import Queue

from subprocess import Popen,PIPE
import sys
import re
import time


class YeScan(object):

	description = 'SqlInj check! - [Author:ADO]'
	category = 'sql'

	def __init__(self, data):
		self.data = data
		self.queue = Queue()
		self.result = {}
		self.temp = []

	def run(self):
		# result = {}
		
		for allData in self.data:
			self.queue.put(allData)

		gevent_pool = []

		for i in range(thread_count):
			gevent_pool.append(gevent.spawn(self.sqlMapScna, self.queue))
		gevent.joinall(gevent_pool)
			# print dataid,reqData

		self.result[YeScan.category] = self.temp

		# print self.result
		return self.result

	def sqlMapScna(self, queue):

		while not queue.empty():
			allData = queue.get_nowait()

			dataid = allData[0]
			reqData = allData[4]
			reqUrl = allData[2]

			if 'sqlrun.' in reqData:
				sqlData = sqli(dataid=dataid, method='checksql', host=None)

				try:
					if sqlData[0][0] == 0:
						sqli(dataid=dataid, method='updatesql', host=None)
						checkFile = self.creatFile(reqData)
						checkSqlinj = Popen(['python',sqlmapPath, '--batch', '-r'+checkFile], stdin=PIPE, stdout=PIPE)
						sqlmapResult = checkSqlinj.stdout.read()
						
						# print sqlmapResult

						if '] [INFO] the back-end DBMS is ' in sqlmapResult:
							
							# dbms = re.findall('back-end DBMS: (.*?)\n', sqlmapResult)
							dbms = re.findall('INFO] the back-end DBMS is (.*?)\n', sqlmapResult)[0]

							# print '[=======]'+dbms
							
							self.temp.append([dataid,reqUrl,dbms])
				except Exception,e:
					print colored('[!]<{}> Error:\n{}'.format(self.getTime(),e.__doc__), 'red')
					sqli(dataid=dataid, method='updatesql', host=None)
					pass
			sqli(dataid=dataid, method='updatesql', host=None)



	def creatFile(self,req):
		stime = time.strftime("%Y%m%d%H%M%S")
		filename = '{}{}.txt'.format(reqPath,stime)
		f = open(filename,'w')
		f.write(req)
		f.close()
		return filename
