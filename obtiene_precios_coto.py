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

	def obtiene_nombre_productos(self,html):
		'''
		Esta funcion devuelve una lista cuyos elementos son los nombres de los productos asociados al 'producto' buscado
		'''
		product_containers = html.find_all('div', class_ = 'descrip_full')
		lista_productos = []
		for producto in product_containers:
			lista_productos+=[producto.text]
		return lista_productos


	def obtiene_precios_productos(self,html):

		html_sting = str(html)
		texto_separado = html_sting.split('\n')

		texto_html_precio = '<span class="precioContado">PRECIO CONTADO</span></span></span></div></li>'  # El precio de un producto aparece luego de este texto (para todos los productos). 
		lista_precios = []
		i=0
		while i<len(texto_separado):
			if texto_html_precio in texto_separado[i]:
				j=0
				flag = True
				while j<len(texto_separado) and flag:
					if '$' in texto_separado[i+j]:
						lista_precios+=[float(texto_separado[i+j].strip(' $'))]
						flag = False
						i = i+j-1
					j+=1
			i+=1
		return lista_precios


	def imprime_lista_precios(self, lista_productos,lista_precios):
		'''
		Imprime en la terminal una tabla de productos y precios
		'''

		print("\nProducto\t\t\tPrecio ")
		for i in range(0,len(lista_productos)):
			print("{}\t\t{}".format(lista_productos[i], lista_precios[i]))

def main():
	

	bot = precioBot_coto()
	url = 'http://www.cotodigital3.com.ar/'
	bot.accede_al_sitio(url)
	print("¿Qué producto buscas?\n")
	producto = str(input())
	bot.busca_producto(producto)

	response = get(bot.driver.current_url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	lista_productos = bot.obtiene_nombre_productos(html_soup)
	lista_precios = bot.obtiene_precios_productos(html_soup)

	bot.imprime_lista_precios(lista_productos,lista_precios)

	#bot.driver.find_element_by_xpath('//*[@title="Siguiente"]').click()
	#bot.driver.find_element_by_xpath('//*[@title="Ir a página 2"]').click()

	time.sleep(10)
	

if __name__ == '__main__':
    main()