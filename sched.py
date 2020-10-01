import time
import schedule

def job():
	print("Funciona")
	string_out = "\n\nUltima actualizacion: {}".format(time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))
	return string_out


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    #time.sleep(1) # wait one minute
