'''
	This is Assignment 2
'''

def pricingService():
	'''
		I am here assuming that I will get this kind of price list from another service.
		This list is having an improved design so that we can add many prices for a single item.
		Here you can see I have added one more proce for ites A. So there are 3 prices now.
	'''
	pricelist = [
		{
			'id':'1',
			'item': 'A',
			'prices':{
				'1':'50',
				'3':'130',
				'4':'10'
			}
		},
		{
			'id':'2',
			'item': 'B',
			'prices':{
				'1':'30',
				'2':'45'
			}
		},
		{
			'id':'3',
			'item': 'C',
			'prices':{
				'1':'20',
				'5':'80'
			}
		},
		{
			'id':'4',
			'item': 'D',
			'prices':{
				'1':'15',
			}
		}
	]
	return pricelist

class CheckOut():
	'''
		Checkout class definition here
	'''
	def __init__(self,price_call):
		'''
			price_list will keep the price list collected from another service
			item_list will keep the id of every item we scan
		'''
		self.price_list = price_call()
		self.item_list = []

	def scan(self,item):
		'''
			Here I am appending the id of scanned items in item_list
		'''
		self.item_list.append(item)

	def calculate_my_order_detail(self):
		'''
			temp will keep the items we have processed. It will be used for finding item repetation in ordere
			p1 is going to keep the item price so that we can calculate the total
			amounts will keep the processed items price, so that we can sum it up for finding total
			backup_amount is just used for keeping a bakup of amounts as we may remove values from amount during item repetation			
		'''
		temp = []
		p1 = 0
		amounts = []
		backup_amounts = []
		for i in self.item_list:  # iterating over the order items
			temp.append(i)
			icount = temp.count(i)
			d = next(x['prices'] for x in self.price_list if x['id']==i) #finding the price list of the item
			try:
				p1 = round(float(d[str(icount)]),2)  # exception may generate if the price list is not available for that item count
				if icount != 1:           # checking whether the item is repeated or not
					for item in backup_amounts: # here I am removing the previously processed amounts if the item count falls in a new price list
						if item[0]==i:
							amounts.remove(item)
			except Exception, e:
				p1 = round(float(d['1']),2) # if exception generated for a specific item count then single unit price will be considered
			amounts.append((i,p1))
			backup_amounts = list(amounts) # copying the amounts for backup

		return sum(list(t[1] for t in amounts)) # finding the sum of prices in the order