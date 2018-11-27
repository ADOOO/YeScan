#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thread
import time


def run(**kwargs):
	print kwargs['method']


def main():
	for i in range(5):
		result = thread.start_new_thread(run, (i,))

# run('1')
run(method='check', dataid=None, host='1.com')