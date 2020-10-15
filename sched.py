import time
import schedule
import psycopg2
import psycopg2.extras
import datetime

DB_HOST = "ec2-34-235-62-201.compute-1.amazonaws.com"
DB_NAME = "de5j3eiug6jr8t"
DB_USER = "lonhfypadrcwga"
DB_PASS = "47db36530ea1899a22c36daae1b3eadce120520c46e7b92a24eaf9144a2b1f22"


def job():
	print("Print Sched")
	#string_hora = "Ultima actualizacion: {}".format(time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))
	delta_t = datetime.timedelta(hours=3) # porque BsAs esta a gmt-3
	string_hora = "Ultima actualizacion: {}".format((datetime.datetime.now()- delta_t).strftime('%Y-%m-%d %H:%M:%S'))

	conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
	with conn:
		with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
			cur.execute("update tabla_hora set hora='{}' where id='1';".format(string_hora))
	conn.close()

	return string_hora


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
