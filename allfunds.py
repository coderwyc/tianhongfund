#_*_coding:utf-8_*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 爬取天弘所有基金的数据


'''module for get URL of funds by name'''

def get_url_by_name(name):
	try:
		from urllib2 import urlopen
		from lxml.html import parse
		url = 'http://www.thfund.com.cn/column.dohsmode=searchtopic&pageno=0&channelid=2&categoryid=2435&childcategoryid=2436.htm'
		parsed = parse(urlopen(url))
		doc = parsed.getroot()
		navs = doc.find_class('left_nav_new_subnav') # 查找class='left_nav_new_subnav'的项
		# print len(navs)

		funds = {}
		for nav in navs:
			funds_link = nav.findall('.//a')
			for item in funds_link:
				funds[item.text] = item.get('href')
		# print len(funds)
		# print funds
		base_url = 'http://www.thfund.com.cn'
		funds_db = {}
		for key in funds.keys():
			funds[key] = base_url + funds[key]
			spt = key.split('\n')
			funds_db[spt[0]] = funds[key]
		# for k,v in funds_db.items():
		# 	print k
		return funds_db[name]
	except Exception, e:
		raise e


if __name__ == '__main__':
	print get_url_by_name(u'天弘沪深300')

# 天弘鑫安宝保本
# 行健宏扬中国基金
# 天弘中证全指运输
# 天弘稳利定期开放
# 天弘中证食品饮料
# 天弘新价值混合
# 天弘永利债券
# 天弘中证休闲娱乐
# 天弘中证500
# 天弘裕利灵活配置
# 天弘中证移动互联网
# 天弘中证高端装备制造
# 天弘互联网灵活配置
# 天弘精选混合
# 天弘通利混合
# 天弘安康养老
# 天弘中证大宗商品
# 天弘弘利债券
# 天弘鑫动力混合
# 天弘季加利理财债券
# 天弘债券发起式
# 天弘丰利债券LOF
# 天弘现金管家货币
# 天弘新活力混合
# 天弘弘运宝
# 天弘云商宝
# 天弘增益宝
# 天弘中证银行
# 天弘瑞利分级债券
# 天弘余额宝货币
# 天弘创业板
# 天弘添利债券LOF
# 天弘中证电子
# 天弘中证100
# 天弘云端生活优选
# 天弘周期策略
# 天弘上证50
# 天弘中证证券保险
# 天弘中证医药100
# 天弘普惠养老保本
# 天弘惠利混合
# 天弘中证800
# 天弘同利分级债券
# 天弘中证计算机
# 天弘中证全指房地产
# 天弘沪深300
# 天弘中证环保产业
# 天弘永定价值成长