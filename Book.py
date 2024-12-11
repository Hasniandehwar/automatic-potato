from database  import Database

#book management
class Books:
    


    def add_Book(self):
        # Establish database connection
        conn = Database.connect_db()  # Assuming Database.connect_db() is correctly implemented
        if conn is None:
            print("Database connection failed.")
            return False

        try:
            cursor = conn.cursor()

            # Taking user inputs
            book_Title = input("Enter Book title: ").strip()
            book_author = input("Enter the name of Book Author: ").strip()
            number_of_copies = int(input("How many copies you have: "))
            Book_id = int(input("Enter Book ID: "))

            # Insert query
            query = """
            INSERT INTO Books (book_id, Title, Author, Copies_available)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (Book_id, book_Title, book_author, number_of_copies))

            # Commit changes to the database
            conn.commit()

            print("Book added successfully!")
            return True

        except Exception as e:
            print(f"Error: {e}")
            return False

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if conn:
                conn.close()




    def update_books(self): # FOR UPDATING BOOKS IN DB
        conn = Database.connect_db()  # Assuming Database.connect_db() is correctly implemented
        if conn is None:  # Getting insure the data base is connceted 
            print("Database connection failed.")
            return False

        try:  
         cursor=conn.cursor()
         #USERS INPUT
         number_of_copies=int(input("How many number you wana add")) 
         book_author=input("Enter author name: ").strip()
         book_title=input("enter the title of book:  ").strip()


        # Update Query
         update_query = """
                        UPDATE Books
                        SET Copies_available = %s
                        WHERE Title = %s AND Author = %s;
                        """

         cursor.execute(update_query,(number_of_copies, book_author, book_title))
         # Commit changes to the database
         conn.commit()
         print("Number of copies updated")
         return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
        # Closing Connection    
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        





    def Delete_book(self):
        conn=Database.connect_db() 
        if conn is None:
            print("Database connection failed.")
            return False
        

        try:
            cursor=conn.cursor()

            Book_id=int(input("ENTER BOOK ID : "))


            # Delete Query
            Delete_query="DELETE FROM Books WHERE book_id = %s"
            # change the user input into tuple because it give error  to 1 parameters  
            para=(Book_id,)
            cursor.execute(Delete_query, para)
            conn.commit()
            print("Book is deleted ")

            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
            
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

   
    def count__book(self):
        conn = Database.connect_db()
        if conn is None:
            print("Database connection failed.")
            return False

        try:
            print("___________________________IF YOU WANT TO KNOW THE NUMBER OF BOOKS BY AUTHOR NAME OR TOTAL COUNT OF BOOKS:______________________")
            choice = input("Press 1 for total books, press 2 for books by a specific author: ").strip()
            cursor = conn.cursor()

            if choice == "1":
                query = "SELECT SUM(Copies_available) FROM Books WHERE Copies_available > 0;"
                cursor.execute(query)
                result = cursor.fetchone()  
                print(f"Total books available in the library: {result [0]}")

            elif choice == "2":
                author_name = input("Enter the Author's Name: ").strip()
                query = "SELECT COUNT(*) FROM Books WHERE Author = %s;"
                cursor.execute(query, (author_name,))  # Pass author_name as a tuple
                result = cursor.fetchone()  # Fetch the result
                print(f"Total books by {author_name}: {result[0]}")

            else:
                print("Invalid choice! Please enter 1 or 2.")
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def view_books(self):
        conn=Database.connect_db()

        if conn is None:
            print("Database connection failed.")
            return False
        try:
          cursor=conn.cursor()
          query= "Select * from Books "

          cursor.execute(query)
          rows=cursor.fetchall()

          if rows:
                print("Books in the Library:")
                for row in rows:
                    print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Copies Available: {row[3]}")
          else:
                print("No books found in the library.")

        except Exception as e:
            print(f"Error: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()



        

        









        

        


