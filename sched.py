import time
import schedule

def job():
	print("Funciona")
	return "SI"


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
