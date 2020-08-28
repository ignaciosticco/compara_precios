


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PrecioBot:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def accede_al_sitio(self, url):

        self.driver.get("{}".format(url))


    def devuelve_lista_precios(self):

        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for i in ids:
            if 'product-price' in i.get_attribute(
                    'id') and 'amlabel' not in i.get_attribute('id'):
                print("Precio = ", i.text)


    def extrae_producto_y_precio(self, texto):
        '''
		Le pasas el texto donde estan todos los precios y extrae el nombre de los productos y sus precios. 
		Warning: Esta funcion solo sirve para Carrefour 
		'''

        lista_texto_dividido = texto.split("\n")
        lista_texto_dividido = [x for x in lista_texto_dividido
                                if x]  # saco los elementos vacios
        producto_precio = []
        for i in range(0, len(lista_texto_dividido)):
            if lista_texto_dividido[i][0] == '$':
                if "Por unidad" in lista_texto_dividido[i + 1]:
                    producto = lista_texto_dividido[i + 4]
                    precio = lista_texto_dividido[i]
                    producto_precio.append({
                        "name": producto,
                        "precio": float(precio.strip('$').replace(',','.'))
                    })
                else:
                    producto = lista_texto_dividido[i + 2]
                    precio = lista_texto_dividido[i]
                    producto_precio.append({
                        "name": producto,
                        "precio": float(precio.strip('$').replace('.','').replace(',','.'))
                    })

        return producto_precio





def main():

	bot = PrecioBot()
	url = 'https://supermercado.carrefour.com.ar/desayuno-y-merienda/yerba/yerba-mate-la-merced-barbacua-500-g.html'
	#url = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'
	#url = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
	bot.accede_al_sitio(url)

	time.sleep(4)


	price = bot.driver.find_element_by_class_name("regular-price")	

	if price.text =='':		
		print("Azul - Sin promos")
		price = bot.driver.find_elements_by_xpath("//*[contains(@id, 'product-price')]")
		print(price[1].text)

	else:
		print("Rojo - Con promos")
		print(price.text)



if __name__ == '__main__':
    main()