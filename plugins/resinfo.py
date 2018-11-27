#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# data[0][0:id,1:host,2:url,3:statusCode,4:req,5:res,6:state,7:time]

class YeScan(object):

	description = 'Basic Information check! - [Author:ADO]'
	category = 'Inf'

	def __init__(self, data):
		self.data = data
		self.result = {}

	def run(self):
		# pass
		# print type(data)
		temp = []
		for allData in self.data:
			dataid = allData[0]
			resData = allData[5]
			reqUrl = allData[2]
			try:
				# server = re.findall('Server: (.*?)\n', resData)
				# xpb = re.findall('X-Powered-By: (.*?)\n', resData)
				# tel = re.findall('1[34578]\\d{9}', resData)
				mail = re.search('^[-_\w\.]{0,64}@([-\w]{1,63}\.)*[-\w]{1,63}$', resData)
				path = re.findall('[cdef]:\\\\\w{1,8}|/bin/\w{1,8}|/dev/\w{1,8}|/home/\w{1,8}|/lib64/\w{1,8}|/media/\w{1,8}|/opt/\w{1,8}|/root/\w{1,8}|/sbin/\w{1,8}|/sys/\w{1,8}|/usr/\w{1,8}|/boot/\w{1,8}|/etc/\w{1,8}|/lib/\w{1,8}|/lost+found/\w{1,8}|/mnt/\w{1,8}|/proc/\w{1,8}|/run/\w{1,8}|/srv/\w{1,8}|/tmp/\w{1,8}|/var/\w{1,8}', resData)

				# if server: print server[0]
				# if xpb: print xpb[0]
				# if tel: print tel[0]
				# if mail: print mail
				# if path: print path
				# print server,xpb,tel,mail,path
				# if server: tmep.append(server[0].rstrip())
				# if xpb: tmep.append(xpb[0].rstrip())
				# if tel: tmep.append([reqUrl,tel[0].rstrip()])

				if mail: temp.append([dataid,reqUrl,mail.group()])
				if path: temp.append([dataid,reqUrl,path[0].rstrip()])

				# print tmep
				# result[category] = list(set(tmep))
				self.result[YeScan.category] = temp

			except Exception,e:
				print e
				# print e.__doc__
				pass

		# if result: print result
		return self.result
