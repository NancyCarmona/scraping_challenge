from flask import Flask,request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/')
def root():
	return 'Inicio'

def get_precios(lista):
	precios = [float(precio.text.replace('$\xa0','')) for precio in lista]
	return min(precios),max(precios)

@app.route('/get_elements',methods=['POST'])
def get_15_elements():
	data_input=request.get_json()
	url=data_input['url']
	data_productos={
		'url':url
	}
	options = Options()
	options.headless = True
	options.add_argument("--start-maximized")
	driver = webdriver.Firefox(options=options)
	try:
		driver.get(url)
		time.sleep(10)
	except:
		driver.close()
		return None
	driver.execute_script(f"window.scrollBy(0, 1000);")
	time.sleep(10)
	driver.execute_script(f"window.scrollBy(0, 1000);")
	time.sleep(20)
	contenido = BeautifulSoup(driver.page_source,'html.parser')
	driver.close()
	total_elementos=(contenido.find('div',{'id':'gallery-layout-container'})).find_all('div',recursive=False)
	products=[]
	while len(products)<15:
		dic_producto={
			'nombre':'',
			'price':'',
			'promo_price':''
		}
		precio=total_elementos[len(products)].find_all('div',{'id':'items-price'})
		nombre=total_elementos[len(products)].find('h3')
		dic_producto['nombre']=nombre.text
		if len(precio)==1:
			dic_producto['price']=precio[0].text.replace('\xa0',' ')
			dic_producto['promo_price']=precio[0].text.replace('\xa0',' ')
		else:
			promo,regular=get_precios(precio)
			dic_producto['price']=f'$ {regular:.3f}'
			dic_producto['promo_price']=f'$ {promo:.3f}'
		products.append(dic_producto)
	data_productos['products']=products
	return data_productos, 200

"""if __name__ == '__main__':
	
	app.run(debug=True)"""
