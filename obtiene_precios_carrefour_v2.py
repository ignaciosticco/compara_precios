'''
Este script encuentra e imprime los precios del supermercado carrefour
Hay que pasarle un url del producto cuyo precio se quiere imprimir
'''


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
			precio_output = precio[1].text

		else:
			precio_output = precio.text

		return precio_output

def main():

	#url = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'

	bot = PrecioBot()
	bot.accede_al_sitio(url)
	time.sleep(2)
	precio = bot.driver.find_element_by_class_name("regular-price")	
	bot.imprime_precio(precio)



if __name__ == '__main__':
    main()