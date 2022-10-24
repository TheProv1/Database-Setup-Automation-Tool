import package_checker

passwd = input("Enter the MySQL Command Line Client Password: ")

conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)

if conobj.is_connected:
	print("Connected Successfully")
else:
	print("Password Entered is Incorrect")
	exit()
	
cur = conobj.cursor()

db_name = input("Enter the name of the required database: ")
db = (db_name,)

cur.execute("show databases")
db_tup = cur.fetchall()

def db_searcher():
	'''
	This function searches the tuple "db_tup" for the required database / user required database "db_name".
	'''
	if db in db_tup:
		print("The database", db, "exists in the Client")
	
	else:
		print('The database', db, 'does not exist in the Client\n')
		db_query = input("Do you wish to create the required database?(Y/n): ")
		print()
		if db_query.lower() == "y":
			print("Creating Database")
			db_create_cmd = "create database " + db_name
			cur.execute(db_create_cmd)
			cur.execute("commit")
			print("\nDatabase", db_name, "Created Successfully")
	
		else:
			print("Exiting Program")
			exit()
	
	db_switch = "use " + db_name
	cur.execute(db_switch)

n = int(input("Enter the number of table(s): "))
t_lst = []

for i in range(n):
	t_name = input("Enter the name of the table: ")
	t_lst.append(t_name)

t_tup = tuple(t_lst)

cur.execute("show tables")
tb_tup = cur.fetchall()

def table_searcher():
	'''
	This function searches the database for the table(s) entered by the user.
	'''
	if t_tup in tb_tup:
		print("The table(s) is/are present within the database")
	else:
		print("The table(s) is/are missing")
