import feedparser
import re

def getwordcounts(url):
	d=feedparser.parse()
	wc={}

	for e in d.entries:
		if 'sumary' in e: sumary=e.sumary
		else: sumary=e.description
	
		words=getwords(e.title+' '+sumary)
		for word in words:
			wc.setdefault(word,0)
			wc[word] += 1

	return d.feed.title,wc

def getwords(html):
	"""docstring for getwords"""
	txt = re.compile(r'<[^]+>').sub('',html)

	words.re.compile(r'[^A-Z^a-z]+').split(txt)

	return [word.lower() for word in words if word!='' ]
