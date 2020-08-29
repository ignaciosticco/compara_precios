from time import sleep
from flask import Flask, jsonify
from obtiene_precios_carrefour_v2 import PrecioBot
import time

app = Flask(__name__)


nombre = 'Leche'
precio = '12'



@app.route('/')
def main():

    #url = 'https://supermercado.carrefour.com.ar/desayuno-y-merienda/yerba/yerba-mate-la-merced-barbacua-500-g.html'
    #url = 'https://supermercado.carrefour.com.ar/bebidas/gaseosa-coca-cola-light-2-5-l.html'
    url = 'https://supermercado.carrefour.com.ar/lacteos-y-productos-frescos/leches/leche-entera-larga-vida-la-serenisima-3-1-l.html'
    
    bot = PrecioBot()
    bot.accede_al_sitio(url)
    time.sleep(2)
    precio = bot.driver.find_element_by_class_name("regular-price") 
    precio = bot.imprime_precio(precio)

    nombre = 'Leche entera'
    string_out = " Producto: {}\nPrecio: {}\n\nUltima actualizacion: {}".format(nombre,precio,time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    return string_out


if __name__ == '__main__':
    app.run(debug=True, port=4000)