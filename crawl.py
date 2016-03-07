#_*_coding:utf-8_*_
'''get funds net val and date'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import allfunds
import re
from urllib2 import urlopen
from lxml.html import parse
import requests

def get_net_val(url):
	try:
		# url是沪深3000
		# url = "http://www.thfund.com.cn/column.dohsmode=searchtopic&pageno=0&channelid=2&categoryid=2992&childcategoryid=2993.htm"
		html = urlopen(url).read()
		find_value = re.compile('<td><span style="color:red;">(.+?)</span></td>', re.DOTALL)
		find_time = re.compile('<td>(20.+?)</td>', re.DOTALL)
		net_val = find_value.findall(html)
		date = find_time.findall(html)
		return net_val[0], date[0]
	except:
		print 'Network Failed'

def get_val(url):
	# url是创业板
	# url = "http://www.thfund.com.cn/column.dohsmode=searchtopic&pageno=0&channelid=2&categoryid=3785&childcategoryid=3788.htm"
	parsed = parse(urlopen(url))
	doc = parsed.getroot()
	tables = doc.findall('.//table')
	# print len(tables)
	data = tables[1]
	rows = data.findall('.//tr')
	thhs300 = [val.text_content() for val in rows[1].findall('td')]
	return thhs300[0], thhs300[1], thhs300[2]
if __name__ == '__main__':
	# val, date = get_net_val()
	# print r'日期:'+date
	# print r'基金净值:'+val
	url = allfunds.get_url_by_name(u'天弘创业板')
	name, date, val = get_val(url)
	print r'基金名称:' +  str(name)
	print r'日期:'+ date
	print r'基金净值:'+ val


