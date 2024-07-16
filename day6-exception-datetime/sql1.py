
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost:3307", user = "root",passwd = "root")  
  
#printing the connection object   
print(myconn)   