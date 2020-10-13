import psycopg2
import psycopg2.extras

DB_HOST = "ec2-34-235-62-201.compute-1.amazonaws.com"
DB_NAME = "de5j3eiug6jr8t"
DB_USER = "lonhfypadrcwga"
DB_PASS = "47db36530ea1899a22c36daae1b3eadce120520c46e7b92a24eaf9144a2b1f22"

string = "Test"

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
with conn:
	with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
		#cur.execute("DROP TABLE Tabla_Hora;")  # Esto borra la tabla 
		#cur.execute("CREATE TABLE tabla_hora (id SERIAL PRIMARY KEY, hora VARCHAR);") # Crea tabla
		#cur.execute("INSERT INTO tabla_hora (hora) VALUES(%s)", ("primera hora",)) # Mete fila en la tabla
		#cur.execute("update tabla_hora set hora='segunda hora' where id='1';")  # Actualiza fila en la tabla
		cur.execute("SELECT * FROM tabla_hora;")	# Esta linea y la de abajo imprimen la tabla
		print(cur.fetchall())
		
		cur.execute("update tabla_hora set hora='{}' where id='1';".format(string))
		cur.execute("SELECT * FROM tabla_hora;")
		print(cur.fetchall())