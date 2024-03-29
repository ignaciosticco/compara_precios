'''
Este script se encarga de entrar a los sitios de los supermercados y obtener los precios de los productos
'''

# Nota: El programa a veces corre bien y aveces tira error. No se porque tiene este comportamiento aleatorio.

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PrecioBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def accede_al_sitio(self, url):

        self.driver.get("{}".format(url))

    def busca_producto(self, producto):

        id_busqueda = self.driver.find_element_by_id('search')
        id_busqueda.send_keys('{}'.format(producto))
        id_busqueda.send_keys(Keys.ENTER)

    def muestra_elementos(self):
        '''
		Imprime todos los elementos del sitio
		'''

        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for i in ids:
            print(i.tag_name)
            print(i.get_attribute('id'))

    def selecciona_elemento(self, elemento):

        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for i in ids:
            if i.tag_name == elemento or i.get_attribute('id') == elemento:
                print("tag name:", i.tag_name)
                print("ID:", i.get_attribute('id'))
                print("texto:", i.text)
            if i.get_attribute('id') == 'amlabel-product-price-44037':
                print("amb label:", i.text)

    def nombra_todo(self):

        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for i in ids:
            print("ID: {}\n".format(i.get_attribute('id')))
            print("Texto: {}\n".format(i.text))

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



    def imprime_lista_precios(self, producto_precio):
        '''
		Imprime en la terminal una tabla de productos y precios
		'''

        print("\nProducto\t\t\tPrecio ")
        for x in producto_precio:
            print("{}\t\t{}".format(x['name'], x['precio']))




def main():

    bot = PrecioBot()
    url = 'https://supermercado.carrefour.com.ar'
    bot.accede_al_sitio(url)
    #producto = 'coca cola'
    print("¿Qué producto buscas?\n")
    producto = str(input())
    bot.busca_producto(producto)

    time.sleep(2)  # Espera 2 seg antes de buscar los precios
    '''
    bot.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    ids = bot.driver.find_elements_by_xpath('//*[@id]')
    texto_data_productos = ids[0].text  # Estoy asumiendo que estan en el primer elemento de la lista de elementos
    producto_precio = bot.extrae_producto_y_precio(texto_data_productos)
    bot.imprime_lista_precios(producto_precio)

    boton = bot.driver.find_element_by_class_name("ver-mas-productos")
    time.sleep(20)
    

    ###
    ###Funciona
    bot.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    boton_mas_productos = bot.driver.find_element_by_class_name("ver-mas-productos") 
    print(boton_mas_productos)
    
    print(boton_mas_productos.is_displayed())
    bot.driver.execute_script("arguments[0].click();", boton_mas_productos)
    '''
         
    flag = True
    while flag:
        bot.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4) 
        print("in while")
        try:
            print("tryup")
            boton_mas_productos = bot.driver.find_element_by_class_name("ver-mas-productos") 
            if boton_mas_productos.is_displayed():
                bot.driver.execute_script("arguments[0].click();", boton_mas_productos)
                print("True")
            else:
                flag = False
                print("False")
            
            print("trydown")
        except:
            flag = False
            print("except")

    ids = bot.driver.find_elements_by_xpath('//*[@id]')
    texto_data_productos = ids[0].text  # Estoy asumiendo que estan en el primer elemento de la lista de elementos
    producto_precio = bot.extrae_producto_y_precio(texto_data_productos)
    bot.imprime_lista_precios(producto_precio)

    time.sleep(20)
if __name__ == '__main__':
    main()

