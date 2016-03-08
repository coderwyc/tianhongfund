#_*_coding:utf-8_*_
# from crawl import get_net_val
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from allfunds import get_url_by_name
from crawl import get_val

class Fund(object):
	""" 沪深300基金投资,
		investment:投资额
		fund_net:基金净值		
		handing_charge:手续费
	"""
	def __init__(self, investment, fund_net, handing_charge=0.001):
		self.investment = float(investment)
		self.fund_net = fund_net
		self.net_investment = float(investment)/(1+handing_charge)	#净申购额=申购金额/(1+申购费率)
		self.share = self.net_investment / fund_net #申购份额=净申购额/T日基金份额净值
		self.in_charge = [float(investment) - self.net_investment] #申购费用=申购额-净申购金额
		self.out_charge = []
		self.in_ = [fund_net] #记录买入价格
		self.out = [] #记录卖出价格
	def get_share(self):
		"""获取基金份额"""
		return self.share
	def get_profit(self, sell_charge=0.0005):
		"""获取当前利润"""
		return (self.share * self.fund_net) - self.investment
	def update_net(self, new_net):
		"""更新基金净值"""
		self.fund_net = new_net
	def get_all_investment(self):
		"""获取总投资额"""
		return self.investment
	def get_total(self):
		"""获取当前拥有资产"""
		return self.share * self.fund_net
	def buy_more(self, investment, fund_net, handing_charge=0.001):
		"""追加投资"""
		self.in_.append(fund_net)
		self.investment += investment
		self.update_net(fund_net) # 更新基金净值
		self.net_investment = float(investment)/(1+handing_charge)	#净申购额=申购金额/(1+申购费率)
		self.share += self.net_investment / fund_net #申购份额=净申购额/T日基金份额净值
		self.in_charge.append(float(investment) - self.net_investment) #申购费用=申购额-净申购金额
	def unload(self, share, fund_net, sell_charge=0.0005):
		"""减持基金"""
		if share > self.share:
			print 'You have no share'
			return None
		self.out.append(fund_net)
		self.update_net(fund_net) # 更新基金净值
		self.share -= share
		total = share * fund_net  #赎回总额=赎回数量*T日基金份额净值
		self.investment -= total*(1-sell_charge)
		self.out_charge.append(total*sell_charge) #赎回费用=赎回总额*赎回费率
		return total*(1-sell_charge) 

if __name__ == '__main__':
	tz = Fund(1000, 0.7438)
	url = get_url_by_name(u'天弘创业板')
	name, date, val = get_val(url) 	
	tz.update_net(float(val))
	print u'投资额:' + str(tz.get_all_investment())
	print u'基金名称:' + name
	print u'日期:'+ date
	print u'基金净值:'+ val
	print u'基金持有份额:'+str(tz.get_share())
	print u'总资产为:'+str(float(val)*tz.get_share())
	print u'投资收益:'+str(tz.get_profit())
