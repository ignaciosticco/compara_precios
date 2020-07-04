'''
Este script se encarga de entrar a los sitios de los supermercados y obtener los precios de los productos
'''

# Nota: El programa a veces corre bien y aveces tira error. No se porque tiene este comportamiento aleatorio. 

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

def selecciona_elemento(elemento):

	ids = driver.find_elements_by_xpath('//*[@id]') 
	for i in ids:
		if i.tag_name==elemento or i.get_attribute('id')==elemento:
			print("tag name:",i.tag_name) 
			print("ID:",i.get_attribute('id')) 
			print("texto:",i.text)  
		if i.get_attribute('id')=='amlabel-product-price-44037':
			print("amb label:", i.text)

def nombra_todo():

	ids = driver.find_elements_by_xpath('//*[@id]') 
	for i in ids:
		print("ID: ",i.get_attribute('id'))
		print("Texto: ",i.text)	
		print(" ")

def devuelve_lista_precios():

	ids = driver.find_elements_by_xpath('//*[@id]') 
	for i in ids:
		if 'product-price' in i.get_attribute('id') and 'amlabel' not in i.get_attribute('id') :
			print("Precio = ",i.text)  

def main():

	url = 'https://supermercado.carrefour.com.ar'
	accede_al_sitio(url)
	producto = 'coca cola'
	busca_producto(producto)
	#muestra_elementos()
	#nombra_todo()
	#lista = driver.find_element_by_id('top').find_elements_by_tag_name('div')
	
	time.sleep(2)	# Espera 2 seg antes de buscar los precios 
	devuelve_lista_precios()


if __name__=='__main__':
     main()