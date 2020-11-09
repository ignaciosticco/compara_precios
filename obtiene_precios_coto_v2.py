from bs4 import BeautifulSoup
import requests
from requests import get
from selenium import webdriver


class precioBot_coto:


	def __init__(self):
		self.driver = webdriver.Chrome()

	def accede_al_sitio(self, url):
		self.driver.get("{}".format(url))


	def obtiene_precio(self,html):

		html_sting = str(html)
		texto_separado = html_sting.split('\n')
		texto_html_precio = 'PRECIO CONTADO'  # El precio de un producto aparece luego de este texto 

		i=0
		flag = True
		# Warning: estoy asumiendo que el primer precio que aprece es el correcto. 
		while i<len(texto_separado) and flag:
			if texto_html_precio in texto_separado[i]:
				j=0
				while j<len(texto_separado) and flag:
					if '$' in texto_separado[i+j]:
						precio = float(texto_separado[i+j].strip(' $').replace(',', ''))
						flag = False
						i = i+j-1
					j+=1
			i+=1

		return precio


def main():
	
	############ TESTEO ############ 
	bot = precioBot_coto()
	url = 'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-sin-azucar---botella-25-l-/_/A-00183936-00183936-200'
	#url = 'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-clasica-la-serenisima-larga-vida-1l/_/A-00253482-00253482-200'
	bot.accede_al_sitio(url)

	response = get(bot.driver.current_url)
	html_soup = BeautifulSoup(response.text, 'html.parser')
	precio = bot.obtiene_precio(html_soup)
	#bot.obtiene_precio(html_soup)
	print(precio)


if __name__ == '__main__':
    main()