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


cur.execute("")
