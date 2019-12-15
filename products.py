import os # operation system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品名稱, 價格' in line:
				continue #跳過不執行
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
	return products


#讓使用者輸入資料
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price]) #直接在這行創作小清單
	print(products)
	return products
		#上面是簡寫法，也可寫成
		#p = []  #先創作空的小清單
		#p.append(name)
		#p.append(price)
		#products.append(p)
		
		#或是也可寫成
		# p = [name, price]
		# products.append(p)

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '這個商品的價格是:', p[1], '元')

#將輸入的資料寫入，建立新檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品名稱, 價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv' #降低重複性
	if os.path.isfile(filename):
		print('有這個檔案喔!')	
		products = read_file(filename)
	else:
		print('沒有這個檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
#重構程式 refactor
main() #每個function只做一件事

