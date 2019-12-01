products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) #直接在這行創作小清單

	#上面是簡寫法，也可寫成
	#p = []  #先創作空的小清單
	#p.append(name)
	#p.append(price)
	#products.append(p)
	
	#或是也可寫成
	# p = [name, price]
	# products.append(p)
print(products)

