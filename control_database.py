import psycopg2
import psycopg2.extras

DB_HOST = "ec2-34-235-62-201.compute-1.amazonaws.com"
DB_NAME = "de5j3eiug6jr8t"
DB_USER = "lonhfypadrcwga"
DB_PASS = "47db36530ea1899a22c36daae1b3eadce120520c46e7b92a24eaf9144a2b1f22"


conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
with conn:
	with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
		#cur.execute("DROP TABLE productos;")  # Esto borra la tabla productos
		cur.execute("CREATE TABLE hora (hora_id int, hora_actual VARCHAR(200));") 
