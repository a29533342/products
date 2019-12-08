#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品名稱,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

#讓使用者輸入資料
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
#印出所有購買紀錄
print(products)
for p in products:
	print(p)
	print(p[0], '這個商品的價格是:', p[1], '元')

#將輸入的資料寫入，建立新檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品名稱, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


