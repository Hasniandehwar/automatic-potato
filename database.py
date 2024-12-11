import mysql.connector



class Database:
    def connect_db():
        try:
            conn = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='Hasnain@1234',  
            database='library'  
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            return None


