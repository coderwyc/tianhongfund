#_*_coding:utf-8_*_
#正则匹配基金代码、基金净值和更新时间
from urllib2 import urlopen
import re

urls=["http://fund.eastmoney.com/000051.html",
     "http://fund.eastmoney.com/213008.html",
     "http://fund.eastmoney.com/000173.html",
     "http://fund.eastmoney.com/000477.html"]

find_re = re.compile(r'<div id="statuspzgz" class="fundpz"><span class=".+?">(.+?)</span>',re.DOTALL)
html_re = re.compile(r'http://fund.eastmoney.com/(.+?).html',re.DOTALL)
time_re = re.compile(r'<p class="time">(.+?)</p>',re.DOTALL)

for ulr in urls:   
    html=urlopen(ulr).read()
    print html_re.findall(ulr)
    print find_re.findall(html)
    print time_re.findall(html)
    print ''