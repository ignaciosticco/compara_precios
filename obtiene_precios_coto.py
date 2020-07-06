import bs4 as bs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

if __name__ == '__main__':
    main()