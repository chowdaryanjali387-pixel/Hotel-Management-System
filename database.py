import mysql.connector 
def connect_db(): 
    conn = mysql.connector.connect( 
        host="localhost", 
      user="root", 
       password="MySQL1234", 
   database="bluebird_hotel" 
    ) 
    return conn
