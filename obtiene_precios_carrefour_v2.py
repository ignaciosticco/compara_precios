'''
Este script encuentra e imprime los precios del supermercado carrefour
Hay que pasarle un url del producto cuyo precio se quiere imprimir
'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

class PrecioBot:

	def __init__(self):
		self.driver = webdriver.Chrome()

	def accede_al_sitio(self, url):

		self.driver.get("{}".format(url))

	def imprime_precio(self,precio):

		if precio.text =='':
			'''	
			Los precios en promocion no estan en regular-price sino en product-price
			'''		
			precio = self.driver.find_elements_by_xpath("//*[contains(@id, 'product-price')]")
			precio_output = float(str(precio[1].text).strip('$').replace('.','').replace(',','.'))

		else:
			precio_output = float(str(precio.text.split('$')[1]).replace('.','').replace(',','.'))#precio.text

		return precio_output

def main():

	#url1 = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
	#url2 = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'


	bot = PrecioBot()
	bot.accede_al_sitio(url2)
	time.sleep(2)
	precio = bot.driver.find_element_by_class_name("regular-price")	
	
	precio_output = bot.imprime_precio(precio)


if __name__ == '__main__':
    main()