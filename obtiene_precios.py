'''
Este script se encarga de entrar a los sitios de los supermercados y obtener los precios de los productos
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://supermercado.carrefour.com.ar")

id_busqueda = driver.find_element_by_id('search')
id_busqueda.send_keys('coca cola')
id_busqueda.send_keys(Keys.ENTER)


titles = driver.find_elements_by_xpath('//div[@class="producto-info"]')
#titles = driver.find_elements_by_xpath('//div[@class="home-product-cards container_tg"]')
#titles = driver.find_elements_by_xpath('//div[@class="col s12 product-card product-card-food"]')

print(titles)   


