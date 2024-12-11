from database import Database

from Admin import Admin
from membermenu import Member_menu



class Auth_admin:
    def username_exists(self, username):
        conn = Database.connect_db()  # Assuming the connect_db function is in the Database module
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "SELECT * FROM registration WHERE name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None

    def register_user(self, username, password):
        if self.username_exists(username):
            print("Username already exists. Please choose a different username.")
            return False

        conn = Database.connect_db()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO registration (name, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()

        cursor.close()
        conn.close()

        print("Registration successful! You can now log in.")
        return True

    def validate_login(self, username, password):
        conn = Database.connect_db()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "SELECT * FROM registration WHERE name = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None
    
   


class Auth_Member:
    def username_exists(self, username):
        conn = Database.connect_db()  # Assuming the connect_db function is in the Database module
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "SELECT * FROM registration_Member WHERE name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None

    def register_user(self, username, password):
        if self.username_exists(username):
            print("Username already exists. Please choose a different username.")
            return False

        conn = Database.connect_db()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO registration_Member (name, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()

        cursor.close()
        conn.close()

        print("Registration successful! You can now log in.")
        return True

    def validate_login(self, username, password):
        conn = Database.connect_db()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "SELECT * FROM registration_Member WHERE name = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None

    


def main():
    print("Welcome to the System")
    
    login_instance = Auth_admin()

    while True:

        print("\n Please select an option: ")
        print("1. As Admin: ")
        print("2. As Member: ")
        Frist_choice=str(input("Enter your choice: "))

        if Frist_choice=="1":
            print("\nPlease select an option:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
            
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                login_instance.register_user(username, password)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login_instance.validate_login(username, password):
                    print("Login Successful! Welcome!")
                    return Admin.admin_menu()
                else:
                    print("Login Failed! Invalid username or password.")
        
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break

            else:
                    print("Invalid choice. Please try again.")






        elif Frist_choice == "2":
            login_instance=Auth_Member()
            print("\nPlease select an option:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
            
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                login_instance.register_user(username, password)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login_instance.validate_login(username, password):
                    print("Login Successful! Welcome!")
                    return Member_menu.member_menu()
                else:
                    print("Login Failed! Invalid username or password.")
        
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        else:
                print("Invalid choice. Please try again.")







main()