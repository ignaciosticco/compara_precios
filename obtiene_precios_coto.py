import bs4 as bs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from requests import get
from lxml import html
import requests

class precioBot_coto:

	def __init__(self):
		self.driver = webdriver.Chrome()


	def accede_al_sitio(self, url):
		self.driver.get("{}".format(url))

	def busca_producto(self, producto):

		id_busqueda = self.driver.find_element_by_id('atg_store_searchInput')
		id_busqueda.send_keys('{}'.format(producto))
		id_busqueda.send_keys(Keys.ENTER)



def main():
	

	bot = precioBot_coto()
	url = 'http://www.cotodigital3.com.ar/'
	bot.accede_al_sitio(url)
	print("¿Qué producto buscas?\n")
	producto = str(input())
	bot.busca_producto(producto)

	response = get(bot.driver.current_url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	#product_containers = html_soup.find_all('li', class_ = 'clearfix')
	#producto = product_containers[1]
	#test1 = producto.span.span.span
	#test1 = producto.div.div
	#print( html_soup.findAll("span", {"class": "price_regular_precio"}))
	#print(product_containers[1].findAll("span", {"class": "precioContado"}))
	product_containers = html_soup.find_all('li', class_ = 'clearfix')
	print(html_soup)
	print(atg_store_productImage)
	
	time.sleep(10)
	

if __name__ == '__main__':
    main()