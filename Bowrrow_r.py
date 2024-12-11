from database import Database
import datetime
class Borrow_return:
    
    def borrow_book(self):
        conn = Database.connect_db()
        if conn is None:
            print("Database connection failed.")
            return False
    
        try:
            cursor = conn.cursor()

            member_id = int(input("Enter Member Id: "))
            book_id = int(input("Enter Book ID you are borrowing: "))

            # Verify if member_id exists
            cursor.execute("SELECT COUNT(*) FROM Members WHERE Member_id = %s;", (member_id,))
            if cursor.fetchone()[0] == 0:
                print("Invalid Member ID. Please try again.")
                return False

            # Verify if book_id exists
            cursor.execute("SELECT Copies_available FROM Books WHERE book_id = %s;", (book_id,))
            result = cursor.fetchone()
            if not result:
                print("Invalid Book ID. Please try again.")
                return False

            # Check if the book is available
            if result[0] > 0:  # Book is available
                # Decrease the available copies
                d_query = "UPDATE Books SET Copies_available = Copies_available - 1 WHERE book_id = %s;"
                cursor.execute(d_query, (book_id,))

                # Insert a new transaction
                t_query = """INSERT INTO Transactions (member_id, book_id, borrow_date, return_date, fine) 
                             VALUES (%s, %s, CURDATE(), NULL, 0);"""    
                cursor.execute(t_query, (member_id, book_id))

                conn.commit()
                print("Book borrowed successfully!")
            else:
                print("The book is not available.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()




    def return_book(self):
        
        conn = Database.connect_db()
        if conn is None:
            print("Database connection failed.")
            return False

        try:
            cursor = conn.cursor()

            # Get member ID and book ID from the user
            member_id = int(input("Enter Member ID: "))
            book_id = int(input("Enter Book ID: "))

            # Find the active transaction
            cursor.execute(
                "SELECT borrow_date FROM Transactions WHERE member_id = %s AND book_id = %s AND return_date IS NULL;", 
                (member_id, book_id)
            )
            result = cursor.fetchone()

            if result:
                borrow_date = result[0]
                allowed_days = 14  # For example, 2 weeks allowed
                fine_per_day = 5   # Example: 5 currency units per day
                days_borrowed = (datetime.date.today() - borrow_date).days

                # Calculate fine
                fine = max(0, (days_borrowed - allowed_days) * fine_per_day)

                # Update transaction record
                cursor.execute(
                    "UPDATE Transactions SET return_date = CURDATE(), fine = %s WHERE member_id = %s AND book_id = %s AND return_date IS NULL;",
                    (fine, member_id, book_id)
                )

                # Increase the available copies
                cursor.execute("UPDATE Books SET Copies_available = Copies_available + 1 WHERE book_id = %s;", (book_id,))

                conn.commit()
                print(f"Book returned successfully! Fine: {fine}")
            else:
                print("No active transaction found for this member and book.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


