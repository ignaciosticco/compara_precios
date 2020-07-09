import bs4 as bs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from requests import get


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


	product_containers = html_soup.find_all('li', class_ = 'clearfix')
	producto = product_containers[0]
	test1 = producto.span.span
	#print(test1)


	time.sleep(10)
	

if __name__ == '__main__':
    main()