import os
import platform

if platform.system().lower() == "windows":
	
	try:
		import mysql.connector
	
	except:
		query = input("Do you want to install the required package(Y/n): ")
	
		if query.lower() == 'y':
			os.system("pip install mysql.connector")
	
		else:
			exit()

elif platform.system().lower() == "linux":
	
	try:
		import mysql.connector
	
	except:
		query = input("Do you wish to install the required package(Y/n): ")
		
		if query.lower() == 'y':
			os.system("pip3 install mysql.connector")
		
		else:
			exit()
