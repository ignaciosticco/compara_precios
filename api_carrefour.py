from time import sleep
from flask import Flask, jsonify
from obtiene_precios_carrefour_v2 import PrecioBot
import time

app = Flask(__name__)



product_id = [1,2]
url1 = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
url2 = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'
lista_urls = [url1,url2]
lista_nombre_productos = ['Leche entera','Coca Cola']




@app.route('/')
def main():
	'''
	En la landing page imprime los nombres y precios de los productos
	'''

	global lista_precio_out
	lista_precio_out = []

	bot = PrecioBot()
	string_out = 'Precios de Carrefour\n\n'
	for i in range (0,len(lista_urls)):
		bot.accede_al_sitio(lista_urls[i])
		time.sleep(4)
		precio = bot.driver.find_element_by_class_name("regular-price") 
		precio_out = bot.imprime_precio(precio)
		lista_precio_out+=[precio_out]

		string_out += "\nProducto: {}\nPrecio: ${}\n\n".format(lista_nombre_productos[i],precio_out)
		print(string_out)
		string_out+="\n\nUltima actualizacion: {}".format(time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))
	return string_out


@app.route('/json')
def solapa_json():
	'''
	En la pagina /json muestra el diccionario de productos y precios 
	'''

	diccionario_out = {'nombre_producto':lista_nombre_productos,
						'precio_producto':lista_precio_out}
	
	return jsonify(diccionario_out)


if __name__ == '__main__':
    app.run(debug=True, port=4000)