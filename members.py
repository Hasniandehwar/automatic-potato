from database import Database


class Members:
   
    def Add_member(self):
        conn=Database.connect_db()
        if conn is None:
            print("Database connection failed.")
            return False
        try: 
            cursor=conn.cursor()
            # Get member ID and Other details  from the user
            Member_id=int(input("Enter Member id: "))
            name= input("Enter the name :  ")
            Email= input("Enter your email: ")
            contact= int(input("Enter you c.Number:   "))
            query= """INSERT INTO MEMBERS (Member_id,name , email , phone )
            Values ( %s , %s , %s, %s) """

            cursor.execute(query,(Member_id,name, Email, contact))
            conn.commit()
            print("MEMBer_Added")
            return True
        
            # Addittional function we can add
            # s=self.name 
            # query_for__output='''select * from members where name= %s
            # '''
            # cursor.execute(query_for__output,(s))

            
            # rows=cursor.fetchall()

            # if rows:
            #     for row in rows:
            #         print(f"Your MEMBER ID: {row[0]}, USERNAME: {row[1]}, EMAIL : {row[2]}, Phone: {row[3]}")

            # else:
            #     print("USER is persent ")



        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    
    # For remove member
    def Remove_member(self):
        conn=Database.connect_db()
        if conn is None:
              print("Failed To connect: ")
              return False
        try:
              cursor=conn.cursor()
              id=int(input("Enter Member ID: "))
              Delete_query = "DELETE FROM MEMBERS WHERE Member_id = %s"
              num=(id,)
              cursor.execute(Delete_query, num)  
              conn.commit()
              print("Member removed ")
              return True
        except Exception as e:
                print(f"Error: {e}")
                return False
        finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()


    def View_member(self):         
         conn=Database.connect_db()
         if conn is None:
                  print("Connection is failed:")
                  return False
         try:            
             cursor=conn.cursor()
             query= "SELECT * FROM MEMBERS"
             cursor.execute(query)
             rows=cursor.fetchall()
             if rows:
                   print("Books in the Library:")
                   for row in rows:
                     print(f"Member  ID: {row[0]}, Name : {row[1]}, Email :  {row[2]}, Contact: {row[3]}")
             else:
                   print("No Members are in lab.")
         except Exception as e:
            print(f"Error: {e}")
            return False
         finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

c=Members()


c.View_member()
