import time
import schedule
import psycopg2
import psycopg2.extras
import datetime
from obtiene_precios_carrefour_v2 import PrecioBot

DB_HOST = "ec2-34-235-62-201.compute-1.amazonaws.com"
DB_NAME = "de5j3eiug6jr8t"
DB_USER = "lonhfypadrcwga"
DB_PASS = "47db36530ea1899a22c36daae1b3eadce120520c46e7b92a24eaf9144a2b1f22"


def job():
	print("Print Sched up")
	delta_t = datetime.timedelta(hours=3) # porque BsAs esta a gmt-3
	string_hora = "{}".format((datetime.datetime.now()- delta_t).strftime('%Y-%m-%d %H:%M:%S'))

	lista_precio_out = actualiza_lista_precios()
	print(lista_precio_out)

	conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
	with conn:
		with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
			cur.execute("update tabla_hora set hora='{}' where id='1';".format(string_hora))
			
			cur.execute("update tabla_carrefour set precio='{}' where id='1';".format(str(lista_precio_out[0])))
			cur.execute("update tabla_carrefour set precio='{}' where id='2';".format(str(lista_precio_out[1])))
	conn.close()



	return string_hora


def actualiza_lista_precios():
	'''
	Esta funcion devuelve una lista con los precios actualizados
	'''


	url1 = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
	url2 = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'
	lista_urls = [url1,url2]

	lista_precio_out = []
	bot = PrecioBot()

	for i in range (0,len(lista_urls)):
		
		bot.accede_al_sitio(lista_urls[i])
		time.sleep(5)
		precio = bot.driver.find_element_by_class_name("regular-price") 
		precio_out = bot.imprime_precio(precio)
		lista_precio_out+=[precio_out]

	return lista_precio_out


def wakeup():
	print("UP and working (print)")
	return "UP and working"


schedule.every(5).minutes.do(wakeup)
schedule.every(90).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
