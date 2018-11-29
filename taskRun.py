#!/usr/bin/env python
# -*- coding: utf-8 -*-

import libs.schedule as schedule
from libs.color.termcolor import colored, cprint
from conf.config import *
from common import *
import thread
import argparse
import os
import sys
import importlib
import time
import logging

logging.basicConfig(
    level=logging.INFO, # filename='/tmp/wyproxy.log',
    format='%(asctime)s [%(levelname)s] %(message)s',
)

class TaskManage(object):
	def __init__(self, host):

		self.host = host
		self.result = []

	def getTime(self):
		return time.strftime("%Y-%m-%d %H:%M")

	def run(self):
		# print colored('[*]<{}> Start Run ...'.format(self.getTime()),'green')
		logging.info(colored('[*]Start Run ...','green'))
		schedule.every(freq).seconds.do(self.scan)
		try:
			while True:
				schedule.run_pending()
		except KeyboardInterrupt:
			# print '[*]User exit!'
			logging.info('[*]User exit!')
			sys.exit(0)


			return None
		
	def scan(self):
		# print colored('[*]Run sqlconn','green')

		# result = sqli('check', '1')
		result = sqli(method='check', dataid=None, host=self.host)
		# print result
		if not result:
			# print colored('[^-^]Have no new Data I\'m Waiting .. ..','yellow')
			logging.info(colored('[^-^]Have no new Data I\'m Waiting .. ..','yellow'))
			logging.info(colored('[+]Scan Result:\n{}'.format(self.result), 'yellow'))
			pass
		else:
			self.loadPlugin(result)
			for allData in result:
				dataid = allData[0]
				result = sqli(method='update', dataid=dataid, host=None)



	def loadPlugin(self, data):
		script_path = os.path.dirname(os.path.abspath(__file__))
		plugin_path = os.path.join(script_path, 'plugins')
		
		items = os.listdir(plugin_path)

		for item in items:
			if item.endswith(".py") and not item.startswith('__'):
				plugin_name = item[:-3]
				module = importlib.import_module("plugins." + plugin_name)
				plugLoad = module.YeScan(data)
				# print colored('[-]Load Plugin:{}'.format(module.description),'yellow')
				logging.info(colored('[-]Load Plugin:{}'.format(plugLoad.description),'yellow'))

				# print plugLoad.description
				# print plugLoad.category

				# print dir(plugLoad)

				try:
					
					result = plugLoad.run()

				except Exception,e:
					# print colored('[!]<{}> Error:\n{}'.format(self.getTime(),e.__doc__), 'red')
					logging.info(colored('[!]Error:{}'.format(e), 'red'))
					pass

				# print result
				# print result[plugLoad.category]

				# thread.start_new_thread(module.run, (data,))

				if result[plugLoad.category]:
					# if result not in self.result:
					self.result.append(result)

		# print colored('[+]<{}> Scan Result:\n{}'.format(self.getTime(), self.result), 'green')
		logging.info(colored('[+]Scan Result:\n{}'.format(self.result), 'green'))

# scan = TaskManage('ctnma.cn')
# scan.run()

if __name__ == '__main__':

	print '''
+-------------------------------------------+
	__     __   _____                    
	\ \   / /  / ____|                    
	 \ \_/ /__| (___   ___ __ _ _ __      
	  \   / _ \\___ \ / __/ _` | '_ \      
	   | |  __/____) | (_| (_| | | | |   
	   |_|\___|_____/ \___\__,_|_| |_|                                                                             
	    Author:ADO  {1.0#dev}            
+-------------------------------------------+
'''

	parser = argparse.ArgumentParser(description="Ye Scan Ver:1.0")
	parser.add_argument("-t", "--target", metavar="" , help="scan target")

	args = parser.parse_args()

	if args.target:
		try:
			scan = TaskManage(args.target)
			scan.run()
			sys.exit(1)
		except Exception,e:
			print e
			sys.exit(-1)

	parser.print_help()


