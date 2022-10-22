# db-and-table-checker-python
This code checks if the required database (DB) and the related tables are present within the DB.

The main objective of this code is to check for the presence of the user entered database in the MySQL Command Line Client, by using the mysql.connector package/API
which can be downloaded. 

The way how the module works is as follows:

1) The presence of the package is processed, if found the code moves on. Else, the user is prompted for the permission to download the required package if the user declines the request, the code cannot be run.

2) The user is prompted to enter the MySQL Command Line Client's password.

3) 
