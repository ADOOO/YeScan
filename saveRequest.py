#!/usr/bin/env python
# -*- coding: utf-8 -*-

from burp import IBurpExtender,IHttpListener,IContextMenuFactory
from java.io import PrintWriter
from javax.swing import JMenuItem
from java.util import List,ArrayList

import libs.pymysql as pymysql
from conf.config import *

class BurpExtender(IBurpExtender,IHttpListener,IContextMenuFactory):

	def registerExtenderCallbacks(self,callbacks):
		self._callbacks = callbacks
		self.context = None
		callbacks.setExtensionName("SaveReqRes by ADO")
		self._helpers = callbacks.getHelpers()
		callbacks.registerHttpListener(self)
		return

	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		''' 
			All method here
		'''
		# messageInfo ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__doc__', '__ensure_finalizer__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__subclasshook__', '__unicode__', 'b', 'class', 'comment', 'equals', 'getClass', 'getComment', 'getHighlight', 'getHost', 'getHttpService', 'getPort', 'getProtocol', 'getRequest', 'getResponse', 'getStatusCode', 'getUrl', 'hashCode', 'highlight', 'host', 'httpService', 'notify', 'notifyAll', 'port', 'protocol', 'request', 'response', 'setComment', 'setHighlight', 'setHost', 'setHttpService', 'setPort', 'setProtocol', 'setRequest', 'setResponse', 'statusCode', 'toString', 'url', 'wait']

		# print '[getClass]{}'.format(messageInfo.getClass())
		# print '[getComment]{}'.format(messageInfo.getComment().tostring())
		# print '[getHighlight]{}'.format(messageInfo.getHighlight().tostring())

		# print '[getHost]{}'.format(messageInfo.getHost())
		# print '[getHttpService]{}'.format(messageInfo.getHttpService())
		# print '[getPort]{}'.format(messageInfo.getPort())
		# print '[getProtocol]{}'.format(messageInfo.getProtocol())
		# print '[getRequest]{}'.format(messageInfo.getRequest().tostring())
		# if messageInfo.getResponse():
		# 	print '[getResponse]{}'.format(messageInfo.getResponse().tostring())
		# print '[getStatusCode]{}'.format(messageInfo.getStatusCode())
		# print '[getUrl]{}'.format(messageInfo.getUrl())

		''' 
			Userful method here
		'''

		code = str(messageInfo.getStatusCode())


		if code != '0':
			try:
				host = str(messageInfo.getHost())
				url = str(messageInfo.getUrl())
				req = str(messageInfo.getRequest().tostring())
				res = None
				if messageInfo.getResponse():
					res = str(pymysql.escape_string(messageInfo.getResponse().tostring()))
				print '[getUrl]{}'.format(url)
				ext = url.split('/')[-1].split('?')[0].split('.')[-1]
				if ext not in static:
					sql =  '''insert ignore into burpsuiteHistory (host,url,statusCode,req,res) values ('{host}','{url}','{statusCode}','{req}','{res}')'''.format(host=host, url=url, statusCode=code, req=req, res=res)
					self.sqlSave(sql)
					print '[*]Save Success!'
			except Exception,e:
				print '[*]Error! {}'.format(e.__doc__)
	
	def sqlSave(self, sql):
		conn = pymysql.connect(host = ip, db = db, port = port, user = user, passwd = pwd, charset = 'utf8')
		cus = conn.cursor()
		cus.execute(sql)
		conn.commit()
		cus.close()
		conn.close()