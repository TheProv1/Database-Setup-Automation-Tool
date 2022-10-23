# db-and-table-checker-python
This code checks if the required database (DB) and the related tables are present within the DB.

The main objective of this code is to check for the presence of the user entered database in the MySQL Command Line Client, by using the mysql.connector package/API
which can be downloaded. 

The way how the module works is as follows:

1) The presence of the package is processed, if found the code moves on. Else, the user is prompted for the permission to download the required package if the user declines the request, the code cannot be run.

2) The user is prompted to enter the MySQL Command Line Client's password. If the wrong password is entered the program/code exits.

3) The user is prompted to enter the name of the database.

4) The function "db_searcher" checks for the user entered database in the mysql client's list of databases.

5) If the database is found, a message is displayed. Else, the database can be created.

6) The database is switched.

7) The number and names of the table are entered by the user.

8) The function "table_searcher" checks for the user entered tables within the  
