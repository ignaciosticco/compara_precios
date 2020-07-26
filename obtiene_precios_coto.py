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

	#### Intento extraccion de precio ####

	print(html_soup)
	text_file = open("sample.txt", "w")
	n = text_file.write('{}'.format(html_soup))
	text_file.close()

	#### Intento extraccion de producto ####

	# Esto me parece que esta OK. Si imprimis product_containers[0].text te da el nombre del primer producto
	product_containers = html_soup.find_all('div', class_ = 'descrip_full')
	#print(product_containers[0].text)
	



	time.sleep(10)
	

if __name__ == '__main__':
    main()