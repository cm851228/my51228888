# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/1/21 23:07
# @file    : 界影视

P='vod_remarks'
O='vod_name'
N='vod_id'
M='url'
L='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
K='User-Agent'
H='data'
G=print
F=int
E='type_name'
D='jx'
C='parse'
A='list'
import hashlib as I,re,sys,time as J,requests as B
sys.path.append('..')
from base.spider import Spider as Q
class Spider(Q):
	def getName(A):return'JieYingShi'
	def init(A,extend=''):A.home_url='https://www.hkybqufgh.com';A.error_url='https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4';A.headers={K:L}
	def getDependence(A):return[]
	def isVideoFormat(A,url):0
	def manualVideoCheck(A):0
	def homeContent(B,filter):A='type_id';return{'class':[{A:'1',E:'电影'},{A:'2',E:'电视剧'},{A:'4',E:'动漫'},{A:'3',E:'综艺'}]}
	def homeVideoContent(B):E=B.get_data(B.home_url);return{A:E,C:0,D:0}
	def categoryContent(B,cid,page,filter,ext):E=B.home_url+f"/vod/show/id/{cid}/page/{page}";F=B.get_data(E);return{A:F,C:0,D:0}
	def detailContent(B,did):E=did[0];F=B.get_detail_data(E);return{A:F,C:0,D:0}
	def searchContent(B,key,quick,page='1'):
		if F(page)>1:return{A:[],C:0,D:0}
		E=B.home_url+f"/vod/search/{key}";G=B.get_data(E);return{A:G,C:0,D:0}
	def playerContent(A,flag,pid,vipFlags):B=A.get_play_data(pid);return{M:B,'header':A.headers,C:0,D:0}
	def localProxy(A,params):0
	def destroy(A):return'正在Destroy'
	def get_data(F,url):
		D=[]
		try:
			A=B.get(url,headers=F.headers)
			if A.status_code!=200:return D
			E=re.findall('\\\\"vodId\\\\":(.*?),',A.text);H=re.findall('\\\\"vodName\\\\":\\\\"(.*?)\\\\"',A.text);I=re.findall('\\\\"vodPic\\\\":\\\\"(.*?)\\\\"',A.text);J=re.findall('\\\\"vodRemarks\\\\":\\\\"(.*?)\\\\"',A.text)
			for C in range(len(E)):D.append({N:E[C],O:H[C],'vod_pic':I[C],P:J[C]})
		except B.RequestException as K:G(K)
		return D
	def get_detail_data(K,ids):
		S='vod_play_url';C=ids;D=K.home_url+f"/api/mw-movie/anonymous/video/detail?id={C}";L=str(F(J.time()*1000));T=K.get_headers(L,f"id={C}&key=cb808529bae6b6be45ecfab29a4889bc&t={L}")
		try:
			I=B.get(D,headers=T)
			if I.status_code!=200:return[]
			A=I.json()[H];M={E:A['vodClass'],N:A['vodId'],O:A['vodName'],P:A['vodRemarks'],'vod_year':A['vodYear'],'vod_area':A['vodArea'],'vod_actor':A['vodActor'],'vod_director':A['vodDirector'],'vod_content':A['vodContent'],'vod_play_from':'蓝光秒播',S:''};Q=[]
			for R in I.json()[H]['episodeList']:U=R['name'];D=R['nid'];Q.append(f"{U}${C}-{D}")
			M[S]='#'.join(Q);return[M]
		except B.RequestException as V:G(V)
		return[]
	def get_play_data(C,play):
		D=play.split('-');E=D[0];I=D[1];N=C.home_url+f"/api/mw-movie/anonymous/v2/video/episode/url?clientType=1&id={E}&nid={I}";K=str(F(J.time()*1000));O=C.get_headers(K,f"clientType=1&id={E}&nid={I}&key=cb808529bae6b6be45ecfab29a4889bc&t={K}")
		try:
			L=B.get(N,headers=O)
			if L.status_code!=200:return C.error_url
			return L.json()[H][A][0][M]
		except B.RequestException as P:G(P)
		return C.error_url
	@staticmethod
	def get_headers(t,e):A=I.sha1(I.md5(e.encode()).hexdigest().encode()).hexdigest();B={K:L,'Accept':'application/json, text/plain, */*','sign':A,'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"','t':t,'referer':'https://www.hkybqufgh.com/'};return B
if __name__=='__main__':0
