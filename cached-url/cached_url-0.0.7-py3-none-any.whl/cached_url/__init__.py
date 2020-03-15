#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'cached_url'
import os
import sys
import hashlib
import requests
import re

def getUrlContent(url, headers = {}):
	headers['method'] = headers.get('method', 'GET')
	headers['accept'] = headers.get('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/apng,*/*;q=0.8,application/signed-exchange;v=b3')
	headers['user-agent'] = headers.get('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
	r = requests.get(url, headers=headers)
	r.encoding = 'utf-8'
	return r.text
	
def getFileName(url):
	h = hashlib.sha224(url.encode('utf-8')).hexdigest()[:3]
	k = re.sub(r'\W+', '', url.split('/')[-1].split('.')[0])[:10]
	return k + '_' + h

def cachedContent(url, headers = {}):
	cache = 'tmp/' + getFileName(url) + '.html'
	try:
		with open(cache) as f:
			return f.read()
	except:
		content = getUrlContent(url, headers)
		os.system('mkdir tmp > /dev/null 2>&1')
		with open(cache, 'w') as f:
			f.write(content)
		return content

def get(url, headers = {}, force_cache=False):
	if force_cache or 'test' in str(sys.argv):
		return cachedContent(url, headers)
	else:
		return getUrlContent(url, headers)