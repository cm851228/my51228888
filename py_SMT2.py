#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2026/1/1
# @file    : SMT.py

D='User-Agent'
A='utf-8'
import sys,time,hashlib as F,requests as B,base64 as C,json
from urllib import parse
sys.path.append('..')
from base.spider import Spider as E
class Spider(E):
	def __init__(A):B='127.0.0.1';super().__init__();A.name='TvSmt';A.headers={D:'Mozilla/5.0','CLIENT-IP':B,'X-FORWARDED-FOR':B};A.cache={};A.extendDict={};A.proxies={}
	def getName(A):return A.name
	def init(A,extend='{}'):
		try:A.extendDict=json.loads(extend)
		except:A.extendDict={}
		B=A.extendDict.get('proxy',None)
		if B is None:A.proxies={}
		else:A.proxies={'http':B,'https':B}
	def liveContent(A,url):
		C={D:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}
		try:E=B.get(url,headers=C,proxies=A.proxies);return E.text
		except Exception as F:print(F)
		return''
	def localProxy(A,params):
		B=params;C=B['type']
		if C=='m3u8':D=A.get_play_url(B);return[200,'application/vnd.apple.mpegurl',A.parse_m3u8_text(D)]
		if C=='ts':E=A.b64decode(B['url']);return[206,'application/octet-stream',A.parse_ts(E)]
	def get_play_url(C,params):
		B=params['pid']
		if C.cache.get(B):return C.cache[B]
		G=bytearray([115,109,116,46,116,118,104,100,46,100,112,100,110,115,46,111,114,103]).decode();H=f"http://{G}:8278/{B}/playlist.m3u8";D=str(int(time.time()/150));I={'tid':'mc42afe745533','ct':D,'tsum':F.md5(f"tvata nginx auth module/{B}/playlist.m3u8mc42afe745533{D}".encode(A)).hexdigest()};E=H+'?'+parse.urlencode(I);C.cache[B]=E;return E
	def parse_m3u8_text(A,url):
		E=url.rsplit('/',1)[0]+'/';F=B.get(url,headers=A.headers,proxies=A.proxies);G=F.text.splitlines();C=[]
		for D in G:
			if'.ts'in D:H='proxy://do=py&type=ts&url='+A.b64encode(E+D);C.append(H)
			else:C.append(D)
		return'\n'.join(C)
	def parse_ts(A,url):return B.get(url,headers=A.headers,proxies=A.proxies).content
	def destroy(A):return'正在Destroy'
	def b64encode(B,data):return C.b64encode(data.encode(A)).decode(A)
	def b64decode(B,data):return C.b64decode(data.encode(A)).decode(A)
if __name__=='__main__':0
