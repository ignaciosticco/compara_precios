from time import sleep
from flask import Flask, jsonify
from obtiene_precios_carrefour_v2 import PrecioBot
import time
from selenium import webdriver
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule

def job():
	print("Funciona")
	return "SI"


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
