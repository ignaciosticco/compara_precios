from time import sleep
from flask import Flask, jsonify
from obtiene_precios_carrefour_v2 import PrecioBot
import time
from selenium import webdriver
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--no-sandbox")
   
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


###################### DATA DE PRODUCTOS ######################
product_id = [1,2]
url1 = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
url2 = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'
lista_urls = [url1,url2]
lista_nombre_productos = ['Leche entera','Coca Cola']

app = Flask(__name__)

##################### TESTING #####################

@app.route('/')
def main():
	return "Hola mundo"


def job():
	return "SI"


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute



################################################### 





'''
@app.route('/')
def main():
	
	#En la landing page imprime los nombres y precios de los productos
	

	global lista_precio_out
	lista_precio_out = []
	bot = PrecioBot()
	string_out = 'Compara Precios de supermercados \n\nPrecios de Carrefour\n\n'

	for i in range (0,len(lista_urls)):
		
		bot.accede_al_sitio(lista_urls[i])
		time.sleep(4)
		precio = bot.driver.find_element_by_class_name("regular-price") 
		precio_out = bot.imprime_precio(precio)
		lista_precio_out+=[precio_out]

		string_out += "\nProducto: {}\nPrecio: ${}\n\n".format(lista_nombre_productos[i],precio_out)
	string_out+="\n\nUltima actualizacion: {}".format(time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))
		
	return string_out
	

@app.route('/json')
def solapa_json():

	#En la pagina /json muestra el diccionario de productos y precios 

	diccionario_out = {'nombre_producto':lista_nombre_productos,
	'precio_producto':lista_precio_out}

	return jsonify(diccionario_out)
'''