from time import sleep
from flask import Flask, jsonify
from obtiene_precios import PrecioBot

app = Flask(__name__)


@app.route('/producto/<string:nombre>')
def producto(nombre):
    print(nombre)
    productoPrecio = getPrecios(nombre)
    return jsonify(productoPrecio)


def getPrecios(producto):
    bot = PrecioBot()
    url = 'https://supermercado.carrefour.com.ar'
    bot.accede_al_sitio(url)
    bot.busca_producto(producto)
    sleep(2)
    ids = bot.driver.find_elements_by_xpath('//*[@id]')
    texto_data_productos = ids[
        0].text  # Estoy asumiendo que estan en el primer elemento de la lista de elementos
    producto_precio = bot.extrae_producto_y_precio(texto_data_productos)
    bot.imprime_lista_precios(producto_precio)
    return producto_precio


if __name__ == '__main__':
    app.run(debug=True, port=4000)