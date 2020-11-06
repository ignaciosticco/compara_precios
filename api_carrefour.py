### ATENCION: Incluir sched rompio todo. Hay que ver que se puede hacer

from time import sleep
from flask import Flask, jsonify
from obtiene_precios_carrefour_v2 import PrecioBot
import time
from selenium import webdriver
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import psycopg2
import psycopg2.extras

DB_HOST = "ec2-34-235-62-201.compute-1.amazonaws.com"
DB_NAME = "de5j3eiug6jr8t"
DB_USER = "lonhfypadrcwga"
DB_PASS = "47db36530ea1899a22c36daae1b3eadce120520c46e7b92a24eaf9144a2b1f22"


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

	conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
	with conn:
		with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
			#cur.execute("SELECT * FROM tabla_hora;")
			cur.execute("SELECT * FROM tabla_hora WHERE id ='1';")
			string_web = "Ultima actualizacion: \n"+str(cur.fetchone()['hora'])+"\n\n"

			cur.execute("SELECT * FROM tabla_carrefour WHERE id ='1';")
			string_web += "Precio Leche: "+"$"+str(cur.fetchone()['precio'])+"\n"
			cur.execute("SELECT * FROM tabla_carrefour WHERE id ='2';")
			string_web += "Precio Coca: "+"$"+str(cur.fetchone()['precio'])+"\n"

			# TO DO: hacer que el string out incluya a los datos de los precios.

	return string_web 



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