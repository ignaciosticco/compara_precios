'''
Este script se encarga de entrar a los sitios de los supermercados y obtener los precios de los productos
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')


def accede_al_sitio(url):

	driver.get("{}".format(url))


def busca_producto(producto):

	id_busqueda = driver.find_element_by_id('search')
	id_busqueda.send_keys('{}'.format(producto))
	id_busqueda.send_keys(Keys.ENTER)

def muestra_elementos():
	'''
	Imprime todos los elementos del sitio
	'''

	ids = driver.find_elements_by_xpath('//*[@id]') 
	for i in ids:
		print(i.tag_name)
		print(i.get_attribute('id'))    

def main():

	url = 'https://supermercado.carrefour.com.ar'
	accede_al_sitio(url)
	producto = 'coca cola'
	busca_producto(producto)
	#muestra_elementos()

	lista = driver.find_element_by_id('top').find_elements_by_tag_name('div')
	print(lista)
	print(lista[0].get_attribute('id'))

if __name__=='__main__':
     main()