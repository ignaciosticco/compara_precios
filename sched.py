import time
import schedule

def job():
	print("Funciona")
	string_out = "\n\nUltima actualizacion: {}".format(time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))
	print("{}".format(string_out))
	return string_out


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
